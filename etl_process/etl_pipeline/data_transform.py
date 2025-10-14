import pandas as pd 
import os 


def saleOrder_transform(file_path):    
    saleOrder_df = pd.read_csv(r'C:\Users\admin\Desktop\local_env_ppeline_project\raw_data\saleOrder_20251005_134940.csv')
    saleOrder_df.columns = saleOrder_df.columns.str.strip()
    saleOrder_df.columns 
    
    #----------------------------------------------------------------
    saleOrder_df = saleOrder_df.drop_duplicates(subset=['invoiceNum'])
    
    # drop invoice number < 8 digits 
    saleOrder_df = saleOrder_df[~saleOrder_df['invoiceNum'].astype(str).str.fullmatch(r'\d{1,7}')]
    saleOrder_df
    
    
    
    
    
    
    
    
    return saleOrder_df




















