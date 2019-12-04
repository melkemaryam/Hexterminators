import pandas as pd

import numpy as np


def load_data(path):
    # loads dataframe and returns it 
    # change 'csv' with whatever type the data frame is stored as    

    dataframe = pd.read_csv(path)
    return dataframe

class Invoice:

    def count_month(name):
        monies = dataframe.groupby(["customer_ID"==name]).sum(numeric_only=bool)
        #combines all invoices of a single customer

        return monies
    


##eliminate multiple entries of same ID
##if monies==0 generate email "we realised you didn't rent any tools this month, are all your project now done?"
=======
    print("Hello")
    print("Hi test")
    print("Hi again")
>>>>>>> 63b84d8bab353861d0dd5f7d8615361e6ed76d92
