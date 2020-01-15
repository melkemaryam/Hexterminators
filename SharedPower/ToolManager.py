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
from ToolCategory import ToolCategory

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
        returnedTool = None
        
        try:
            
            userManager = UserManager(self.databaseFilename)

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
                user = userManager.LoadUserId(cust_id)

                # create tool
                returnedTool = Tools(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedTool

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: loadToolName()
    Task: load a tool from the DB with the use of the tool name
    '''
    def loadToolName(self, tool_name):

        functionName = 'loadToolName'
        
        # empty list
        returnedTool = None
        
        try:
            
            userManager = UserManager(self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT cust_id, tool_id, tool_start, tool_name, tool_duration, tool_cat, price  FROM Tools WHERE tool_name = ?", (tool_name))

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
                user = userManager.LoadUserId(cust_id)

                # create tool
                returnedTool = Tools(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedTool

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise


    '''
    Function name: searchToolByName()
    Task: search a tool in a DB by name
    '''
    def searchToolByName(self, search_criteria):

        functionName = 'searchToolByName'

        # empty list
        returnedToolList = []
        
        try:
            
            start_date = datetime.now()
            search_criteria = '%' + search_criteria + '%'

            userManager = UserManager(self.databaseFilename)

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
                user = userManager.LoadUserId(cust_id)

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

            userManager = UserManager(self.databaseFilename)

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
                user = userManager.LoadUserId(cust_id)

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
    Function name: loadFutureTools()
    Task: load all the tools that are booked for the future
    '''

    def loadFutureTools(self, range_start, range_end_days = 42):

        functionName = 'loadFutureTools'

        # empty list
        returnedToolList = []
        
        try:
            
            # calculationg range_end
            range_end = range_start + timedelta(days = range_end_days)  

            userManager = UserManager(self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_start, tool_duration, tool_cat, price FROM Tools WHERE tool_start BETWEEN ? AND ?", (range_start, range_end))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:
                
                # Read our values from the record
                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_start = datetime.strptime(tool[3], '%Y-%m-%d %H:%M:%S')
                tool_duration = tool[4]
                tool_cat = tool[5]
                price = tool[6]

                # get ID
                user = userManager.LoadUserId(cust_id)

                # create tool
                singleTool = tool(tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price)

                returnedToolList.append(singleTool)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedToolList

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: createTool()
    Task: create a new tool in the database
    '''

    def createTool(self, user, tool_name, tool_cat, tool_desc, price, halfDayPrice):

        functionName = 'createTool'

        try:
            
            # get ID
            cust_id = user.getId()

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('INSERT INTO Tools (cust_id, tool_name, tool_cat, tool_desc, price, half_price) VALUES (?, ?, ?, ?, ?, ?)', (cust_id, tool_name, tool_cat.value, tool_desc, price, halfDayPrice))

            databaseConnection.commit()

            # get ID
            tool_id = cursor.lastrowid

            # create tool object
            returnedTool = Tools(tool_id, user, tool_name, tool_cat, tool_desc, self.price, self.halfDayPrice)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedTool

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise