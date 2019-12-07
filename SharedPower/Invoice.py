import sqlite3

class Invoice:
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id

    def getData(database_filename):
        theCustomer = None
        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT customer_ID, customer_forename, customer_surname, customer_email FROM customer WHERE customer_email = ?'), (customer_email,))
        customer_row=cursor.fetchone()
        if (customer_row != None):
            #checking if customer with given email exists (if doesn't will return 'None')

            customer_id = customer_row[0]
            customer_forename = customer_row[1]
            customer_surname = customer_row[2]
            customer_email = customer_row[3]
            theCustomer = Customer (customer_id, customer_forename, customer_surname, customer_email)
            #customer creation based on retrieved data

        database_connection.close()
        #close db conection to free resources

        return theCustomer
        #presenting the Customer back to us

    def getTool(database_filename)
        rental.list = []
        database_connection = sqlite3.connect(database_filename)
        #estabilishing a db connection

        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('SELECT tool_ID, tool_name, price, duration, customer_id FROM tool WHERE customer_id= ?'), (customer_id,))
        tool_row=cursor.fetchall()
        for tool in tool_rows:
            #checking if customer with given id borrowed any tools and if it was more than one creating a list

            customer_id = tool[0]
            tool_name = tool[1]
            price = tool[2]
            duration = tool[3]
            total_price = int(price) * int(duration)
            theTool = Tool (customer_id, tool_name, price, duration, total_price)
            rentalList.append(theTool)
            #rental lines creation based on retrieved data

        database_connection.close()
        #close db conection to free resources

        return rental.list
        #presenting the Rental lines back to us
            
import smtplib
# import the smtplib module. It should be included in Python by default

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
# set up the SMTP server as we use outlook 365