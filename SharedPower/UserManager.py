''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: UserManager.py

Created: 10th January 2020

-------------------------------------------------
'''

from DatabaseConnection import DatabaseConnection
from Classes.Helpers.PasswordHelpers import PasswordHelpers
from User import User
from sqlite3 import Error

class UserManager:

    #Constructor
    def __init__(self, databaseFilename):

        self.databaseFilename = databaseFilename


    '''
    Function name: createUser()
    Task: create a new user in the DB
    '''

    def createUser(self, F_name, L_name, email, password):

        functionName = 'createUser'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.__databaseFilename)
            cursor = databaseConnection.cursor()

            # Hash the users password
            password = PasswordHelpers.HashPassword(password)
            
            cursor.execute('INSERT INTO Customer (F_name, L_name, email, password) VALUES (?, ?, ?, ?, ?)', (F_name, L_name, email.lower(), password))

            databaseConnection.commit()

            # get ID
            cust_id = cursor.lastrowid

            # create user
            returnedUser = User(cust_id, F_name, L_name, email)

            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise


    '''
    Function name: validateUser()
    Task: validate the password of the user
    '''

    def validateUser(self, email, supplied_password):

        functionName = 'validateUser'
        returned_user = None
        
        try:

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email, password FROM Customer WHERE email = ?', (email.lower()))

            user_row = cursor.fetchone()

            if (user_row != None):
                cust_id = user_row[0]
                F_name = user_row[1]
                L_name = user_row[2]
                email = user_row[3]
                password = user_row[4]

                # check password
                password_valid = PasswordHelpers.VerifyPassword(password, supplied_password)

                # create object
                if (password_valid == True):
                    returned_user = User(cust_id, F_name, L_name, email)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returned_user

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: updateUser()
    Task: update the information of an existing user in the DB
    '''

    def updateUser(self, user):

        functionName = 'updateUser'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.__databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('UPDATE Customer SET F_name = ?, L_name = ?, email = ? WHERE cust_id = ?', (user.getFirstName(), user.getLastName(), user.getEmail(), user.getId()))

            databaseConnection.commit()
           
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
                       
    '''
    Function name: deleteUser
    Task: Delete an existing user from the DB
    '''
    
    def deleteUser(self, cust_id):

        functionName = 'deleteUser'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('DELETE FROM Customer WHERE cust_id = ?', (cust_id))

            databaseConnection.commit()
           
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise



    '''
    Function name: LoadUserId()
    Task: load the user from the DB with the use of the user ID
    '''

    def LoadUserId(self, cust_id):

        functionName = 'LoadUserId'
        returnedUser = None
        
        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer WHERE cust_id = ?', (cust_id,))

            user_row = cursor.fetchone()

            if (user_row != None):
                cust_id = user_row[0]
                F_name = user_row[1]
                L_name = user_row[2]
                email = user_row[3]

                # create user
                returnedUser = User(cust_id, F_name, L_name, email)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: loadUserEmail()
    Task: create a booking for a tool in the DB
    '''

    def loadUserEmail(self, email):

        functionName = 'LoadUserEmail'
        returnedUser = None
        
        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer WHERE email = ?', (email))

            user_row = cursor.fetchone()

            if (user_row != None):
                cust_id = user_row[0]
                F_name = user_row[1]
                L_name = user_row[2]
                email = user_row[3]

                # create user
                returnedUser = User(cust_id, F_name, L_name, email)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    
    '''
    Function name: loadAllUsers()
    Task: load all users from the DB
    '''

    def loadAllUsers(self):

        functionName = 'loadAllUsers'

        # empty list
        returnedUserList = []
        
        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer')

            user_rows = cursor.fetchall()

            for user in user_rows:
               
                cust_id = user[0]
                F_name = user[1]
                L_name = user[2]
                email = user[3]

                # create user
                single_user = User(cust_id, F_name, L_name, email)

                returnedUserList.append(single_user)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUserList

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
