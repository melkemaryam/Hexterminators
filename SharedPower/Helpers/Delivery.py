''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Delivery.py

Created: 17th November 2020

-------------------------------------------------
'''

import sqlite3
from Helpers.DatabaseConnection import DatabaseConnection

class Delivery:
   
    # Constructor
    def __init__(self, book_id, databaseFilename):
        self.book_id = book_id
        self.databaseFilename = databaseFilename

    '''
    Function name: add_delivery_charge()
    Task: Adds the delivery charges if needed to their account
    '''
    def add_delivery_charge(self, book_id):
        # Connecting to the DB
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
        
        #cursor creation for talking to db
        cursor = databaseConnection.cursor() 

        cursor.execute('UPDATE bookings SET delivery = delivery + 1 WHERE book_id = ?', book_id,)
        databaseConnection.commit()
        # Disconnecting from the DB
        DatabaseConnection.CloseDBConnection(self.databaseFilename)
