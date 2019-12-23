import sqlite3
#import pandas as pd



def load_data(path):
    # loads dataframe and returns it 
    # change 'csv' with whatever type the data frame is stored as    
    
    dataframe = pd.read_csv(path)
    return dataframe



def choose_filters():
    # returns a list of the input variables
    # in_x means: user input of x (x = type, duration etc)
    
    print('''Select the type of tool: \n
    (M) Manual \n
    (E) Electric \n
    Leave blank for no filter''')
    
    # the above print statement can be replaced with a drop down list
    # like on more conventional filter tools
    
    in_type = input()
    
    # the variable stores the input which will be used later
    # to filter through the database
    
    print('''Select the duration (in days) for which you wish to hire the tool for: \n
    (1) 1 day  \n
    (2) 2 days \n
    (3) 3 days \n
    (+) 4+ days''')
    
    in_duration = input()
    
    # this function can be extended to include as many filters as needed
    
    return [in_type,in_duration] 

# storing the filters in the variable
filters = choose_filters() 



def filter_data(lst):
    # argument will contain the list of inputs
    # returns filtered dataframe
    
    cols_to_filter = ["Type","Duration"] 
    # list of the filtrable columns - this can be implemented earlier in the code and it can be extended
    # this list has to match the 'filters' list
    
    filter_list = [] # we will save the filters here
    
    # iterating through each input
    for i in lst:
        if i != '':
            filter_list.append(dataframe[cols_to_filter[i]] == lst[i])
       
    return dataframe.where(filter_list)