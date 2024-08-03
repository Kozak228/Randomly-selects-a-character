from time import sleep
from threading import Thread
from logging import getLogger
from os import listdir

from GUI.download_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt

from requests import get

from Parser_data import Parser_data
from Create_and_remove_forders import path_to_dir, proverka_path_dir_icon, remove_dir_or_file, proverka_or_create_dir_data
from Read_file import read_file

class Parser_and_download(QMainWindow):
    def __init__(self):
        super(Parser_and_download, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(351, 151)

        self.logger = getLogger('app.download')

        self.thread_pars = Thread(target=self.pars_links)

        self.name_file = 'data'
        self.name_dir = 'Data'

        self.ui.pushButton_pars_and_download_data.clicked.connect(self.download_data)

    def pars_links(self):
        parser_data = Parser_data('https://paimon.moe/characters')

        parser_data.pars_data()
    def download_data(self):
        self.ui.pushButton_pars_and_download_data.setEnabled(False)
        self.ui.pushButton_exit.setEnabled(False)

        self.ui.progressBar.setValue(0)
        self.cnt_img = 0

        self.ui.label_download_info.setText('Збiр даних....')
        QApplication.processEvents()

        try:
            self.thread_pars.start()
            self.thread_pars.join()

        except RuntimeError as ex:
            self.logger.error(ex)

        path_main_dir = proverka_or_create_dir_data()

        self.read_file_dates(path_main_dir, self.name_file)

        self.ui.progressBar.setMaximum(self.cnt_total_dates)

        if self.dict_all_dates.get('links_on_img_element'):
            path_secondary_dir = proverka_or_create_dir_data(path_main_dir, 'element', "")

            self.download_image(path_secondary_dir, self.dict_all_dates.get('links_on_img_element'))

        path_secondary_beside_dir = proverka_or_create_dir_data(path_main_dir, 'elements_characters', "")

        for characters_with_elem in range(len(self.list_names_element)):
            if self.dict_all_dates.get(self.list_names_element[characters_with_elem]):
                path_secondary_dir = proverka_or_create_dir_data(path_secondary_beside_dir,
                                                                 self.list_names_element[characters_with_elem],
                                                                 "")

                self.download_image(path_secondary_dir, self.dict_all_dates.get(self.list_names_element[characters_with_elem]))

        self.delete_dir_or_file(path_main_dir, self.name_file)

        self.ui.pushButton_exit.setEnabled(True)

    def download_image(self, path_dir, links):
        for i in links:
            req = get(i)
            response = req.content

            with open(f'{path_dir}{i[i.rindex("/") + 1:]}', 'wb') as f:
                f.write(response)

            self.cnt_img += 1

            self.ui.progressBar.setValue(self.cnt_img)
            QApplication.processEvents()

            self.ui.label_download_info.setText(f'Завантажено: {self.cnt_img} / {self.cnt_total_dates}')
            sleep(0.2)

        if self.cnt_img == self.cnt_total_dates:
            self.ui.label_download_info.setText('Дані завантажені')

    def delete_dir_or_file(self, path, name_file = ''):
        if name_file == "":
            if path_to_dir('Data'):
                remove_dir_or_file(path, name_file)

        else:
            remove_dir_or_file(path, name_file)

    def check_data_in_PC(self):
        path_dir = proverka_path_dir_icon(self.name_dir)
        list_dirs_in_data = listdir(path_dir)
        list_all_data_in_PC = []

        if path_to_dir(self.name_dir) and len(list_dirs_in_data) != 0:
            path_dir_element = proverka_or_create_dir_data(proverka_or_create_dir_data(), 'element', '')
            path_dir_elements_character = proverka_or_create_dir_data(proverka_or_create_dir_data(), 'elements_characters', '')

            list_element_img = listdir(path_dir_element)

            list_all_data_in_PC.extend(list_element_img)

            for elem in list_element_img:
                list_all_data_in_PC.extend(listdir(proverka_or_create_dir_data(path_dir_elements_character,
                                                                               elem[:elem.rindex('.')], '')))

        return list_all_data_in_PC

    def read_file_dates(self, path_dir, name_file):
        list_all_data_in_PC = self.check_data_in_PC()
        self.dict_all_dates = read_file(name_file, path_dir)

        self.list_names_element = self.dict_all_dates.get('names_element')

        self.dict_all_dates.pop('names_element')

        if list_all_data_in_PC:
            new_dict_all_dates = {}
            list_keys = list(self.dict_all_dates.keys())

            for key in list_keys:
                list_links_in_key = self.dict_all_dates.get(key)

                new_list_links = []
                for link in list_links_in_key:
                    if link[link.rindex('/') + 1:] not in list_all_data_in_PC:
                        new_list_links.append(link)

                new_dict_all_dates[key] = new_list_links
            self.dict_all_dates = new_dict_all_dates

        temp_dict_values = list(self.dict_all_dates.values())

        self.cnt_total_dates = 0

        for i in range(len(temp_dict_values)):
            self.cnt_total_dates += len(temp_dict_values[i])