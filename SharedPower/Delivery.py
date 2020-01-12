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
    def __init__(self, book_id):
        self.book_id = book_id
    
    def add_delivery_charge(self, booking_id):
        DatabaseConnection.CreateDBConnection(databaseFilename)
        
        cursor = databaseConnection.cursor()
        #cursor creation for talking to db

        cursor.execute('UPDATE booking SET delivery = delivery + 1 WHERE book_id = ?', book_id)
        
        DatabaseConnection.CloseDBConnection(databaseFilename)
        
