from os.path import abspath, exists
from os import mkdir
from shutil import rmtree

def path_to_dir(name_dir):
    path_to_app = abspath(__name__)

    path_main_dir = path_to_app[:path_to_app.rindex('\\') + 1]

    path_dir = path_main_dir + name_dir

    return True if exists(path_dir) else False

def proverka_path_dir_icon(name_dir):
    path_to_app = abspath(__name__)

    path_main_dir = path_to_app[:path_to_app.rindex('\\') + 1]

    path_icon_dir = path_main_dir + name_dir

    if exists(path_icon_dir):
        path_icon_dir += '\\'
    else:
        path_icon_dir = ''

    return path_icon_dir

def proverka_or_create_dir_data(path_main_dir ='', name_new_dir = '', select = "main_dir"):
    if select == 'main_dir':
        name_dir = 'Data'
        path_to_app = abspath(__name__)

        path_main_dir = path_to_app[:path_to_app.rindex('\\') + 1] + name_dir

        if exists(path_main_dir):
            path_main_dir += '\\'
        else:
            mkdir(path_main_dir)
            path_main_dir += "\\"

        return path_main_dir

    else:
        path_secondary_dir = path_main_dir + name_new_dir

        if exists(path_secondary_dir):
            path_secondary_dir += '\\'
        else:
            mkdir(path_secondary_dir)
            path_secondary_dir += '\\'

        return path_secondary_dir

def remove_dir(path_dir):
    try:
        rmtree(path_dir[:-1])
    except OSError as e:
        print(f'Error: {e}')
