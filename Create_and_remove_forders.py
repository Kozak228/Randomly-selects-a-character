from os.path import abspath, exists
from os import mkdir
from shutil import rmtree

def proverka_or_create_dir(path_main_dir ='', name_new_dir = '', select = "main_dir"):
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

# def main():
#     path_main_dir = proverka_or_create_dir()
#     print(f'main: {path_main_dir}')
    # path_secondary_dir = proverka_or_create_dir(path_main_dir, 'pyro',"")
    # print(f'path_secondary_dir: {path_secondary_dir}')
    # path_secondary_dir = proverka_or_create_dir(path_main_dir, 'crio',"")
    # print(f'path_secondary_dir: {path_secondary_dir}')
    # path_secondary_dir = proverka_or_create_dir(path_main_dir, 'geo',"")
    # print(f'path_secondary_dir: {path_secondary_dir}')
    # remove_dir(path_main_dir)

# if __name__ == '__main__':
#     main()