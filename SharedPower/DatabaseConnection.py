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
    
    '''
    Function name: createDBConnection
    Task: create a connection with the database (DB) SharedPower.db
    '''

    @staticmethod
    def CreateDBConnection(databaseFilename):
    
        databaseConnection = None
        functionName = 'CreateDBConnection'
        
        try:
            databaseConnection = sqlite3.connect(databaseFilename)
                
        except Error as e:
            print(__name__, ':', functionName, ":", e)
            raise

        return databaseConnection

    @staticmethod
    def cursor(databaseConnection):

        cursor = databaseConnection.cursor()

        return cursor

    # -------------------------------------------------
    # Close a sqlite database connection
    # -------------------------------------------------
    @staticmethod
    def CloseDBConnection(databaseConnection):

        functionName = 'CloseDBConnection'
        
        try:
            databaseConnection.close()        
                
        except Error as e:
            print(__name__, ':', functionName, ":", e)
            raise
            



    
