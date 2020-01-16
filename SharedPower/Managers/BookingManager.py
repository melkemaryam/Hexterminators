''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: BookingManager.py

Created: 3rd January 2020

-------------------------------------------------
'''

from datetime import datetime
from sqlite3 import Error

from GetterSetter.Bookings import Bookings
from GetterSetter.Tools import Tools
from GetterSetter.User import User     

from Managers.ToolManager import ToolManager

from Helpers.DatabaseConnection import DatabaseConnection

from CheckingFiles.LateCharge import LateCharge

class BookingManager:

    #Constructor
    def __init__(self, databaseFilename):

        self.databaseFilename = databaseFilename

    '''
    Function name: createBooking()
    Task: create a booking for a tool in the DB
    '''

    def createBooking(self, tool, user):

        functionName = 'createBooking'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            # get IDs
            tool_id = Tools.getId(self.databaseFilename)
            cust_id = User.getId(self.databaseFilename)

            cursor.execute('INSERT INTO Bookings (tool_id, cust_id) VALUES (?, ?)', (tool_id, cust_id,)) 

            databaseConnection.commit()

            book_id = cursor.lastrowid

            returnedBooking = Bookings(book_id, tool, user)
            
            # Diconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return returnedBooking

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: SearchFutureBookings
    Task: search for future bookings for the user
    '''

    def searchFutureBookings(self, user):

        functionName = 'SearchFutureBookings'

        # empty list
        RetBookingList = []
        
        try:

            toolManager = ToolManager(self.databaseFilename)
            start_date = datetime.now()

            # get ID
            cust_id = user.getId()

            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute("SELECT Bookings.book_id, Bookings.tool_id FROM Bookings INNER JOIN Tools ON Bookings.tool_id = Tools.tool_id WHERE Tools.tool_start > ? AND Bookings.cust_id = ?", (start_date, cust_id,))

            booking_rows = cursor.fetchall()

            # crete bookings in the DB
            for Booking in booking_rows:
                
                book_id = booking_rows[0]
                tool_id = booking_rows[1]

                # load the correct tool
                tool = toolManager.loadToolId(tool_id)

                # create booking
                singleBooking = Booking(book_id, tool, user)

                RetBookingList.append(singleBooking)
            
            # Disconnect from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

            return RetBookingList

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: markAvailability()
    Task: takes a tool of availability in the database
    '''

    def markAvailability(self, tool_id):

        functionName = 'markAvailability'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('UPDATE Bookings SET availability = 0 WHERE tool_id = ?', (tool_id,))

            databaseConnection.commit()

            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: bookOutNotes()
    Task: taskes a tool of availability in the database
    '''

    def bookOutNotes(self, book_id, brokenNoteInput):

        functionName = 'bookOutNotes'

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('UPDATE Bookings SET note_out = ? WHERE book_id = ?', (brokenNoteInput, book_id,))

            databaseConnection.commit()

            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise

    '''
    Function name: returnItem()
    Task: taskes a tool of availability in the database
    '''

    def returnItem(self, book_id):

        functionName = 'confirms the return and adds late charges if needed'

        late_charge = LateCharge.checkIfLate(self, book_id)

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
            cursor = databaseConnection.cursor()

            cursor.execute('UPDATE Bookings SET late_charge = ? WHERE book_id = ?', (late_charge, book_id,))

            databaseConnection.commit()

            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
