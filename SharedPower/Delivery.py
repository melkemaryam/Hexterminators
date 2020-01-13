''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Delivery.py

Created: 17th November 2020

-------------------------------------------------
'''

import sqlite3
from DatabaseConnection import DatabaseConnection

class Delivery:
    # Constructor
    def __init__(self, book_id):
        self.book_id = book_id

'''
Function name: add_delivery_charge()
Task: Adds the delivery charges if needed to their account
'''
    def add_delivery_charge(self, booking_id):
        # Connecting to the DB
        DatabaseConnection.CreateDBConnection(databaseFilename)
        
        #cursor creation for talking to db
        cursor = databaseConnection.cursor()

        cursor.execute('UPDATE booking SET delivery = delivery + 1 WHERE book_id = ?', book_id)
        
        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection(databaseFilename)
