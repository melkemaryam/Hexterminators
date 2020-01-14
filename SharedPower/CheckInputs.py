''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: CheckInputs.py

Created: 14th January 2020

-------------------------------------------------
'''

import re
import User from User

class CheckInputs:

    def sortCodeCheck (self, sort_code):
        re.match('^[0-9]{2}-[0-9]{2}-[0-9]{2}$', sort_code)

    def accNoCheck (self, acc_no):
        re.match('^[0-9]{7}$', acc_no)

    def postCodeCheck (self, postcode):
        re.match('^[A-Z]{2}[0-9,A-Z]{2,3}[A-Z]{2}$', postcode)

    def emailCheck (self, email):
        re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)

    def passwordCheck(self, password):
        re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$', password)

