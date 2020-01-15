''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: __init__.py

Created: 15th January 2020

-------------------------------------------------
'''

import datetime

from sqlite3 import Error

from Menu import Menu

databaseFilename = 'SharedPower.db'
function_name = '__init__'

try:
    registeredUser = None

    #start off by getting the user to sign in or sign up and sign in if necessary
    menu = Menu(databaseFilename)
    confirmUser = menu.checkAccount()

    #Once user is succesfully signed in ask him what is his/her desire
    
    if (confirmUser != None):
        userInput = None
        while (userInput != 'back'):

            action_choice = Menu.action()
        
        Menu.checkAccount()


    print('Thank you for Sharing your Power. Good bye.')

except Error as e:

    # Catch and display any errors that occur
    print(__name__, ':', function_name, " - ", e)

