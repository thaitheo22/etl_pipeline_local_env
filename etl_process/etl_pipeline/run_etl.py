import pandas as pd 
import os 
import sys 
import traceback
#---------------------------------
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_path)
from etl_pipeline_tool import get_file, move_archive, get_function_str
import delivery_tools
#---------------------------------
import logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#---------------------------------
import yaml
import os

# Get the directory containing the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load table configuration
table_config_path = os.path.join(current_dir, 'table_config.yaml')
with open(table_config_path, 'r') as f: 
    table_config = yaml.safe_load(f)

# Load validation configuration
validate_cols_path = os.path.join(current_dir, 'validate_cols.yaml')
with open(validate_cols_path, 'r') as f1: 
    validate_cols = yaml.safe_load(f1)
#===============================================================================================

def run_etl_process(table_config, validate_columns):
    try: 
        file = get_file(table_config['raw_data_folder'], table_config['prefix'], table_config['suffix'])
        if not file:
            logging.error('No file passed!')
            return None
        
        func = get_function_str(table_config['transform_func'])
        if not func:
            logging.error(f'no function name with {table_config['transform_func']}')
            return None
        
        dfs = func(file)
        if isinstance(dfs, tuple):
            pass
        else: 
            delivery_tools.df_to_sql(dfs, table_config['schema'], table_config['table_name'], validate_columns)
            move_archive(table_config['archive_folder'], file)
            
            
    except Exception as e: 
        logging.error('there is something wrong')
        print(e)
        traceback.print_exc()
        move_archive(table_config['archive_fail_folder'], file)
        return None
        

    
def process_config():
    config = table_config['table_config'] 
    validation_rules = validate_cols['validate_columns'] 
    run_etl_process(config, validation_rules)
    
        
        
