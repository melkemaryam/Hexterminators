import sqlite3
#for talking to the database
import numpy
import pandas
#for tables and making them fancy
from datetime import datetime
#for checking the time
import smtplib
#import the smtplib module for setting up mail connection. It should be included in Python by default
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#more emailing from python stuff

class Invoice:
    def __init__(self, invoice_id, customer_id, customer_forename, customer_surname, customer_email, tool_ID, tool_name, price, duration, rental_list, format_invoice, invoice_table):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.customer_forename = customer_forename
        self.customer_surname = customer_surname
        self.customer_email = customer_email
        self.tool_ID = tool_ID
        self.tool_name = tool_name
        self.price = price
        self.duration = duration
        self.rental_list = rental_list
        self.invoice_table = invoice_table
        self.format_invoice = format_invoice

    def getData(self, customer_email, database_filename):
        #for finding customer in the base using email address

        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT customer_ID, customer_forename, customer_surname, customer_email FROM customer WHERE customer_email = ?', customer_email )
        customer_row=cursor.fetchone()
        if (customer_row != None):
            #checking if customer with given email exists (if doesn't will return 'None')

            customer_forename = customer_row[1]
            customer_surname = customer_row[2]
            customer_email = customer_row[3]
            #customer creation based on retrieved data

        database_connection.close()
        #close db conection to free resources

        return customer_forename, customer_surname, customer_email
        #presenting the Customer back to us

    def getTool(self, customer_id, database_filename):
        #for getting all the tools used by customer for last month

        rental_list = ['Tool Name', 'Day Price', 'Rental Duration', 'Total Price']
        grand_total = 0
        date = ('01-' + str(datetime.now().month - 1) + '-' + str(datetime.now().year))
        date_end = ('31-' + str(datetime.now().month - 1) + '-' + str(datetime.now().year))
        database_connection = sqlite3.connect(database_filename)
        #deliveries_charge = 
        #insurance_charge =
        ####

    
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT tool_name, price, duration, customer_id FROM tool WHERE customer_id= ? AND date=< ? AND date=<'), (customer_id, date, date_end)
        tool_row=cursor.fetchall()
        for tool in tool_row:
            #checking if customer with given id borrowed any tools and if it was more than one creating a list

            customer_id = tool[0]
            tool_name = tool[1]
            price = tool[2]
            duration = tool[3]
            total_price = int(price) * int(duration)
            grand_total = grand_total + total_price + deliveries_charge + insurance_charge
            rental_list.append(tool_name, price, duration, total_price)
            #rental lines creation based on retrieved data

        database_connection.close()
        #close db conection to free resources
        return rental_list, grand_total
        #presenting the Rental lines back to us
    
    def cut_list(self, rental_list):
        #rearranging single list from getTool function into a table for the invoice to be generated
    
        tool_droppings = numpy.asarray(rental_list)
        invoice_table = numpy.reshape(tool_droppings, (-1,4))
        return invoice_table
        
    def generate_invoice(self, rental_list, grand_total, invoice_table, customer_forename, customer_surname):
        #building the actual invoice - message and numbers together

        invoice_main_body = pandas.DataFrame(invoice_table, columns=['Tool Name', 'Day Price', 'Rental Duration', 'Total Price'])
        #adding headers to numpy array to make it more table-like (should be neat)
        name = customer_forename + ' ' + customer_surname
        period = str(datetime.now().month) + ' ' + str(datetime.now().year)
        customer_info = (name, period, invoice_main_body, grand_total)
        format_invoice = ("""Hello %s,
        Please find your invoice for %s below: 
        %s
        Totaling at: %s

        Thank you for using SharedPower.""" % customer_info)
        return format_invoice
        #e voila!
    
    def send_invoice(self, customer_email, format_invoice):
        #now for sending the bitch away >.<

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
        
    def getList(self, database_filename):
        #for finding customer in the base using email address

        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT customer_email FROM customer;' )
        mailing_list=cursor.fetchall()

        database_connection.close()
        #close db conection to free resources

        return mailing_list
        #presenting the Customer list back to us
    
    def run_month(self, database_filename):
        getList(database_filename)
        length = len(mailing_list)
        
        for i in range(length):
            getData(mailing_list)
            getTool(mailing_list)
            cut_list(mailing_list)
            generate_invoice(mailing_list)
            send_invoice(mailing_list)
            
