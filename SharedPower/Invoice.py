''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Invoice.py

Created: 17th November 2019

-------------------------------------------------
'''

from DatabaseConnection import DatabaseConnection
#for talking to the database
import sqlite3
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
    def __init__(self, invoice_id, customer_id, customer_firstname, customer_lastname, customer_email, tool_ID, tool_name, price, duration, rental_list, format_invoice, invoice_table, databaseFilename):
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

'''
Function name: getData()
Task: for finsing customer in the base using email address
'''
    def getData(self, customer_email):
        # Connecting to the DB
        DatabaseConnection.CreateDBConnection()
        cursor.execute('SELECT cust_id, F_name, L_name, email FROM customer WHERE email = ?', customer_email )
        customer_row=cursor.fetchone()
        if (customer_row != None):
            #checking if customer with given email exists (if doesn't will return 'None')

            customer_id = customer_row[0]
            customer_firstname = customer_row[1]
            customer_lastname = customer_row[2]
            customer_email = customer_row[3]
            #customer creation based on retrieved data

        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection()

        return customer_id, customer_firstname, customer_lastname, customer_email
        #presenting the Customer back to us

'''
Function name: getTool()
Task: for getting all the tools used by customer for last month
'''
    def getTool(self, customer_id):
        #for getting all the tools used by customer for last month

        rental_list = ['Tool Name', 'Day Price', 'Rental Duration', 'Total Price']
        grand_total = 0
        date = (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")+"-01"
        date_end = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        delivery_charge = 5
        insurance_charge = 5
        
        # Connecting to the DB
        DatabaseConnection.CreateDBConnection()
        cursor.execute('''SELECT tool_id, price, duration, cust_id, delivery, late_return FROM booking WHERE cust_id= ? AND strftime('%s', date) BETWEEN strftime('%s', start_date) AND strftime('%s', end_date)'''), (customer_id, date, date_end)
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
        DatabaseConnection.CloseDBConnection()

        grand_total = grand_total + total_price + deliveries_charge + insurance_charge

        return rental_list, grand_total
        #presenting the Rental lines back to us
    
    def cut_list(self, rental_list):
        #rearranging single list from getTool function into a table for the invoice to be generated
    
        tool_droppings = numpy.asarray(rental_list)
        invoice_table = numpy.reshape(tool_droppings, (-1,5))
        return invoice_table
        
'''
Function name: generate_invoice
Task: Building the actual invoice - message and numbers together
'''
    def generate_invoice(self, rental_list, grand_total, invoice_table, customer_firstname, customer_lastname):
        #building the actual invoice - message and numbers together

        invoice_main_body = pandas.DataFrame(invoice_table, columns=['Tool Name', 'Day Price', 'Rental Duration', 'Total Price'])
        #adding headers to numpy array to make it more table-like (should be neat)
        name = customer_firstname + ' ' + customer_lastname
        period = str(datetime.now().month) + ' ' + str(datetime.now().year)
        customer_info = (name, period, invoice_main_body, grand_total)
        format_invoice = ("""Hello %s,
        Please find your invoice for %s below: 
        %s
        Totaling at: %s

        Thank you for using SharedPower.""" % customer_info)
        return format_invoice
        #e voila!
    
'''
Function name: send_invoice()
Task: Now for sending the bitch away >.<
'''
    def send_invoice(self, customer_email, format_invoice):

        MY_ADDRESS = 'breo.Piotr.Hexterminators@study.beds.ac.uk'
        PASSWORD = 'need.to.hash.this.away'
        #give it access to basic SharedPower customer services email address

        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        #set up the SMTP server as we use outlook 365

        msg = MIMEMultipart()       #create a message

        message = format_invoice

        msg['From']=MY_ADDRESS
        msg['To']= customer_email
        msg['Subject']="This is your monthly SharedPower invoice"
        #setup the parameters of the message

        msg.attach(MIMEText(message, 'plain'))
        #add in the message body

        s.send_message(msg)
        #send the message via the server set up earlier.
    
        del msg

        s.quit()
        #clean up done

'''
Function name: getList()
Task: For finding customer in the base using email address
'''
    def getList(self):

        # Connecting to the DB
        DatabaseConnection.CreateDBConnection()
        cursor.execute('SELECT customer_email FROM customer;' )
        mailing_list=cursor.fetchall()

        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection()

        return mailing_list
        #presenting the Customer list back to us
    
    
'''
Function name: run_month()
Task: Assuming the code runs non-stop, it sends an invoice to every customer at the start of every month
'''
    def run_month(self, invoice_id, customer_id, customer_firstname, customer_lastname, customer_email, tool_ID, tool_name, price, duration, rental_list, format_invoice, invoice_table, mailing_list, grand_total):
        
        self.getList()
        #constructing library of email invoices should be sent to
        length = len(mailing_list)
        
        for mailing_list in range(length):
            #for each email in the database
            self.getData(customer_email)
            #get customer data
            self.getTool(customer_id)
            #get their bookings data
            self.cut_list(rental_list)
            self.generate_invoice(rental_list, grand_total, invoice_table, customer_firstname, customer_lastname)
            self.send_invoice(customer_email, format_invoice)
    
'''
Function name: timr_stuff()
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
       
