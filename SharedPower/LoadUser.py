''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: LoadUser.py

Created: 17th January 2020

-------------------------------------------------
'''

from sqlite3 import Error
from DatabaseConnection import DatabaseConnection
from User import User

class LoadUser:
    
    @staticmethod
    def LoadUser (databasefilename, criteria, value):

        functionName = LoadUser

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(databasefilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email, username FROM Customers WHERE ? = ?', (criteria, value))

            user_row = cursor.fetchone()

            if (user_row != None):
                cust_id = user_row[0]
                F_name = user_row[1]
                L_name = user_row[2]
                email = user_row[3]
                username = user_row[4]

                # create user
                returnedUser = User(cust_id, F_name, L_name, email, username)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

