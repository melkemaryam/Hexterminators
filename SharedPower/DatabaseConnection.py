''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: DatabaseConnection.py

Created: 27th December 2019

-------------------------------------------------
'''

import sqlite3
from sqlite3 import Error

class DatabaseConnection:
    
    # -------------------------------------------------
    # Connect to an existing sqlite database
    # -------------------------------------------------
    @staticmethod
    def CreateDBConnection(database_filename):
    
        database_connection = None
        function_name = 'Create_DB_Connection'
        
        try:
            database_connection = sqlite3.connect(database_filename)
                
        except Error as e:
            print(__name__, ':', function_name, ":", e)
            raise

        return database_connection

    # -------------------------------------------------
    # Close a sqlite database connection
    # -------------------------------------------------
    @staticmethod
    def CloseConnection(database_connection):

        function_name = 'Close_DB_Connection'
        
        try:
            database_connection.close()        
                
        except Error as e:
            print(__name__, ':', function_name, ":", e)
            raise
            



    
