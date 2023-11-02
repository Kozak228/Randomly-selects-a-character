from json import loads

from Loging_error import log_error
from Create_and_remove_forders import proverka_path_dir_icon

def read_file(file_name, file_path):
    try:
        with open(f'{file_path}{file_name}.json') as f:
            slovar = loads(f.read())

        return slovar
    
    except FileNotFoundError as ex:
        log_error(proverka_path_dir_icon('log'), ex)
        return {}