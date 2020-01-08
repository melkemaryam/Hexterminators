#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is a program that when called by the owner, sends a request to the insurance company to check if the program is damaged

# sample data base:

# tool | owner | tool number | hire status | ... | <-- columns of the database

# insert database
db = 'some database'

# insurance inbox <- this will be replaced with whatever it is decided to use as communication system
insurance_inbox = ['something like a list']

def request_insurance_check(tool,db,inbox):
    '''sends a request to the <company> to check if the <tool> in the <db> is damaged'''
    
    message = '''Dear Insurance Company,
    Check if the tool %s with serial number %s is damaged''' %(tool, db["tool number"].where(db["tool"]==tool))
    
    inbox.append(message)
    
