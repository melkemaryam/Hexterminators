# --------------------------------------------------------------------
# Filename:     UserManager.py
#
# Date Created: 28th November 2019
# --------------------------------------------------------------------

from DatabaseConnection import DatabaseConnection
from Classes.Helpers.PasswordHelpers import PasswordHelpers
from Classes.User import User
from Classes.UserType import UserType
from sqlite3 import Error

class UserManager:

    # -----------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------
    def __init__(self, database_filename):

        # Store the filename of the database so that we can use it when we are connecting.
        self.__database_filename = database_filename
        
    # -----------------------------------------------------------
    # load_user_from_id
    # Load the user from the database using the user id
    # -----------------------------------------------------------
    def load_user_from_id(self, cust_id):

        function_name = 'load_user_from_id'
        returned_user = None
        
        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer WHERE cust_id = ?', (cust_id,))

            user_row = cursor.fetchone()

            # Check that we have actually got something back from the database. If our query returned no results then user_row will equal None.
            if (user_row != None):
           
                # Read our values from the record
                cust_id         = user_row[0]
                F_name          = user_row[1]
                L_name          = user_row[2]
                email           = user_row[3]

                # We should now have a record with some data in it so let's create our user
                returned_user = User(cust_id, F_name, L_name, email)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user we just created
            return returned_user

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # load_user_from_email
    # Load the user from the database using the user email
    # -----------------------------------------------------------
    def load_user_from_email(self, email):

        function_name = 'load_user_from_email'
        returned_user = None
        
        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer WHERE email = ?', (email))

            user_row = cursor.fetchone()

            # Check that we have actually got something back from the database. If our query returned no results then user_row will equal None
            if (user_row != None):
            
                # Read our values from the record
                cust_id         = user_row[0]
                F_name          = user_row[1]
                L_name          = user_row[2]
                email           = user_row[3]

                # We should now have a record with some data in it so let's create our user
                returned_user = User(cust_id, F_name, L_name, email)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user we just created
            return returned_user

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # validate_user
    # Load a user using their email and validate their password
    # -----------------------------------------------------------
    def validate_user(self, email, supplied_password):

        function_name = 'validate_user'
        returned_user = None
        
        try:

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email, password FROM Customer WHERE email = ?', (email.lower(),))

            user_row = cursor.fetchone()

            # Check that we have actually got something back from the database. If our query returned no results then user_row will equal None
            if (user_row != None):
            
                # Read our values from the record
                cust_id         = user_row[0]
                F_name          = user_row[1]
                L_name          = user_row[2]
                email           = user_row[3]
                password        = user_row[4]

                # We have our details from the database now.  Before we create a user object, let's check the password
                password_valid = PasswordHelpers.VerifyPassword(password, supplied_password)

                # If the password was valid then create our object
                if (password_valid == True):
                    returned_user = User(cust_id, F_name, L_name, email)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user we just created
            return returned_user

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # load_all_users
    # Load all users from the database
    # -----------------------------------------------------------
    def load_all_users(self):

        function_name = 'load_all_users'

        # Create an empty list so that we can add users to it later
        returned_user_list = []
        
        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute('SELECT cust_id, F_name, L_name, email FROM Customer')

            user_rows = cursor.fetchall()

            # Iterate through the database records, creating a user object and adding it to our list as we go
            for user in user_rows:
                
                # Read our values from the record
                cust_id         = user[0]
                F_name          = user[1]
                L_name          = user[2]
                email           = user[3]

                # We should now have a record with some data in it so let's create our user
                single_user = User(cust_id, F_name, L_name, email)

                returned_user_list.append(single_user)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user list we just created
            return returned_user_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise
        
    # -----------------------------------------------------------
    # create_user
    # Create a new user in the database
    # -----------------------------------------------------------
    def create_user(self, F_name, L_name, email, password):

        function_name = 'create_user'

        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            # Hash the users password
            password = PasswordHelpers.HashPassword(password)
            
            # Execute our INSERT query against the database
            cursor.execute('INSERT INTO Customer (F_name, L_name, email, password) VALUES (?, ?, ?, ?, ?)', (F_name,
                                                                                                                                           L_name,
                                                                                                                                           email.lower(),
                                                                                                                                           password))

            # Commit the changes
            database_connection.commit()

            # Let's get the id of the record we just created
            cust_id = cursor.lastrowid

            # Create a user object based on the information we now have
            returned_user = User(cust_id, F_name, L_name, email)

            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user we just created
            return returned_user

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # update_user
    # Update an existing user in the database
    # -----------------------------------------------------------
    def update_user(self, user):

        function_name = 'update_user'

        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            # Execute our UPDATE query against the database
            cursor.execute('UPDATE Customer SET F_name = ?, L_name = ?, email = ? WHERE cust_id = ?', (user.getForename(),
                                                                                                                                    user.getSurname(),
                                                                                                                                    user.getEmail(),
                                                                                                                                    user.getId()))

            # Commit the changes
            database_connection.commit()
           
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise
                       
    # -----------------------------------------------------------
    # delete_user
    # Delete an existing user from the database
    # -----------------------------------------------------------
    def delete_user(self, cust_id):

        function_name = 'delete_user'

        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            # Execute our UPDATE query against the database
            cursor.execute('DELETE FROM Customer WHERE cust_id = ?', (cust_id))

            # Commit the changes
            database_connection.commit()
           
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise
