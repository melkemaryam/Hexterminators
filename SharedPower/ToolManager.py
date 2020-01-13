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

from UserManager import UserManager

from Tools import Tools
from Classes.toolcategory import toolcategory

from DatabaseConnection import DatabaseConnection


class ToolManager:

    # Constructor
    def __init__(self, databaseFilename):
        self.databaseFilename = databaseFilename

    '''
    Function name: loadToolId()
    Task: load a tool from the DB with the use of the tool ID
    '''
    def loadToolId(self, tool_id):

        functionName = 'loadToolId'
        
        # empty list
        returned_tool = None
        
        try:
            
            user_manager = UserManager(self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT cust_id, tool_id, tool_start, tool_name, tool_duration, tool_cat, price  FROM Tools WHERE tool_id = ?", (tool_id))

            tool_row = cursor.fetchone()

            if (tool_row != None):
           
                tool_id = tool_row[0]
                cust_id = tool_row[1]
                tool_name = tool_row[2]
                tool_start = datetime.strptime(tool_row[3], '%Y-%m-%d %H:%M:%S')
                tool_duration = tool_row[4]
                tool_cat = tool_row[5]
                price = tool_row[6]

                # get user ID
                user = user_manager.LoadUserId(cust_id)

                # create tool
                returned_tool = Tools(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Disconnection from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returned_tool

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: loadAllUsers()
    Task: search a tool in a DB by name
    '''
    def searchToolByName(self, search_criteria):

        functionName = 'searchToolByName'

        # empty list
        returnedToolList = []
        
        try:
            
            start_date = datetime.now()
            search_criteria = '%' + search_criteria + '%'

            user_manager = UserManager(self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start > ? AND tool_name LIKE ?", (start_date, search_criteria))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:
                
                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_start = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration = tool[4]
                tool_cat = tool[5]
                price = tool[6]

                # get user ID
                user = user_manager.LoadUserId(cust_id)

                # create tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returnedToolList.append(single_tool)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedToolList

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: searchToolByCategory()
    Task: search for a tool in the DB by category
    '''

    def searchToolByCategory(self, search_criteria):

        functionName = 'searchToolByCategory'

        # empty list
        returnedToolList = []
        
        try:

            # specify start date
            start_date = datetime.now()

            user_manager = UserManager(self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start > ? AND tool_cat = ?", (start_date, search_criteria.value))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:

                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_start = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration = tool[4]
                tool_cat = tool[5]
                price = tool[6]

                # get user
                user = user_manager.LoadUserId(cust_id)

                # create tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returnedToolList.append(single_tool)
            
            # Disconnection from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedToolList

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: loadAllUsers()
    Task: load all users from the DB
    '''

    def load_future_tools(self, range_start, range_end_days = 30):

        functionName = 'load_future_tools'

        # Create an empty list so that we can add tools to it later
        returned_tool_list = []
        
        try:
            
            # Calculate our range end by adding the number of days to the start date
            range_end = range_start + timedelta(days = range_end_days)  

            # We are going to be using the user manager soon so let's create it now
            user_manager = UserManager(self.databaseFilename)

            # Connect to our database
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)

            # Create a cursor so that we can run queries
            cursor = databaseConnection.cursor()

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
                user = user_manager.LoadUserId(cust_id)

                # We should now have a record with some data in it so let's create our tool
                single_tool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returned_tool_list.append(single_tool)
            
            # Close our database connection
            DatabaseConnection.CloseDBConnection(databaseConnection)

            # Return the tool list we just created
            return returned_tool_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', functionName, ':', e)
            raise

    # -----------------------------------------------------------
    # create_tool
    # Create a new tool in the database
    # -----------------------------------------------------------
    def create_tool(self, user, tool_name, tool_start, tool_duration, price, tool_cat):

        functionName = 'create_tool'

        try:
            
            # get ID
            cust_id = user.getId()

            # Connect to our database
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            # Execute our INSERT query against the database
            cursor.execute('INSERT INTO Tools (cust_id, tool_name, tool_start, tool_duration, tool_cat, price) VALUES (?, ?, ?, ?, ?, ?)', (cust_id, tool_name,
                                                                                                                                                                tool_start,
                                                                                                                                                                tool_duration,
                                                                                                                                                                tool_cat.value,
                                                                                                                                                                price))

            # Commit the changes
            databaseConnection.commit()

            # Let's get the id of the record we just created
            tool_id = cursor.lastrowid

            # Create a tool object based on the information we now have
            returned_tool = Tools(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Close our database connection
            DatabaseConnection.CloseDBConnection(databaseConnection)

            # Return the user we just created
            return returned_tool

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', functionName, ':', e)
            raise