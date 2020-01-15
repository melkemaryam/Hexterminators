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
    def __init__(self, tool_id, user, tool_name, tool_cat, price, halfDayPrice, tool_desc):

        self.tool_id = tool_id
        self.tool_user = user
        self.tool_name = tool_name
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

        returnValue = '{id} \t {name} \t {user} \t {category} \t \t {price} \t {halfDayPrice} \t {tool_desc}'.format(id = self.tool_id, 
                                                                                                           name = self.tool_name,
                                                                                                           user = self.tool_user.getFirstName() + ' ' + self.tool_user.getLastName(),
                                                                                                           category = self.tool_cat,
                                                                                                           price = self.price,
                                                                                                           halfDayPrice = self.halfDayPrice,
                                                                                                           tool_desc = self.tool_desc)

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = '{id} \t {name} \t {user} \t {category} \t \t {price} \t {halfDayPrice} \t {tool_desc}'.format(id = self.tool_id, 
                                                                                                           name = self.tool_name,
                                                                                                           user = self.tool_user.getFirstName() + ' ' + self.tool_user.getLastName(),
                                                                                                           category = self.tool_cat,
                                                                                                           price = self.price,
                                                                                                           halfDayPrice = self.halfDayPrice,
                                                                                                           tool_desc = self.tool_desc)

        return returnValue
