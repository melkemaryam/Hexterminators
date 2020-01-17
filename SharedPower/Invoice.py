''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Invoice.py

Created: 17th November 2019

-------------------------------------------------
'''

from DatabaseConnection import DatabaseConnection

import numpy
import pandas
#for tables and making them fancy

from datetime import datetime
import calendar
#for checking the time

import pause
#for scheduling invoicing

import smtplib
#import the smtplib module for setting up mail connection. It should be included in Python by default

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#more emailing from python stuff

class Invoice:
    
    #constructor
    def __init__(self, invoice_id, customer_id, customer_firstname, customer_lastname, customer_email, tool_ID, tool_name, price, duration, rental_list, format_invoice, invoice_table, databaseFilename, registeredUser):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.customer_firstname = customer_firstname
        self.customer_lastname = customer_lastname
        self.customer_email = customer_email
        self.tool_ID = tool_ID
        self.tool_name = tool_name
        self.price = price
        self.duration = duration
        self.rental_list = rental_list
        self.invoice_table = invoice_table
        self.format_invoice = format_invoice
        self.databaseFilename = databaseFilename
        self.registeredUser = registeredUser

    '''
    Function name: getData()
    Task: for finding customer in the DB using email address
    '''

    def getData(self, customer_email):
        
        # Connecting to the DB
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
        cursor = databaseConnection.cursor()

        cursor.execute('SELECT cust_id, F_name, L_name, email FROM customers WHERE email = ?', customer_email,)

        customer_row=cursor.fetchone()

        if (customer_row != None):

            customer_id = customer_row[0]
            customer_firstname = customer_row[1]
            customer_lastname = customer_row[2]
            customer_email = customer_row[3]

        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection(self.databaseFilename)

        return customer_id, customer_firstname, customer_lastname, customer_email
        #presenting the Customer back to us

    '''
    Function name: getTool()
    Task: for getting all the tools used by customer for last month
    '''

    def getTool(self, customer_id):

        rental_list = ['Tool Name', 'Day Price', 'Rental Duration', 'Total Price']
        grand_total = 0

        date = (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")+"-01"
        date_end = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)

        delivery_charge = 5
        insurance_charge = 5
        
        # Connecting to the DB
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
        cursor = databaseConnection.cursor()

        cursor.execute('''SELECT tool_id, price, duration, cust_id, delivery, late_return FROM Bookings WHERE cust_id= ? AND strftime('%s', date) BETWEEN strftime('%s', start_date) AND strftime('%s', end_date)'''), (customer_id, date, date_end,)
        
        tool_row=cursor.fetchall()
        for booking in tool_row:
            #checking if customer with given id borrowed any tools and if it was more than one creating a list

            customer_id = booking[0]
            tool_id = booking[1]
            price = booking[2]
            duration = booking[3]
            deliveries_charge = booking[4] * delivery_charge
            late_charge = booking [5]
            total_price = int(price) * int(duration) + int(late_charge)
            rental_list.append(tool_id, price, duration, total_price)
            #rental lines creation based on retrieved data
        
        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection(self.databaseFilename)

        grand_total = grand_total + total_price + deliveries_charge + insurance_charge

        return rental_list, grand_total
        #presenting the Rental lines back to us
    
    '''
    Function name: cut_list()
    Task: rearranging a single list from the getTool() function into a table for the invoice to be generated
    '''

    def cut_list(self, rental_list):
    
        tool_droppings = numpy.asarray(rental_list)
        invoice_table = numpy.reshape(tool_droppings, (-1,5))
        return invoice_table
            
    '''
    Function name: generate_invoice
    Task: Building the actual invoice - message and numbers together
    '''

    def generate_invoice(self, rental_list, grand_total, invoice_table, customer_firstname, customer_lastname):

        invoice_main_body = pandas.DataFrame(invoice_table, columns=['Tool Name', 'Day Price', 'Rental Duration', 'Total Price'])
        
        #adding headers to the numpy array to make it more table-like (should be neat)
        name = customer_firstname + ' ' + customer_lastname
        period = str(datetime.now().month) + ' ' + str(datetime.now().year)
        customer_info = (name, period, invoice_main_body, grand_total)
        
        format_invoice = ("""Hello %s,
        Please find your invoice for %s below: 
        %s
        Totaling at: %s

        Thank you for using SharedPower.""" % customer_info)
        return format_invoice
        
    '''
    Function name: send_invoice()
    Task: sends the invoice away
    '''

    def send_invoice(self, customer_email, format_invoice):

        # give it access to a basic SharedPower customer services email address
        MY_ADDRESS = 'breo.Piotr.Hexterminators@study.beds.ac.uk'
        PASSWORD = 'need.to.hash.this.away'
        
        # set up the SMTP server as we use outlook 365
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        
        #create a message
        msg = MIMEMultipart()       

        message = format_invoice

        #setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']= customer_email
        msg['Subject']="This is your monthly SharedPower invoice"
        
        #add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #send the message via the server set up earlier.
        s.send_message(msg)
        
        del msg

        s.quit()
        

    '''
    Function name: getList()
    Task: for finding the customer in the DB using teh email address
    '''

    def getList(self):

        # Connecting to the DB
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
        cursor = databaseConnection.cursor()
        cursor.execute('SELECT customer_email FROM customers;' )
        mailing_list=cursor.fetchall()

        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection(self.databaseFilename)

        #presenting the Customer list back to us
        return mailing_list


    '''
    Function name: run_month()
    Task: Assuming the code runs non-stop, it sends an invoice to every customer at the start of every month
    '''

    def run_month(self, invoice_id, customer_id, customer_firstname, customer_lastname, customer_email, tool_ID, tool_name, price, duration, rental_list, format_invoice, invoice_table, mailing_list, grand_total, databaseFilename):
        
        Invoice.getList(self)
        #constructing library of email invoices should be sent to
        length = len(mailing_list)
        
        for mailing_list in range(length):
            
            #for each email in the database
            Invoice.getData(self, customer_email)
            
            #get customer data
            Invoice.getTool(self, customer_id)
            
            #get their bookings data
            Invoice.cut_list(self,rental_list)
            Invoice.generate_invoice(self, rental_list, grand_total, invoice_table, customer_firstname, customer_lastname)
            Invoice.send_invoice(self, customer_email, format_invoice)
        
    '''
    Function name: time_stuff()
    Task: Setting the time to zero in case the code is not started at the start of the month 
    '''
    
    def time_stuff(self):
        start = 0
        start_date = (datetime.now().year, (datetime.now().month + 1), 1)
        if start == 0:
            pause.until(start_date)
            start +=1
            
        else:
            pause.days(calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month))
            #triggering the invoice sending on the first of subsequent months (pause module manual states even if the machine goes into standby over the event time it should re-run the moment it wakes up)
       
