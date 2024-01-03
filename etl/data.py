import pandas as pd
import numpy as np
import os

from etl.Extracts import Extracts
from etl.Transforms import Transforms

#############################################################################
###                                                                       ###
###                             Extracts data                             ###
###                                                                       ###
#############################################################################

ikea = Extracts(os.getcwd() +'/data/ikea.csv').load_data()

def fix_old_price(df):
    
    # fill in price to old_price for No old price
    if df['old_price']  == 'No old price':              
        return df['price']

    # remove SR and , from old_price                            
    elif df['old_price'][-4:] != 'pack':                
        return float(str(df['old_price'])[3:].replace(',','')) 
                                                               
    else:
        return np.nan

#############################################################################
###                                                                       ###
###                            Transform Data                             ###
###                                                                       ###
#############################################################################
def factTable(df):
    df=df.drop(['Unnamed: 0'],axis=1)
    median_depth=df.groupby('category')['depth'].median().reset_index()
    median_depth.columns = ['category','medianDepth']

    median_height=df.groupby('category')['height'].median().reset_index()
    median_height.columns = ['category','medianHeight']

    median_width=df.groupby('category')['width'].median().reset_index()
    median_width.columns = ['category','medianWidth']

    
    median_size = Transforms(Transforms(median_depth,median_height,'category').transform_state(),median_width,'category').transform_state()

    
    df=Transforms(df,median_size,'category').transform_state()
    df['depth']=df['depth'].fillna(df['medianDepth'])
    df['height']=df['height'].fillna(df['medianHeight'])
    df['width']=df['width'].fillna(df['medianWidth'])

    df.drop(['medianDepth','medianHeight','medianWidth'],axis=1 ,inplace=True)
    # create new colum price_diff to help identified is there any different
    # between price and old_price

    df['price_diff']=(df['old_price']!='no old price')

    #apply the function 
    df['old_price']=df.apply(fix_old_price,axis=1)
    df['old_price']=df['old_price'].fillna(df['price'])
    
    return df