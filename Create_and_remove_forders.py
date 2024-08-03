from os.path import abspath, exists, isfile
from os import mkdir, remove
from shutil import rmtree
from logging import getLogger

def path_to_dir(name_dir):
    path_to_app = abspath(__name__)

    path_main_dir = path_to_app[:path_to_app.rindex('\\') + 1]

    path_dir = path_main_dir + name_dir

    return True if exists(path_dir) else False

def path_to_file(path_file, name_file):
    return True if exists(f"{path_file + name_file}.json") else False

def proverka_path_dir_icon(name_dir):
    path_to_app = abspath(__name__)

    path_main_dir = path_to_app[:path_to_app.rindex('\\') + 1]

    path_icon_dir = path_main_dir + name_dir

    if exists(path_icon_dir):
        path_icon_dir += '\\'
    else:
        path_icon_dir = path_main_dir

    return path_icon_dir

def proverka_or_create_dir_data(path_main_dir='', name_new_dir='', select="main_dir"):
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

def remove_dir_or_file(path_dir, name_file):
    try:
        rmtree(path_dir[:-1]) if name_file == '' else remove(f'{path_dir + name_file}.json')
    except OSError as ex:
        logger = getLogger('app.download.remove')
        logger.error(ex)