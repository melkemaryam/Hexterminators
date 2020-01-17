''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: NewPassword.py

Created: 15th January 2020

-------------------------------------------------
'''

import hashlib
import binascii
import os

class NewPassword:

    '''
    Function name: Hash()
    Task: hashes a password
    '''
    @staticmethod
    def Hash(password):

        # Generate salt
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

        # Perform the hash
        hashedPassword = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        hashedPassword = binascii.hexlify(hashedPassword)

        return (salt + hashedPassword).decode('ascii')
 
    '''
    Function name: Verify()
    Task: verifies a password from the user input
    '''
    @staticmethod
    def Verify(storedPassword, providedPassword):

        salt = storedPassword[:64]
        storedPassword = storedPassword[64:]
        hashedPassword = hashlib.pbkdf2_hmac('sha512', providedPassword.encode('utf-8'), salt.encode('ascii'), 100000)
        hashedPassword = binascii.hexlify(hashedPassword).decode('ascii')

        return hashedPassword == storedPassword