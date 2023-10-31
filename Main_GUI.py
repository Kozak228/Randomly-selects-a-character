from os import listdir
from random import choice

from GUI.main_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

from Create_and_remove_forders import path_to_dir, proverka_or_create_dir_data, proverka_path_dir_icon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.BypassWindowManagerHint)
        self.setFixedSize(409, 291)

        self.setWindowIcon(QIcon(f"{proverka_path_dir_icon('img_app')}main_app.png"))

        self.reload_exist()

        self.ui.pushButton_rand_elem.clicked.connect(self.btn_random_element)
        self.ui.pushButton_rand_charact.clicked.connect(self.btn_random_character)
        self.ui.pushButton_clear.clicked.connect(self.btn_clear_labels)
        self.ui.pushButton_download_data.clicked.connect(self.download_data)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)

    def download_data(self):
        pass

    def btn_random_element(self):
        self.random_element = choice(self.list_element_img)

        pixmap = QPixmap(f'{self.path_dir_element + self.random_element}')
        pixmap = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.label_img_element.setPixmap(pixmap)

    def btn_random_character(self):
        path_dir_element_characters = proverka_or_create_dir_data(self.path_to_data,
                                                                  self.random_element[:self.random_element.rindex('.')],
                                                                  '')

        list_element_characters_img = listdir(path_dir_element_characters)

        random_element_character = choice(list_element_characters_img)

        pixmap = QPixmap(f'{path_dir_element_characters + random_element_character}')

        self.ui.label_img_charact.setPixmap(pixmap)

    def reload_exist(self):
        self.path_pulling()
        self.exists_dir('Data')

    def path_pulling(self):
        if path_to_dir('Data'):
            self.path_to_data = proverka_or_create_dir_data()
            self.path_dir_element = proverka_or_create_dir_data(self.path_to_data, 'element', '')

            self.list_element_img = listdir(self.path_dir_element)

    def exists_dir(self, name_dir):
        if path_to_dir(name_dir):
            self.ui.label_info_folder.setText("Папку з даними знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #00FF00;")

            self.ui.pushButton_rand_charact.setEnabled(True)
            self.ui.pushButton_rand_elem.setEnabled(True)

            self.ui.pushButton_download_data.setText("Оновити\nдані")
        else:
            self.ui.label_info_folder.setText("Папку з даними не знайдено.")
            self.ui.label_info_folder.setStyleSheet("color: #FF0000;")

            self.ui.pushButton_rand_charact.setEnabled(False)
            self.ui.pushButton_rand_elem.setEnabled(False)

            self.ui.pushButton_download_data.setText("Завантажити\nдані")

    def btn_clear_labels(self):
        self.ui.label_img_charact.clear()
        self.ui.label_img_element.clear()

    def btn_app_exit(self):
        self.exit_app()

    def exit_app(self):
        QApplication.instance().quit
        exit()