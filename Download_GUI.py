from time import sleep

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
        self.setFixedSize(436, 148)

        self.name_file = 'data'

        self.ui.pushButton_pars_and_download_data.clicked.connect(self.download_data)

    def pars_links(self):
        parser_data = Parser_data('https://paimon.moe/characters')

        parser_data.pars_data()
    def download_data(self):
        self.ui.pushButton_pars_and_download_data.setEnabled(False)
        self.ui.pushButton_exit.setEnabled(False)

        self.ui.horizontalSlider.setValue(0)

        self.cnt_img = 0

        path_main_dir = proverka_path_dir_icon('Data')

        self.delete_dir_or_file(path_main_dir)

        self.ui.label_download_info.setText('Збiр даних....')
        QApplication.processEvents()

        self.pars_links()

        sleep(3)

        path_main_dir = proverka_or_create_dir_data()

        self.read_file_dates(path_main_dir, self.name_file)

        self.ui.horizontalSlider.setMaximum(self.cnt_total_dates)

        path_secondary_dir = proverka_or_create_dir_data(path_main_dir, 'element',"")

        self.download_image(path_secondary_dir, self.dict_all_dates.get('links_on_img_element'))

        for characters_with_elem in range(len(self.list_names_element)):

            path_secondary_dir = proverka_or_create_dir_data(path_main_dir, self.list_names_element[characters_with_elem],
                                                             "")

            self.download_image(path_secondary_dir, self.dict_all_dates.get(self.list_names_element[characters_with_elem]))

        self.delete_dir_or_file(path_main_dir, self.name_file)

        self.ui.pushButton_pars_and_download_data.setEnabled(True)
        self.ui.pushButton_exit.setEnabled(True)

    def download_image(self, path_dir, links):
        for i in links:
            req = get(i)
            response = req.content

            with open(f'{path_dir}{i[i.rindex("/") + 1:]}', 'wb') as f:
                f.write(response)

            self.cnt_img += 1

            self.ui.horizontalSlider.setValue(self.cnt_img)
            QApplication.processEvents()

            self.ui.label_download_info.setText(f'Завантажується: {self.cnt_img} / {self.cnt_total_dates}')
            sleep(0.2)

        if self.cnt_img == self.cnt_total_dates:
            self.ui.label_download_info.setText('Загрузка завершена')

    def delete_dir_or_file(self, path, name_file = ''):
        if name_file == "":
            if path_to_dir('Data'):
                remove_dir_or_file(path, name_file)

        else:
            remove_dir_or_file(path, name_file)

    def read_file_dates(self, path_dir, name_file):
        self.dict_all_dates = read_file(name_file, path_dir)

        self.list_names_element = self.dict_all_dates.get('names_element')

        temp_dict = self.dict_all_dates.copy()

        temp_dict.pop('names_element')

        temp_dict_values = list(temp_dict.values())

        self.cnt_total_dates = 0

        for i in range(len(temp_dict_values)):
            self.cnt_total_dates += len(temp_dict_values[i])