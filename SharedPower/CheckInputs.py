''' 
-------------------------------------------------
Project: SharedPower
Group: Hexterminators
File name: CheckInputs.py
Created: 14th January 2020
-------------------------------------------------
'''

import re
from sqlite3 import Error

from User import User 
from DatabaseConnection import DatabaseConnection
from LoadUser import LoadUser

class CheckInputs:

    '''
    Function name: mainmenu()
    Task: validates the input for the menu
    '''

    def mainmenu (self, haveAccount):
        validateM = re.match('([1-3]{1})', haveAccount)
        return validateM

    '''
    Function name: sortCodeCheck()
    Task: validates the input for the sort code
    '''

    def sortCodeCheck (self, sort_code):
        validateS = re.match('[0-9]{2}-[0-9]{2}-[0-9]{2}$', sort_code)
        return validateS

    '''
    Function name: accNoCheck()
    Task: validates the input for the account number
    '''

    def accNoCheck (self, acc_no):
        validateA = re.match('([0-9]{7})', acc_no)
        return validateA

    '''
    Function name: postCodeCheck()
    Task: validates the input for the postcode
    '''

    def postCodeCheck (self, postcode):
        validateP = bool(re.match('[A-Z]{1,2}[0-9A-Z]{1,3}[0-9][A-Z]{2}', postcode))
        return validateP

    '''
    Function name: emailCheck()
    Task: validates the input for the email
    '''

    def emailCheck (self, email):
        validateE = bool(re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email))
        return validateE

    '''
    Function name: passwordCheck()
    Task: validates the input for the password
    '''

    def passwordCheck(self, password):
        validatePass = bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$', password))
        return validatePass

    '''
    Function name: dateCheck()
    Task: validates the input for the date
    '''

    def dateCheck(self, dateOfBooking):
        validateD = bool(re.match('[0-9]{2}-[0-9]{2}-[0-9]{2}$', dateOfBooking))
        return validateD

    '''
    Function name: usernameUnique()
    Task: checks if username is unique 
    '''

    def usernameUnique(self, username):
        
        functionName = 'usernameUnique'
        validateUN =[]

        try:
            
            # Connecting to the DB
            databaseConnection = DatabaseConnection.CreateDBConnection('SharedPower.db')
            cursor = databaseConnection.cursor()

            validateUN = cursor.execute('SELECT cust_id FROM Customers WHERE username = ?', (username,))
           
            if validateUN != 0:
                validateUN = 'unique'
            
            # Disconnecting from the DB
            DatabaseConnection.CloseDBConnection(databaseConnection)

        except Error as e:

            print(__name__, ':', functionName, ':', e)
            raise
        
        return validateUN
