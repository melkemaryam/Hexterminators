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

from GetterSetter.User import User 
from Helpers.DatabaseConnection import DatabaseConnection
from Helpers.LoadUser import LoadUser

class CheckInputs:

    def mainmenu (self, haveAccount):
        validateM = re.match('([1-3]{1})', haveAccount)
        return validateM

    def sortCodeCheck (self, sort_code):
        validateS = re.match('[0-9]{2}-[0-9]{2}-[0-9]{2}$', sort_code)
        return validateS

    def accNoCheck (self, acc_no):
        validateA = re.match('([0-9]{7})', acc_no)
        return validateA

    def postCodeCheck (self, postcode):
        validateP = bool(re.match('[A-Z]{1,2}[0-9A-Z]{1,3}[0-9][A-Z]{2}', postcode))
        return validateP

    def emailCheck (self, email):
        validateE = bool(re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email))
        return validateE

    def passwordCheck(self, password):
        validatePass = bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$', password))
        return validatePass

    def dateCheck(self, dateOfBooking):
        validateD = bool(re.match('[0-9]{2}-[0-9]{2}-[0-9]{2}$', dateOfBooking))
        return validateD

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