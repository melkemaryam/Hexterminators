''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Notes.py

Created: 13th January 2020

-------------------------------------------------
'''

from datetime import datetime
import sqlite3
from DatabaseConnection import DatabaseConnection

class Notes:

    def __init__(self, note_in, note_out, databaseFilename):
        self.note_in = note_in
        self.note_out = note_out
        self.databaseFilename = databaseFilename

    def Rent(self, tool_id, descriptionToolInput):
        
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('SELECT book_id FROM booking WHERE tool_id = ?', tool_id)
        numberOfBookings = cursor.fetchone()
        previousBooking = int(numberOfBookings) - 1
        if previousBooking >= 0:
            printNoteStateOfItem = ('This tool was recently added please see item description:\n' + descriptionToolInput)

        else:
            cursor.execute('SELECT note_in FROM booking WHERE tool_id = ? AND book_id = ?', tool_id, previousBooking)
            printNoteStateOfItem = cursor.fetchone()
                
        DatabaseConnection.CloseDBConnection()
        return printNoteStateOfItem
       

    def Return(self, noteOnReturn, bookingIdReturnInput):
        
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('UPDATE booking SET note_in = ? WHERE booking_id = ?', noteOnReturn, bookingIdReturnInput)
        
        DatabaseConnection.CloseDBConnection()

    def Broken (self, maToolInput, brokenNoteInput):

        today = datetime.date.today()

        DatabaseConnection.CreateDBConnection()

        cursor.execute('SELECT tool_id FROM booking WHERE book_id = ?', maToolInput)
        tool_id = cursor.fetchone()

        cursor.execute('UPDATE booking SET note_out = ? AND available = 0 WHERE tool_id = ? AND date >= ?', brokenNoteInput, tool_id, today)

        DatabaseConnection.CloseDBConnection()


