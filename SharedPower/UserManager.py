''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: UserManager.py

Created: 10th January 2020

-------------------------------------------------
'''

from DatabaseConnection import DatabaseConnection
from NewPassword import PasswordHelpers
from User import User
from sqlite3 import Error
from LoadUser import LoadUser



class UserManager:

    #Constructor
    def __init__(self, databaseFilename):

        self.databaseFilename = databaseFilename


    '''
    Function name: createUser()
    Task: create a new user in the DB
    '''

    def createUser(self, username, password, F_name, L_name, tel_no, email, address1, address2, postcode, acc_no, sort_code, branch_name):

        functionName = 'createUser'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            # Hash the users password
            password = PasswordHelpers.Hash(password)
            
            cursor.execute('INSERT INTO Customers (username, password, F_name, L_name, tel_no, email, address1, address2, postcode, acc_no, sort_code, branch_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (username, password, F_name, L_name, tel_no, email.lower(), address1, address2, postcode, acc_no, sort_code, branch_name,))

            databaseConnection.commit()

            # get ID
            cust_id = cursor.lastrowid

            # create user
            returnedUser = User(cust_id, F_name, L_name, tel_no, email)

            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise


    '''
    Function name: cornfirmUser()
    Task: validate the password of the user
    '''

    def confirmUser(self, username, supplied_password):

        functionName = 'confirmUser'
        returnedUser = None
        
        try:

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, username, email, password FROM Customers WHERE username = ?', (username,))

            user_row = cursor.fetchone()

            if (user_row != None):
                cust_id = user_row[0]
                F_name = user_row[1]
                L_name = user_row[2]
                username = user_row[3]
                email = user_row[4]
                password = user_row[5]

                # check password
                password_valid = PasswordHelpers.Verify(password, supplied_password)

                # create object
                if (password_valid == True):
                    returnedUser = User(cust_id, F_name, L_name, email, username)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUser

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
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('UPDATE Customers SET F_name = ?, L_name = ?, email = ? WHERE cust_id = ?', (user.getFirstName(), user.getLastName(), user.getEmail(), user.getId(),))

            databaseConnection.commit()
           
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
                       
    '''
    Function name: deleteUser()
    Task: Delete an existing user from the DB
    '''
    
    def deleteUser(self, cust_id):

        functionName = 'deleteUser'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('DELETE FROM Customers WHERE cust_id = ?', (cust_id,))

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

        #functionName = 'LoadUserId'

        returnedUser = LoadUser.LoadUser(self.databaseFilename, 'cust_id', cust_id)

        return returnedUser
        
        #try:
            
            # Connecting to the DB
            #databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            #cursor = databaseConnection.cursor()

            #cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customers WHERE cust_id = ?', (cust_id))

            #user_row = cursor.fetchone()

            #if (user_row != None):
                #cust_id = user_row[0]
                #F_name = user_row[1]
               # L_name = user_row[2]
                #email = user_row[3]

                # create user
                #returnedUser = User(cust_id, F_name, L_name, email)
            
            # Disconnecting from the DB
            #DatabaseConnection.CloseDBConnection(databaseConnection)

            #return returnedUser

        #except Error as e:

            #print(__name__, ':', functionName, ':', e)
            #raise

    '''
    Function name: loadUserEmail()
    Task: load the user from the DB with the use of the email address
    '''

    def loadUserEmail(self, email):

        #functionName = 'LoadUserEmail'
        #returnedUser = None
        
        returnedUser = LoadUser.LoadUser(self.databaseFilename, 'email', email)

        return returnedUser
        
        
        #try:
            
            # Connecting to the DB
            #databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            #cursor = databaseConnection.cursor()

            #cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customers WHERE email = ?', (email))

            #user_row = cursor.fetchone()

            #if (user_row != None):
                #cust_id = user_row[0]
                #F_name = user_row[1]
                #L_name = user_row[2]
                #email = user_row[3]

                # create user
                #returnedUser = User(cust_id, F_name, L_name, email)
            
            # Disconnecting from the DB
            #DatabaseConnection.CloseDBConnection(databaseConnection)

            #return returnedUser

        #except Error as e:

            #print(__name__, ':', functionName, ':', e)
            #raise

    
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

            cursor.execute('SELECT cust_id, F_name, L_name, email, username FROM Customers')

            user_rows = cursor.fetchall()

            for user in user_rows:
               
                cust_id = user[0]
                F_name = user[1]
                L_name = user[2]
                email = user[3]
                username = user[4]

                # create user
                singleUser = User(cust_id, F_name, L_name, email, username)

                returnedUserList.append(singleUser)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedUserList

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
