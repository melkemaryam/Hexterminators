import sqlite3
import pandas
from datetime import datetime

class Invoice:
    def __init__(self, invoice_id, customer_id, customer_forename, customer_surname, customer_email, tool_ID, tool_name, price, duration):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.customer_forename = customer_forename
        self.customer_surname = customer_surname
        self.customer_email = customer_email
        self.tool_name = tool_name
        self.price = price
        self.duration = duration

    def getData(self, database_filename):
        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT customer_ID, customer_forename, customer_surname, customer_email FROM customer WHERE customer_email = ?', customer_email )
        customer_row=cursor.fetchone()
        if (customer_row != None):
            #checking if customer with given email exists (if doesn't will return 'None')

            customer_id = customer_row[0]
            customer_forename = customer_row[1]
            customer_surname = customer_row[2]
            customer_email = customer_row[3]
            #customer creation based on retrieved data

        database_connection.close()
        #close db conection to free resources

        return customer_id, customer_forename, customer_surname, customer_email
        #presenting the Customer back to us

    def getTool(self, database_filename):
        rental_list = ['Tool Name', 'Day Price', 'Rental Duration', 'Total Price']
        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT tool_name, price, duration, customer_id FROM tool WHERE customer_id= ?'), (customer_id,)
        tool_row=cursor.fetchall()
        for tool in tool_row:
            #checking if customer with given id borrowed any tools and if it was more than one creating a list

            customer_id = tool[0]
            tool_name = tool[1]
            price = tool[2]
            duration = tool[3]
            total_price = int(price) * int(duration)
            rental_list.append(tool_name, price, duration, total_price)
            #rental lines creation based on retrieved data

        database_connection.close()
        #close db conection to free resources
        return rental_list
        #presenting the Rental lines back to us
    
    def cut_list(self):
        items = len(rental_list)
        rows = items/4
        for x_i in range(rows):
            yield [rental_list[y_i] for y_i in range(x_i, items, rows)]
        #rearranging single list into list of lists for each line of the invoice to be generated
    
    def generate_invoice(self):
        invoice_main_body = pandas.DataFrame(rental_list, columns=headers)
        #returns list of lists as table (should be neat)
        grand_total = invoice_main_body['Total Price'].sum
        #collects all the single total prices from subsequent lines
        name = customer_forename + ' ' + customer_surname
        period = str(datetime.now().month) + ' ' + str(datetime.now().year)
        customer_info = (name, period, invoice_main_body, grand_total)
        format_invoice ="""Hello %s,
        Please find your invoice for %s below: 
        %s
        Totaling at: %s
        Thank you for using SharedPower."""
        return (format_invoice % customer_info)
        #e voila!
#now for sending the bitch away >.<
            
import smtplib
# import the smtplib module. It should be included in Python by default

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
# set up the SMTP server as we use outlook 365
