''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Bookings.py

Created: 10th January 2020

-------------------------------------------------
'''

class Bookings:

    #Constructor
    def __init__(self, book_id, tool, user):

        self.book_id = book_id
        self.tool = tool
        self.user = user

        
    '''
    Function name: getBookingId()
    Task: returns the value of the booking ID
    '''
    def getBookingId(self):
        return self.book_id

    '''
    Function name: getTool()
    Task: returns the tool
    '''
    def getTool(self):
        return self.tool

    '''
    Function name: getUser()
    Task: returns the user
    '''
    def getUser(self):
        return self.user

    # __str__ function
    def __str__(self):

        returnValue = '{id} \t {tool} \t {username}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getUsername())

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = '{id} \t {tool} \t {username}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getUsername())

        return returnValue

class BookingInfo:

    #Constructor
    def __init__(self, start_date, end_date, duration, delivery, note_in, note_out, late_return):
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        self.delivery = delivery
        self.note_in = note_in
        self.note_out = note_out
        self.late_return = late_return

    '''
    Function name: setStartDate()
    Task: sets the start date of the booking of the tool
    '''
    def setStartDate(self, newStart):
        self.start_date = newStart

    '''
    Function name: getStartDate()
    Task: returns the vaule of the start date of the booking of the tool
    '''
    def getStartDate(self):
        return self.start_date

    '''
    Function name: setEndDate()
    Task: sets the end date of the booking of the tool
    '''
    def setEndDate(self, newEndDate):
        self.end_date = newEndDate

    '''
    Function name: getEndDate()
    Task: returns the value of the end date of the booking of the tool
    '''
    def getEndDate(self):        
        return self.end_date

    '''
    Function name: setDuration()
    Task: sets the duration of the booking of the tool
    '''
    def setDuration(self, newDuration):
        self.duration = newDuration

    '''
    Function name: getDuration()
    Task: returns the value of the duration of the booking of the tool
    '''
    def getDuration(self):        
        return self.duration

    '''
    Function name: setDelivery()
    Task: sets the value for the delivery of a tool
    '''
    def setDelivery(self, newDelivery):
        self.delivery = newDelivery

    '''
    Function name: getDelivery()
    Task: returns the value of the delivery of a tool
    '''
    def getDelivery(self):
        return self.delivery

    '''
    Function name: setNoteIn()
    Task: sets the note_in of a tool
    '''
    def setNoteIn(self, newNoteIn):
        self.note_in = newNoteIn

    '''
    Function name: getNoteIn()
    Task: returns the note_in of a tool
    '''
    def getNoteIn(self):
        return self.note_in

    '''
    Function name: setNoteOut()
    Task: sets the note_out of a tool
    '''
    def setNoteOut(self, newNoteOut):
        self.note_out = newNoteOut

    '''
    Function name: getNoteOut()
    Task: returns the note_out of a tool
    '''
    def getNoteOut(self):
        return self.note_out

    '''
    Function name: setLateReturn()
    Task: sets the value for a late return of a tool
    '''
    def setLateReturn(self, newLateReturn):
        self.late_return = newLateReturn

    '''
    Function name: getLateReturn()
    Task: returns the value of the late return of a tool
    '''
    def getLateReturn(self):
        return self.late_return

    # __str__ function
    def __str__(self):

        returnValue = '{start date} \t {end date} \t {duration} \t {delivery} \t {note in} \t {note out} \t {late return}'.format(start_date = self.start_date, 
                                                                                                                                    end_date = self.end_date, 
                                                                                                                                    duration = self.duration, 
                                                                                                                                    delivery = self.delivery, 
                                                                                                                                    note_in = self.note_in,
                                                                                                                                    note_out = self.note_out,
                                                                                                                                    late_return = self.late_return)

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = '{start date} \t {end date} \t {duration} \t {delivery} \t {note in} \t {note out} \t {late return}'.format(start_date = self.start_date, 
                                                                                                                                    end_date = self.end_date, 
                                                                                                                                    duration = self.duration, 
                                                                                                                                    delivery = self.delivery, 
                                                                                                                                    note_in = self.note_in,
                                                                                                                                    note_out = self.note_out,
                                                                                                                                    late_return = self.late_return)

        return returnValue


