# Acquire.py Functions Using REST API that Returns JSON

import requests
import os
import numpy as np
import pandas as pd

######################################### Items DF ########################################

def get_items():
    
    if os.path.isfile('items_df.csv') == False:
        
        base_url = 'https://python.zach.lol'
        api_url = base_url + '/api/v1/items'
        response = requests.get(api_url)
        data = response.json()
        df_items = pd.DataFrame(data['payload']['items'])
        
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df_items = pd.read_csv('items_df.csv', index_col=0)
        
    return df_items

######################################### Stores DF #######################################

def get_stores():
    
    if os.path.isfile('stores_df.csv') == False:
        
        base_url = 'https://python.zach.lol'
        api_url = base_url + '/api/v1/stores'
        response = requests.get(api_url)
        data = response.json()
        df_stores = pd.DataFrame(data['payload']['stores'])
        
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df_stores = pd.read_csv('stores_df.csv', index_col=0)

    return df_stores
    
######################################### Sales DF ########################################

def get_sales():
    
    if os.path.isfile('sales_df.csv') == False:
        
        base_url = 'https://python.zach.lol'

        api_url = base_url + '/api/v1/'
        response = requests.get(api_url + 'sales')
        data = response.json()
    
        # create list from 1st page
        output = data['payload']['sales']

        # loop through the pages and add to list
        while data['payload']['next_page'] != None:
    
            response = requests.get(base_url + data['payload']['next_page'])
            data = response.json()
            output.extend(data['payload']['sales'])
    
        df_sales = pd.DataFrame(output)
        
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df_sales = pd.read_csv('sales_df.csv', index_col=0)
        
    return df_sales

####################################### Joined Sales DF ########################################

def get_joined_sales():
    
    if os.path.isfile('joined_sales_df.csv') == False:
        
        df_items = get_items()
        df_stores = get_stores()
        df_sales = get_sales()
    
        # left join sales and stores
        df = pd.merge(df_sales, df_stores, left_on='store', right_on='store_id').drop(columns={'store'})
    
        # left join the joined df to the items
        df = pd.merge(df, df_items, left_on='item', right_on='item_id').drop(columns={'item'})
        
    else:
        # Reads the csv saved from above, and assigns to the df variable
        joined_sales_df = pd.read_csv('joined_sales_df.csv', index_col=0) 
        
    return joined_sales_df

######################################### Open Power DF ########################################

def get_open_power():

    if os.path.isfile('open_power_df.csv') == False:
        
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        open_power_df = pd.read_csv(url)
        
    else:
        # Reads the csv saved from above, and assigns to the df variable
        open_power_df = pd.read_csv('open_power_df.csv', index_col=0)
    
    return open_power_df