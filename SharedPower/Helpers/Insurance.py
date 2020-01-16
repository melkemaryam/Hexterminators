''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Insurance.py

Created: 17th November 2019

-------------------------------------------------
'''

import sqlite3
import pandas

# AIM: write a program that works out who damaged the product

# we need a way to keep track of:
#     who is in charge of the product 
#     the state of the product

# Example:
#
#     Entity      : Action  : Date (YY/MM/DD) : Status
#     . . . . . . : . . . . : . . . . . . . . : . . . . . .
#     Company     : START   : 19/12/12        : Not damaged
#     Company     : END     : 19/12/15        : Not damaged
#     Transport   : START   : 19/12/15        : Not damaged
#     Transport   : END     : 19/12/16        : Damaged
#     Client_101  : START   : 19/12/16        : Damaged
#     Client_101  : END     : 19/12/18        : Damaged

# this database is all we need in terms of an input for our function

'''
Function name: insurance_tool()
Task: Sorts out the insurance for the tool
'''
def insurance_tool(db):
    '''The argument is the database generated for that item'''
    
    for i in range(db.shape[0]):               # iterates over rows
        if db.at[i,'Status'] == 'Damaged':
            return db.at[i,'Entity']
    return 'Not damaged'                       # if reached, then no damage
            

# creating a sample database...
# date format is YY/MM/DD

db_dict = {'Entity':['Company','Company','Transport','Transport','Client_101','Client_101'],
           'Action':['START','END','START','END','START','END'],
           'Date':['19/12/12','19/12/15','19/12/15','19/12/16','19/12/16','19/12/18'],
           'Status':['Not damaged','Not damaged','Not damaged','Damaged','Damaged','Damaged']
          }

# This is what the database looks like
db = pd.DataFrame(db_dict)
print(db)

# And the guilty one is...
print(insurance_tool(db), 'did it.')
