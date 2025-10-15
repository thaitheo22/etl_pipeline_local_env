import pandas as pd 
import os 


def saleOrder_transform(file_path):    
    saleOrder_df = pd.read_csv(file_path)
    saleOrder_df.columns = saleOrder_df.columns.str.strip()
    saleOrder_df.columns 
    
    #----------------------------------------------------------------
    saleOrder_df = saleOrder_df.drop_duplicates(subset=['invoiceNum'])
    
    # drop invoice number < 8 digits 
    saleOrder_df = saleOrder_df[~saleOrder_df['invoiceNum'].astype(str).str.fullmatch(r'\d{1,7}')]
    saleOrder_df
    
    # work with order_date - format MM/DD/YYYY
    saleOrder_df['orderDate'] = pd.to_datetime(saleOrder_df['orderDate'], format='%m/%d/%Y', errors='coerce') 
    saleOrder_df = saleOrder_df.loc[~saleOrder_df['orderDate'].isnull()]

    
    return saleOrder_df




















