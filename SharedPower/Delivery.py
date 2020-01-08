import sqlite3
from DatabaseConnection import DatabaseConnection

class Delivery:
    def __init__(self):
        self.booking_id = booking_id
    
    def add_delivery_charge(self, booking_id):
        DatabaseConnection.CreateDBconnection(database_filename)
        
        cursor = database_connection.cursor()
        #cursor creation for talking to db

        cursor.execute('UPDATE booking SET delivery = delivery + 1 WHERE book_id = ?', booking_id )
        
        DatabaseConnection.CloseConnection(database_filename)
        
