''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Notes.py

Created: 13th January 2020

-------------------------------------------------
'''

class Notes:

    def __init__(self, note_in, note_out):
        self.note_in = note_in
        self.note_out = note_out

    def Rent(self, tool_id):
        
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('SELECT count(*) FROM booking WHERE tool_id = ?', tool_id)
        numberOfBookings = cursor.fetchone()
        previousBooking = int(numberOfBookings) - 1
        if previousBooking == 0:
            printNoteStateOfItem = 'This tool was recently added please see item description'

        else:
        cursor.execute('SELECT note_in FROM booking WHERE tool_id = ? AND book_id = ?', tool_id, previousBooking)
        printNoteStateOfItem = cursor.fetchone()
                
        DatabaseConnection.CloseDBConnection()
        return printNoteStateOfItem
       

    def Return(self, noteOnReturn, bookingIdReturnInput):
        note_in = noteOnReturn
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('UPDATE booking SET note_in = ? WHERE booking_id = ?', noteOnReturn, bookingIdReturnInput)
        
        DatabaseConnection.CloseDBConnection()

