from os import listdir
from random import choice

from GUI.main_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

from Download_GUI import Parser_and_download
from Timer_GUI import Timers
from Loging_error import logger_init

from Create_and_remove_forders import path_to_dir, proverka_or_create_dir_data, proverka_path_dir_icon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.BypassWindowManagerHint)
        self.setFixedSize(361, 299)

        self.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}main_app.ico"))
        self.ui.pushButton_clear.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}clear.png"))

        logger_init('app')

        self.reload_exist()

        self.parser_and_download_window = Parser_and_download()
        self.timer_window = Timers()

        self.ui.pushButton_rand_elem.clicked.connect(self.btn_random_element)
        self.ui.pushButton_rand_charact.clicked.connect(self.btn_random_character)
        self.ui.pushButton_clear.clicked.connect(self.btn_clear_labels)
        self.ui.pushButton_download_data.clicked.connect(self.download_datas)
        self.ui.pushButton_timer.clicked.connect(self.timer)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)

    def timer(self):
        self.hide()

        self.timer_window.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}timer.ico"))
        self.timer_window.show()

        self.timer_window.ui.pushButton_exit.clicked.connect(self.return_main_with_timer_window)

    def return_main_with_timer_window(self):
        self.timer_window.close()
        self.show()

    def download_datas(self):
        self.hide()

        self.parser_and_download_window.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}download.ico"))

        self.parser_and_download_window.ui.pushButton_pars_and_download_data.setEnabled(True)

        self.parser_and_download_window.show()

        self.parser_and_download_window.ui.pushButton_exit.clicked.connect(self.return_main_with_parser_and_download_window)

    def return_main_with_parser_and_download_window(self):
        self.parser_and_download_window.close()
        self.reload_exist()
        self.show()

    def btn_random_element(self):
        self.random_element = choice(self.list_element_img)

        pixmap = QPixmap(f'{self.path_dir_element + self.random_element}')
        pixmap = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.label_img_element.setPixmap(pixmap)
        self.ui.label_img_element.setStyleSheet(self.change_border_color_label_with_elem(self.random_element[:self.random_element.rindex('.')]))

        self.ui.label_img_charact.clear()
        self.ui.label_img_charact.setStyleSheet(self.change_border_color_label_with_elem(''))

    def btn_random_character(self):
        path_dir_element_characters = proverka_or_create_dir_data(self.path_to_data,
                                                                  self.random_element[:self.random_element.rindex('.')],
                                                                  '')

        list_element_characters_img = listdir(path_dir_element_characters)

        random_element_character = choice(list_element_characters_img)

        pixmap = QPixmap(f'{path_dir_element_characters + random_element_character}')

        self.ui.label_img_charact.setPixmap(pixmap)
        self.ui.label_img_charact.setStyleSheet(self.change_border_color_label_with_elem(self.random_element[:self.random_element.rindex('.')]))

    def change_border_color_label_with_elem(self, element):
        if element == 'anemo':
            return 'border: 2px solid #37dba4;'
        elif element == 'cryo':
            return 'border: 1px solid #65e1ea;'
        elif element == 'dendro':
            return 'border: 1px solid #8ac500;'
        elif element == 'electro':
            return 'border: 1px solid #c97bfe;'
        elif element == 'geo':
            return 'border: 1px solid #f8a300;'
        elif element == 'hydro':
            return 'border: 1px solid #08e4ff;'
        elif element == 'pyro':
            return 'border: 1px solid #ef5f02;'
        else:
            return 'border: none;'

    def reload_exist(self):
        self.exists_dir('Data')
        self.path_pulling()

    def path_pulling(self):
        if path_to_dir('Data') and len(self.list_dirs_in_data) == 8:
            self.path_to_data = proverka_or_create_dir_data()
            self.path_dir_element = proverka_or_create_dir_data(self.path_to_data, 'element', '')

            self.list_element_img = listdir(self.path_dir_element)

    def exists_dir(self, name_dir):
        path_dir = proverka_path_dir_icon(name_dir)
        self.list_dirs_in_data = listdir(path_dir)

        if path_to_dir(name_dir) and len(self.list_dirs_in_data) == 8:
            self.ui.label_info_folder.setText("Дані знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #00FF00;")

            self.ui.pushButton_rand_charact.setEnabled(True)
            self.ui.pushButton_rand_elem.setEnabled(True)
            self.ui.pushButton_clear.setEnabled(True)

            self.ui.pushButton_download_data.setText("Оновити\nдані")

        else:
            self.ui.label_info_folder.setText("Дані не знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #FF0000;")

            self.ui.pushButton_rand_charact.setEnabled(False)
            self.ui.pushButton_rand_elem.setEnabled(False)
            self.ui.pushButton_clear.setEnabled(False)

            self.ui.pushButton_download_data.setText("Завантажити\nдані")

    def btn_clear_labels(self):
        self.ui.label_img_charact.clear()
        self.ui.label_img_charact.setStyleSheet(self.change_border_color_label_with_elem(''))
        self.ui.label_img_element.clear()
        self.ui.label_img_element.setStyleSheet(self.change_border_color_label_with_elem(''))

    def btn_app_exit(self):
        self.exit_app()

    def exit_app(self):
        QApplication.instance().quit
        exit()