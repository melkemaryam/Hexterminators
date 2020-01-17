''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: ToolManager.py

Created: 3rd January 2020

-------------------------------------------------
'''

from datetime import datetime
from datetime import timedelta
from sqlite3 import Error

from UserManager import UserManager

from User import User
from Tools import Tools

from ToolCategory import ToolCategory
from DatabaseConnection import DatabaseConnection

from AvailabilityChecker import AvailabilityChecker


class ToolManager:

    # Constructor
    def __init__(self, registeredUser, databaseFilename):
        self.databaseFilename = databaseFilename
        self.registeredUser = registeredUser

    '''
    Function name: loadToolId()
    Task: load a tool from the DB with the use of the tool ID
    '''

    def loadToolId(self, tool_id):

        functionName = 'loadToolId'
        
        # empty list
        returnedTool = None
        
        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection('SharedPower.db')
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT cust_id, tool_id, tool_name, tool_desc, tool_cat, price, half_price  FROM Tools WHERE tool_id = ?", (tool_id))

            tool_row = cursor.fetchone()

            if (tool_row != None):
           
                tool_id = tool_row[1]
                cust_id = tool_row[0]
                tool_name = tool_row[2]
                tool_desc = tool_row[3]
                tool_cat = tool_row[4]
                price = tool_row[5]
                halfDayPrice = tool_row[6]

                # create tool
                returnedTool = Tools(tool_id, cust_id, tool_name, tool_desc, tool_cat, price, halfDayPrice)
            
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
           
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT cust_id, tool_id, tool_name, tool_desc, tool_cat, price, half_price  FROM Tools WHERE tool_name = ?", (tool_name))

            tool_row = cursor.fetchone()

            if (tool_row != None):
           
                tool_id = tool_row[1]
                cust_id = tool_row[0]
                tool_name = tool_row[2]
                tool_desc = tool_row[3]
                tool_cat = tool_row[4]
                price = tool_row[5]
                halfDayPrice = tool_row[6]

                # create tool
                returnedTool = Tools(tool_id, cust_id, tool_name, tool_desc, tool_cat, price, halfDayPrice)
            
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
    def searchToolByName(self, tool_name):

        functionName = 'searchToolByName'

        # empty list
        returnedToolList = []
        
        try:
           
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_cat, price FROM Tools WHERE tool_name LIKE ?", ( tool_name))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:
                
                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_cat = tool[3]
                price = tool[4]

                # create tool
                single_tool = tool(tool_id, cust_id, tool_name, tool_cat, price)

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

            userManager = UserManager(self.registeredUser, self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, cust_id, tool_name, tool_cat, price, tool_desc, half_price FROM Tools WHERE tool_cat = ?", (search_criteria))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:

                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_cat = tool[3]
                price = tool[4]
                tool_desc = tool[5]
                half_price = tool[6]

                # get user
                user = userManager.LoadUserId(cust_id)

                # create tool
                single_tool = Tools(tool_id, user, tool_name, tool_cat, price, tool_desc, half_price)

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

            userManager = UserManager(self.registeredUser, self.databaseFilename)

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT tool_id, duration FROM Bookings WHERE start_date BETWEEN ? AND ?", (range_start, range_end))

            tool_rows = cursor.fetchall()

            for tool in tool_rows:
                
                # Read our values from the record
                tool_id = tool[0]
                cust_id = tool[1]
                tool_name = tool[2]
                tool_cat = tool[3]
                tool_desc = tool[4]
                price = tool[5]
                halfDayPrice = tool[6]

                # get ID
                user = userManager.LoadUserId(cust_id)

                # create tool
                singleTool = Tools(tool_id, user, tool_name, tool_cat, tool_desc, price, halfDayPrice)

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
            cust_id = #'1'
            tool_id = #'33'

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('INSERT INTO Tools (tool_id, cust_id, tool_name, tool_cat, tool_desc, price, half_price) VALUES (?, ?, ?, ?, ?, ?, ?)', (tool_id, cust_id, tool_name, tool_cat, tool_desc, price, halfDayPrice))

            databaseConnection.commit()

            # create tool object
            returnedTool = Tools(tool_id, user, tool_name, tool_cat, tool_desc, price, halfDayPrice)
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            AvailabilityChecker.get_availability(cust_id, tool_id, int(0))

            return returnedTool

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise