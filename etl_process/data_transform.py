import pandas as pd 
import os 


def saleOrder_transform(file_path):    
    saleOrder_df = pd.read_csv(r'C:\Users\admin\Desktop\local_env_ppeline_project\raw_data\saleOrder_20251005_102646.csv')

    #---------------------------------------------------------------------------------------------
    # work with dim customer table 
    customer_tb = saleOrder_df[['customerName', 'customerGender', 'birthYear']]
    customer_tb = customer_tb.drop_duplicates(['customerName'])
    
    #---------------------------------------------------------------------------------------------
    # work with product table 
    product_tb = saleOrder_df[['productName', 'productColor', 'productSize', 'productCategory', 'productUnitPrice']]
    product_tb = product_tb.drop_duplicates(subset=['']) 


    return saleOrder_df




















