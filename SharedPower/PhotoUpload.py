''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: PhotoUpload.py

Created: 15th January 2020

-------------------------------------------------
'''

import time

class PhotoUpload:

    '''
    Function name: upload()
    Task: gives the user the possibility to upload a photo, theoretically
    '''

    @staticmethod
    def upload():
        file_path = input('Please specify the path:')
        print('Uploading file ', file_path)
        time.sleep(2)