''' 
-------------------------------------------------
Project: SharedPower
Group: Hexterminators
File name: CheckInputs.py
Created: 14th January 2020
-------------------------------------------------
'''

import re

class CheckInputs:

    def sortCodeCheck (self, sort_code):
        validateS = bool(re.match('^(?=.*\d)(?=.*[-])[\d-]{8,}$', sort_code))
        return validateS

    def accNoCheck (self, acc_no):
        validateA = bool(re.match('^[0-9]{7}$', acc_no))
        return validateA

    def postCodeCheck (self, postcode):
        validateC = bool(re.match('^[A-Z]{2}[0-9,A-Z]{2,3}[A-Z]{2}$', postcode))
        return validateC

    def emailCheck (self, email):
        validateE = bool(re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email))
        return validateE

    def passwordCheck(self, password):
        validatePass = bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$', password))
        return validatePass