from os import listdir
from random import choice, randrange
from time import sleep

from GUI.main_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

from Download_GUI import Parser_and_download
from Timer_GUI import Timers
from Loging_error import logger_init

from Create_and_remove_forders import path_to_dir, proverka_or_create_dir_data, proverka_path_dir_icon, path_to_file
from Read_file import read_file

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.BypassWindowManagerHint)
        self.setFixedSize(360, 470)

        self.ui.groupBox_3.setEnabled(False)
        self.ui.groupBox_3.hide()

        self.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}main_app.ico"))
        self.ui.pushButton_clear.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}clear.png"))
        self.ui.pushButton_clear_2.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}clear.png"))

        logger_init('app')

        self.reload_exist()

        self.parser_and_download_window = Parser_and_download()
        self.timer_window = Timers()

        self.ui.pushButton_rand_elem.clicked.connect(self.btn_random_element)
        self.ui.pushButton_rand_charact.clicked.connect(self.btn_random_character)
        self.ui.pushButton_rand_squad.clicked.connect(self.btn_random_squad)
        self.ui.pushButton_clear.clicked.connect(self.btn_clear_labels)
        self.ui.pushButton_clear_2.clicked.connect(self.btn_clear_labels)
        self.ui.pushButton_download_data.clicked.connect(self.download_datas)
        self.ui.pushButton_timer.clicked.connect(self.timer)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)

        self.ui.radioButton_rand_elem_charact.toggled.connect(lambda: self.btn_state(self.ui.radioButton_rand_elem_charact))
        self.ui.radioButton_rand_squad.toggled.connect(lambda: self.btn_state(self.ui.radioButton_rand_squad))

    def timer(self):
        self.hide()

        self.timer_window.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}timer.ico"))
        self.timer_window.ui.pushButton_clear.click()
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
        self.btn_clear_labels()

        self.random_element = choice(self.list_element_img)

        pixmap = QPixmap(f'{self.path_dir_element + self.random_element}')
        pixmap = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.label_img_element.setPixmap(pixmap)
        self.ui.label_img_element.setStyleSheet(self.change_border_color_label_with_elem(self.random_element[:self.random_element.rindex('.')]))

    def btn_random_character(self):
        path_dir_element_characters = proverka_or_create_dir_data(self.path_dir_elements_character,
                                                                  self.random_element[:self.random_element.rindex('.')],
                                                                  '')

        list_element_characters_img = listdir(path_dir_element_characters)

        random_element_character = choice(list_element_characters_img)

        pixmap = QPixmap(f'{path_dir_element_characters + random_element_character}')

        self.ui.label_img_charact.setPixmap(pixmap)
        self.ui.label_name_charact.setText(self.dict_all_name_characters.get(random_element_character[:random_element_character.rindex('.')],
                                                                             random_element_character[:random_element_character.rindex('.')]))
        self.ui.label_img_charact.setStyleSheet(self.change_border_color_label_with_elem(self.random_element[:self.random_element.rindex('.')]))
        self.ui.label_name_charact.setStyleSheet(self.change_border_color_label_with_elem(self.random_element[:self.random_element.rindex('.')]))

    def btn_random_squad(self):
        dict_element_and_characters = {}

        for elem in self.list_element_img:
            path_dir_element_characters = proverka_or_create_dir_data(self.path_dir_elements_character,
                                                                      elem[:elem.rindex('.')],
                                                                      '')
            dict_element_and_characters[elem[:elem.rindex('.')]] = listdir(path_dir_element_characters)

        for num_lab in range(1, 5):
            random_element = choice(self.list_element_img)
            random_element = random_element[:random_element.rindex('.')]

            path_dir_rand_elem_with_charact = proverka_or_create_dir_data(self.path_dir_elements_character,
                                                                          random_element,
                                                                          '')

            list_characters_in_elem = dict_element_and_characters.get(random_element)

            random_charact = list_characters_in_elem.pop(randrange(len(list_characters_in_elem)))

            dict_element_and_characters[random_element] = list_characters_in_elem

            pixmap = QPixmap(f'{path_dir_rand_elem_with_charact + random_charact}')

            eval(f"self.ui.label_img_charact_squad_{str(num_lab)}.setPixmap(QPixmap(pixmap))")
            eval(f"self.ui.label_img_charact_squad_{str(num_lab)}.setStyleSheet(self.change_border_color_label_with_elem(random_element))")
            eval(f"self.ui.label_name_charact_squad_{str(num_lab)}.setText(self.dict_all_name_characters.get(random_charact[:random_charact.rindex('.')],\
                                                                                         random_charact[:random_charact.rindex('.')]))")
            eval(f"self.ui.label_name_charact_squad_{str(num_lab)}.setStyleSheet(self.change_border_color_label_with_elem(random_element))")

            QApplication.processEvents()
            sleep(2)

    def btn_state(self, btn):
        if btn.isChecked() and btn.objectName() == "radioButton_rand_elem_charact":
            self.setFixedWidth(360)
            self.setFixedHeight(470)

            self.ui.groupBox_2.setEnabled(True)
            self.ui.groupBox_2.show()

            self.ui.groupBox_3.setEnabled(False)
            self.ui.groupBox_3.hide()

        if btn.isChecked() and btn.objectName() == "radioButton_rand_squad":
            self.setFixedWidth(748)
            self.setFixedHeight(514)

            self.ui.groupBox_3.setEnabled(True)
            self.ui.groupBox_3.show()

            self.ui.groupBox_2.setEnabled(False)
            self.ui.groupBox_2.hide()

    def change_border_color_label_with_elem(self, element):
        if element == 'anemo':
            return 'border: 2px solid #37dba4; color: #37dba4;'
        elif element == 'cryo':
            return 'border: 1px solid #65e1ea; color: #65e1ea;'
        elif element == 'dendro':
            return 'border: 1px solid #8ac500; color: #8ac500;'
        elif element == 'electro':
            return 'border: 1px solid #c97bfe; color: #c97bfe;'
        elif element == 'geo':
            return 'border: 1px solid #f8a300; color: #f8a300;'
        elif element == 'hydro':
            return 'border: 1px solid #08e4ff; color: #08e4ff;'
        elif element == 'pyro':
            return 'border: 1px solid #ef5f02; color: #ef5f02;'
        else:
            return 'border: none;'

    def reload_exist(self):
        self.exists_dir('Data')

    def exists_dir(self, name_dir):
        path_dir = proverka_path_dir_icon(name_dir)
        self.list_dirs_in_data = listdir(path_dir)

        if path_to_dir(name_dir) and len(self.list_dirs_in_data) != 0:
            self.path_to_data = proverka_or_create_dir_data()
            self.path_dir_element = proverka_or_create_dir_data(self.path_to_data, 'element', '')
            self.path_dir_elements_character = proverka_or_create_dir_data(self.path_to_data, 'elements_characters', '')

            self.list_element_img = listdir(self.path_dir_element)

            if path_to_file(self.path_to_data, 'Name characters'):
                self.dict_all_name_characters = read_file('Name characters', self.path_to_data)
            else:
                self.dict_all_name_characters = {}

            self.ui.label_info_folder.setText("Дані знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #00FF00;")

            self.ui.pushButton_rand_charact.setEnabled(True)
            self.ui.pushButton_rand_elem.setEnabled(True)
            self.ui.pushButton_clear.setEnabled(True)
            self.ui.pushButton_clear_2.setEnabled(True)
            self.ui.pushButton_rand_squad.setEnabled(True)

            self.ui.pushButton_download_data.setText("Оновити\nдані")

        else:
            self.ui.label_info_folder.setText("Дані не знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #FF0000;")

            self.ui.pushButton_rand_charact.setEnabled(False)
            self.ui.pushButton_rand_squad.setEnabled(False)
            self.ui.pushButton_rand_elem.setEnabled(False)
            self.ui.pushButton_clear.setEnabled(False)
            self.ui.pushButton_clear_2.setEnabled(False)

            self.ui.pushButton_download_data.setText("Завантажити\nдані")

    def btn_clear_labels(self):
        self.ui.label_img_charact.clear()
        self.ui.label_img_charact.setStyleSheet(self.change_border_color_label_with_elem(''))
        self.ui.label_img_element.clear()
        self.ui.label_img_element.setStyleSheet(self.change_border_color_label_with_elem(''))
        self.ui.label_name_charact.clear()
        self.ui.label_name_charact.setStyleSheet(self.change_border_color_label_with_elem(''))

        for num_lab in range(1, 5):
            eval(f"self.ui.label_img_charact_squad_{str(num_lab)}.clear()")
            eval(f"self.ui.label_name_charact_squad_{str(num_lab)}.clear()")
            eval(f"self.ui.label_img_charact_squad_{str(num_lab)}.setStyleSheet(self.change_border_color_label_with_elem(''))")
            eval(f"self.ui.label_name_charact_squad_{str(num_lab)}.setStyleSheet(self.change_border_color_label_with_elem(''))")

    def btn_app_exit(self):
        self.exit_app()

    def exit_app(self):
        QApplication.instance().quit()