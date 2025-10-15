import pandas as pd
import traceback
import numpy as np

import os 
import sys 
sys.path.append(os.path.abspath(r'C:\Users\admin\Desktop\local_env_ppeline_project\etl_process'))
from sql_server_config import pg_connection

import openpyxl

#===========================================================================================================

def validate_df_columns(df, schema, sql_tb, valid_col_dict):
    _, engine = pg_connection()
    df.columns = df.columns.str.strip() 
    
    query = f'SELECT * FROM {schema}.{sql_tb}'
    sql_table = pd.read_sql(query, con=engine)
    
    sql_col_list = list(sql_table.columns)
    valid_col_list = list(valid_col_dict.keys())
    
    # thay tên đổi họ cho tên cột 
    rename_col_dict = {}
    for sql_col in sql_col_list:
        try: 
            if sql_col not in valid_col_list:
                continue
            
            for i in range(len(list(df.columns))):
                if list(df.columns)[i] == sql_col or list(df.columns)[i] in valid_col_dict[sql_col]:
                    rename_col_dict[list(df.columns)[i]] = sql_col
        except: 
            traceback.print_exc()
    df = df.rename(columns=rename_col_dict)
    
    
    # thêm cột 
    for sql_col in sql_col_list: 
        if sql_col not in list(df.columns):
            df[sql_col] = np.nan
            
    # xóa cột 
    for df_col in list(df.columns):
        if df_col not in sql_col_list:
            df = df.drop(columns=[df_col])
            
    # sắp xếp cột 
    df_col = list(df.columns)
    for i in range(len(sql_col_list)):
        j = i 
        while df_col[j] != sql_col_list[i]:
            j += 1
        else: 
            temp = df_col[j]
            df_col[j] = df_col[i] 
            df_col[i] = temp 
    
    df = df[df_col]
    
    #replace empty string into np.nan
    df = df.replace('', np.nan, regex=True)
    
    return df

#===========================================================================================================

def pure_sql_execute(query):
    pg_connect, _ = pg_connection()
      
    try: 
        cursor = pg_connect.cursor()
        cursor.execute(query)
        pg_connect.commit()
        print('execute sucessfully')
        
    except Exception as e:
        print('execute fails')
        traceback.print_exc()
        pg_connect.rollback()
    
    finally:    
        cursor.close()
        pg_connect.close()


        
def sql_to_df(query):
    _, engine_connect = pg_connection()   
    try:
        df = pd.read_sql(query, engine_connect)
        return df 
    except Exception as e: 
        print('there is something wrong when read sql')
        traceback.print_exc()
        print(e)
             
        
def sql_to_csv(query, file_path):
    _, engine_connect = pg_connection()
    try:             
        df = pd.read_sql(query, engine_connect)
        df.to_csv(file_path, index=False)
    except Exception as e: 
        print('there is something wrong when read sql')
        traceback.print_exc()
        print(e)
        
#-------------------------------------------------------------------------------------------------------

def df_to_csv_simple(df, file_path):
    try: 
        df.to_csv(file_path, index=False)
    except Exception as e:
        print('there is something wrong')    
        traceback.print_exc()
        print(e)


def df_to_sql(df, schema, tb_name, valid_col_dict):
    import psycopg2
    import numpy as np
    import psycopg2
    from psycopg2.extensions import register_adapter, AsIs
    # --- register numpy adapters ---
    def adapt_numpy_float64(numpy_float64):
        return AsIs(float(numpy_float64))

    def adapt_numpy_int64(numpy_int64):
        return AsIs(int(numpy_int64))
    
    def adapt_numpy_datetime64(numpy_datetime64):
        return AsIs(f"'{pd.Timestamp(numpy_datetime64).to_pydatetime()}'")
    
    register_adapter(np.float64, adapt_numpy_float64)
    register_adapter(np.int64, adapt_numpy_int64)
    register_adapter(np.datetime64, adapt_numpy_datetime64)
    
    pg_connect, connect_str = pg_connection()
    
    valid_df = validate_df_columns(df, schema, tb_name, valid_col_dict)

    df_col = list(valid_df.columns)
    df_col = ','.join(tuple(df_col))
    
    valid_df = valid_df.replace('', np.nan)
    
    df_records = valid_df.to_records(index=False)
    records_list = [
        tuple(None if (isinstance(x, float) and np.isnan(x)) else x for x in record) 
        for record in df_records
    ]
    
    placeholder = ','.join(['%s']*len(list(valid_df.columns)))
    
    cursor = pg_connect.cursor()

    query = f'''
        INSERT INTO {schema}.{tb_name}({df_col})
        VALUES({placeholder})
    ''' 
    cursor.executemany(query, records_list)
    
    pg_connect.commit()
    
    cursor.close()
    pg_connect.close()


# import yaml 
# with open(r'C:\Users\admin\Desktop\local_env_ppeline_project\etl_process\etl_pipeline\validate_cols.yaml', 'r') as f: 
#     tb_cols = yaml.safe_load(f)
# with open(r'C:\Users\admin\Desktop\local_env_ppeline_project\etl_process\etl_pipeline\table_config.yaml', 'r') as f1: 
#     table_config = yaml.safe_load(f1)
#     tb_config = table_config['table_config']


# import pandas as pd 
# sys.path.append(os.path.abspath(r'C:\Users\admin\Desktop\local_env_ppeline_project\etl_process\etl_pipeline'))
# import data_transform
# df = data_transform.saleOrder_transform(r'C:\Users\admin\Desktop\local_env_ppeline_project\raw_data\saleOrder_20251005_135254.csv')
# df_to_sql(df, tb_config['schema'], tb_config['table_name'], tb_cols['validate_columns'])


'''
pd.ExcelFile: read excel file 
pd.ExcelWrter: write excel file 
'''
def df_to_csv(df, filepath, sheetname):
    try: 
        with pd.ExcelWriter(path=filepath, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=sheetname, index=False)
            print('Done!')
    except: 
        traceback.print_exc()


#===============================================================================================================






















