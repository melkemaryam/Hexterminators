''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Tools.py

Created: 10th January 2020

-------------------------------------------------
'''

from datetime import datetime
from datetime import timedelta

#from Classes.Helpers.StringHelpers import StringHelpers

class Tools:

    #Constructor
    def __init__(self, tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price, halfDayPrice, tool_desc):

        self.tool_id = tool_id
        self.tool_user = user
        self.tool_name = tool_name
        self.tool_start = tool_start
        self.tool_duration = tool_duration
        self.tool_end = self.tool_start + timedelta(days = self.tool_duration)
        self.tool_cat = tool_cat
        self.price = price
        self.halfDayPrice = halfDayPrice
        self.tool_desc = tool_desc
        
    '''
    Function name: getId()
    Task: returns the value for the ID
    '''
    def getId(self):
        return self.tool_id

    '''
    Function name: getUser()
    Task: returns the value for the user of the tool
    '''
    def getUser(self):
        return self.tool_user

    '''
    Function name: setName()
    Task: sets the name of the tool
    '''
    def setName(self, newName):
        self.tool_name = newName

    '''
    Function name: getName()
    Task: returns the value of the name of the tool
    '''
    def getName(self):
        return self.tool_name

    '''
    Function name: setStartDate()
    Task: sets the start date of the booking of the tool
    '''
    def setStartDate(self, newStart):
        self.tool_start = newStart

    '''
    Function name: getStartDate()
    Task: returns the vaule of the start date of the booking of the tool
    '''
    def getStart(self):
        return self.tool_start

    '''
    Function name: setDuration()
    Task: sets the duration of a booking of a tool
    '''
    def setDuration(self, newDuration):
        self.tool_duration = newDuration

    '''
    Function name: getDuration()
    Task: returns the value of the duration of the booking of a tool
    '''
    def getDuration(self):
        return self.tool_duration

    '''
    Function name: getEndDate()
    Task: returns the value of the end date of the booking of the tool
    '''
    def getEndDate(self):        
        return self.tool_end

    '''
    Function name: setPrice()
    Task: sets the day price for the tool
    '''
    def setPrice(self, newPrice):
        self.price = newPrice

    '''
    Function name: getPrice()
    Task: returns the value of the day price
    '''
    def getPrice(self):
        return self.price

    '''
    Function name: setHDPrice()
    Task: sets the day price for the tool
    '''
    def setHDPrice(self, newHalfDayPrice):
        self.halfDayPrice = newHalfDayPrice

    '''
    Function name: getHDPrice()
    Task: returns the value of the day price
    '''
    def getHDPrice(self):
        return self.halfDayPrice

    '''
    Function name: setDescription()
    Task: sets the description of the tool
    '''
    def setDescription(self, newDescription):
        self.tool_desc = newDescription

    '''
    Function name: getDescription()
    Task: returns the description
    '''
    def getDescription(self):
        return self.tool_desc

    '''
    Function name: getCategory()
    Task: returns the value for the category of the tool
    '''
    def getCategory(self):
        return self.tool_cat

    # __str__ function
    def __str__(self):

        returnValue = '{id} \t {name} \t {user} \t \t {start} \t {end} \t {duration} \t \t {category}'.format(id = self.tool_id, 
                                                                                                           name = StringHelpers.PadString(self.tool_name, 30),
                                                                                                           user = self.tool_user.getFirstName() + ' ' + self.tool_user.getLastName(),
                                                                                                           start = self.tool_start,
                                                                                                           end = self.tool_end,
                                                                                                           duration = self.tool_duration,
                                                                                                           category = self.tool_cat)

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = '{id} \t {name} \t {user} \t \t {start} \t {end} \t {duration} \t \t {category}'.format(id = self.tool_id, 
                                                                                                           name = StringHelpers.PadString(self.tool_name, 30),
                                                                                                           user = self.tool_user.getFirstName() + ' ' + self.tool_user.getLastName(),
                                                                                                           start = self.tool_start,
                                                                                                           end = self.tool_end,
                                                                                                           duration = self.tool_duration,
                                                                                                           category = self.tool_cat)

        return returnValue
