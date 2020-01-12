''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: ToolManager.py

Created: 10th January 2020

-------------------------------------------------
'''

from datetime import datetime
from datetime import timedelta
from sqlite3 import Error

from Classes.Managers.UserManager import UserManager

from Classes.tool import tool
from Classes.toolType import toolType

from DatabaseConnection import DatabaseConnection


class ToolManager:

    # -----------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------
    def __init__(self, database_filename):

        # Store the filename of the database so that we can use it when we are connecting.
        self.__database_filename = database_filename

    # -----------------------------------------------------------
    # load_tool_from_id
    # Load an individual tool from it's ut
    # -----------------------------------------------------------
    def load_tool_from_id(self, tool_id):

        function_name = 'load_tool_from_id'

        # Create an empty list so that we can add tools to it later
        returned_tool = None
        
        try:
            
            # We are going to be using the user manager soon so let's create it now
            user_manager = UserManager(self.__database_filename)

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute("SELECT cust_id, tool_id, tool_start, tool_name, tool_duration, tool_cat, price  FROM Tools WHERE tool_id = ?", (tool_id,))

            tool_row = cursor.fetchone()

            # Check that we have actually got something back from the database. If our query returned no results then tool_row will equal None.
            if (tool_row != None):
           
                # Read our values from the record
                tool_id          = tool_row[0]
                cust_id          = tool_row[1]
                tool_name        = tool_row[2]
                tool_start       = datetime.strptime(tool_row[3], '%Y-%m-%d %H:%M:%S')
                tool_duration    = tool_row[4]
                tool_cat         = tool_row[5]
                price            = tool_row[6]

                # Now we can ask the user manager to give us the user with the id we just got from the database
                user = user_manager.load_user_from_id(cust_id)

                # We should now have a record with some data in it so let's create our tool
                returned_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the tool we just created
            return returned_tool

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # search_tools_by_name
    # Search for tools by their name
    # -----------------------------------------------------------
    def search_tool_by_name(self, search_criteria):

        function_name = 'search_tool_by_name'

        # Create an empty list so that we can add tools to it later
        returned_tool_list = []
        
        try:
            
            # We need to prepare our search criteria so that it can be used in SQL
            start_date = datetime.now()
            search_criteria = '%' + search_criteria + '%'

            # We are going to be using the user manager soon so let's create it now
            user_manager = UserManager(self.__database_filename)

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start > ? AND tool_name LIKE ?", (start_date, search_criteria))

            tool_rows = cursor.fetchall()

            # Iterate through the database records, creating a tool object and adding it to our list as we go
            for tool in tool_rows:
                
                # Read our values from the record
                tool_id          = tool[0]
                cust_id          = tool[1]
                tool_name        = tool[2]
                tool_start       = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration    = tool[4]
                tool_cat         = tool[5]
                price            = tool[6]

                # Now we can ask the user manager to give us the user with the id we just got from the database
                user = user_manager.load_user_from_id(cust_id)

                # We should now have a record with some data in it so let's create our tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returned_tool_list.append(single_tool)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the tool list we just created
            return returned_tool_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # search_tools_by_type
    # Search for tools by their type
    # -----------------------------------------------------------
    def search_tools_by_type(self, search_criteria):

        function_name = 'search_tools_by_type'

        # Create an empty list so that we can add tools to it later
        returned_tool_list = []
        
        try:

            # We only want tools from now - so we specify the start date and include this in our SQL query
            start_date = datetime.now()

            # We are going to be using the user manager soon so let's create it now
            user_manager = UserManager(self.__database_filename)

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start > ? AND tool_cat = ?", (start_date, search_criteria.value))

            tool_rows = cursor.fetchall()

            # Iterate through the database records, creating a tool object and adding it to our list as we go
            for tool in tool_rows:
                
                # Read our values from the record
                tool_id          = tool[0]
                cust_id          = tool[1]
                tool_name        = tool[2]
                tool_start       = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration    = tool[4]
                tool_cat         = tool[5]
                price            = tool[6]

                # Now we can ask the user manager to give us the user with the id we just got from the database
                user = user_manager.load_user_from_id(cust_id)

                # We should now have a record with some data in it so let's create our tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returned_tool_list.append(single_tool)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the tool list we just created
            return returned_tool_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # load_future_tools
    # Load future tools from the database based upon a start date and range
    # -----------------------------------------------------------
    def load_future_tools(self, range_start, range_end_days = 30):

        function_name = 'load_future_tools'

        # Create an empty list so that we can add tools to it later
        returned_tool_list = []
        
        try:
            
            # Calculate our range end by adding the number of days to the start date
            range_end = range_start + timedelta(days = range_end_days)  

            # We are going to be using the user manager soon so let's create it now
            user_manager = UserManager(self.__database_filename)

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start BETWEEN ? AND ?", (range_start, range_end))

            tool_rows = cursor.fetchall()

            # Iterate through the database records, creating a tool object and adding it to our list as we go
            for tool in tool_rows:
                
                # Read our values from the record
                tool_id          = tool[0]
                cust_id          = tool[1]
                tool_name        = tool[2]
                tool_start       = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration    = tool[4]
                tool_cat         = tool[5]
                price            = tool[6]

                # Now we can ask the user manager to give us the user with the id we just got from the database
                user = user_manager.load_user_from_id(cust_id)

                # We should now have a record with some data in it so let's create our tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returned_tool_list.append(single_tool)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the tool list we just created
            return returned_tool_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # create_tool
    # Create a new tool in the database
    # -----------------------------------------------------------
    def create_tool(self, user, tool_name, tool_start, tool_duration, price, tool_cat):

        function_name = 'create_tool'

        try:
            
            # Grab the user_id from the incoming user object so that we can store it in the database
            cust_id = user.getId()

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            # Execute our INSERT query against the database
            cursor.execute('INSERT INTO Tools (cust_id, tool_name, tool_start, tool_duration, tool_cat, price) VALUES (?, ?, ?, ?, ?, ?)', (cust_id,
                                                                                                                                                                tool_name,
                                                                                                                                                                tool_start,
                                                                                                                                                                tool_duration,
                                                                                                                                                                tool_cat.value,
                                                                                                                                                                price))

            # Commit the changes
            database_connection.commit()

            # Let's get the id of the record we just created
            tool_id = cursor.lastrowid

            # Create a tool object based on the information we now have
            returned_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the user we just created
            return returned_tool

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise