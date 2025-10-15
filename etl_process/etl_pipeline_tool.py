import pandas as pd 
import os 
import sys 
import pathlib
import shutil 
import importlib


def get_file(folder_path, prefix, suffix):
    for file_name in os.listdir(folder_path): 
        if file_name.startswith(prefix) and file_name.endswith(suffix):
            fullpath_file = os.path.join(folder_path, file_name)
            return fullpath_file


def move_archive(archvie_folder, fullpath_file):
    file_name = os.path.basename(fullpath_file)
    archive_file = os.path.join(archvie_folder, file_name)    
    shutil.move(fullpath_file, archive_file)



def get_function_str(func_str):
    module_name, func_name = func_str.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, func_name)
    





        





