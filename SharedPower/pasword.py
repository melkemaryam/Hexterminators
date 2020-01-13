# generating password 
 #import 

 s = "abcdefgijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*-+"
 passlen = 7 
 p = "" .join(random.sample(s,passlen))
print p 

#hash 
#import hashlib
#import os

salt = os.urandom(30)
password= #generating password p""

Key= hashlib.pbkdf2_hmac(
    'sha256'
    password.encode('utf-8')
    salt,150000
    dklen=128
    storage= salt+Key
    salt_froms_storage = storage(30)
    key_from_stortage =storage(30)

salt= user'' 
key = user''

password_to_check =#'generating password p'

new_key= haslib.pbkdf2_hmac(
    'sha256'
    password_to_check.encode('utf-8')
    salt,150000
)
if new_key== #generate password
print('correct')
else
print('wrong')
endif 