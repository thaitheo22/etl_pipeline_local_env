import pandas as pd 
import os 
import sys 
import pathlib
import shutil 
import importlib
    
import yaml 
with open('table_config.yaml', 'r') as f: 
    yaml_config = yaml.safe_load(f)


def func_str():
    pass
    
    
    

def get_file(folder_path, prefix):
    for file_name in os.listdir(folder_path): 
        if file_name.startswith(prefix) and file_name.endswith('csv'):
            fullpath_file = os.path.join(folder_path, file_name)
            return fullpath_file


def move_archive(archvie_folder, fullpath_file):
    file_name = os.path.basename(fullpath_file)
    archive_file = os.path.join(archvie_folder, file_name)    
    shutil.move(fullpath_file, archive_file)









