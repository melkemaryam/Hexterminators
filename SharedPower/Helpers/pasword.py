import hashlib
import os
class PasswordHelp: 
    
    @staticmethod 
    def hashPassword(pwd):

        salt = os.urandom(60)
        pwd = password

        Key = hashlib.pbkdf2_hmac()
        'sha256'
        password.encode('utf-8')
        salt,100000
        dklen=128
        storage= salt+Key
        salt_froms_storage = storage(30)
        key_from_stortage =storage(30)

    @staticmethod
    def verifyPassword(password_to_check):
        salt= user 
        key = user
        pwd = password_to_check

        new_key= haslib.pbkdf2_hmac(
        'sha256'
        password_to_check.encode('utf-8')
        salt,100000
)
        if new_key == key:
            print('correct')
        else 
            print('incorrect')