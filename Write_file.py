from json import dumps

from Loging_error import log_error
from Create_and_remove_forders import proverka_path_dir_icon

def write_file(dicts, file_name, file_path):
    try:
        json_file = dumps(dicts, indent=4, ensure_ascii=False)

        with open(f'{file_path}{file_name}.json', 'w') as f:
            f.write(json_file)

    except Exception as ex:
        log_error(proverka_path_dir_icon('log'), ex)