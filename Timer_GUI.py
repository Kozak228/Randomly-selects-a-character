from GUI.timer_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon

from pyglet import media

from Time_format import add_zero, m_in_s, s_in_m
from Create_and_remove_forders import proverka_path_dir_icon

class Timers(QMainWindow):
    def __init__(self):
        super(Timers, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(420, 261)

        self.ui.pushButton_play.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}play.png"))
        self.ui.pushButton_clear.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}clear.png"))

        self.audio = media.load(f"{proverka_path_dir_icon('audio')}audio.wav", streaming=False)

        self.ui.pushButton_clear.clicked.connect(self.reset_time)
        self.ui.pushButton_FAQ_add.clicked.connect(self.msg_FAQ_action)
        self.ui.pushButton_add_1.clicked.connect(self.click_btn_add_1)
        self.ui.pushButton_add_5.clicked.connect(self.click_btn_add_5)
        self.ui.pushButton_add_10.clicked.connect(self.click_btn_add_10)
        self.ui.pushButton_add_20.clicked.connect(self.click_btn_add_20)
        self.ui.pushButton_add_30.clicked.connect(self.click_btn_add_30)
        self.ui.pushButton_play.clicked.connect(self.start_timer)

    def start_timer(self):
        if self.ui.pushButton_clear.isEnabled():
            if (int(self.ui.label_m.text()) == 0 and int(self.ui.label_s.text()) != 0) or (int(self.ui.label_m.text()) != 0 and int(self.ui.label_s.text()) == 0):
                self.setting_and_start_timer()
            else:
                self.msg('Error', 'Не введено час зворотного відліку.')

        else:
            self.pause_timer()

    def setting_and_start_timer(self):
        self.group_off_elem(False)

        self.ui.pushButton_play.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}pause.png"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_timer)
        self.timer.start(1000)

    def pause_timer(self):
        self.timer.stop()

        self.group_off_elem(True)
        self.ui.pushButton_play.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}play.png"))

    def show_timer(self):
        m = int(self.ui.label_m.text())
        s = int(self.ui.label_s.text())

        if 0 <= s <= 30 and m == 0:
            self.ui.label_s.setStyleSheet("color: red;")
            self.ui.label_m.setStyleSheet("color: red;")

        if s <= 0 and m <= 0:
            self.timer.stop()

            self.group_off_elem(True)

            self.ui.pushButton_play.setIcon(QIcon(f"{proverka_path_dir_icon('img_app')}play.png"))

            self.audio.play()

            self.ui.label_s.setStyleSheet("color: yellow;")
            self.ui.label_m.setStyleSheet("color: yellow;")

            self.ui.pushButton_exit.click()

        else:
            all_sec = m_in_s(m, s)
            all_sec -= 1
            s, m = s_in_m(all_sec)

            self.ui.label_s.setText(str(add_zero(s)))
            self.ui.label_m.setText(str(add_zero(m)))

    def change_time(self, elem_name_btn):
        if self.ui.radioButton_s.isChecked():
            if self.ui.comboBox_action_time.currentText() == "Додати":
                self.change_on_time("s", int(elem_name_btn[elem_name_btn.rindex("_") + 1:]), "Додати")
            else:
                self.change_on_time("s", int(elem_name_btn[elem_name_btn.rindex("_") + 1:]), "Відняти")

        if self.ui.radioButton_m.isChecked():
            if self.ui.comboBox_action_time.currentText() == "Додати":
                self.change_on_time("m", int(elem_name_btn[elem_name_btn.rindex("_") + 1:]), "Додати")
            else:
                self.change_on_time("m", int(elem_name_btn[elem_name_btn.rindex("_") + 1:]), "Відняти")

    def change_on_time(self, change_time, add_or_vicht_time, operation):
        if operation == "Додати":
            elem_value = int(eval(f"self.ui.label_{change_time}.text()"))
            summ = elem_value + add_or_vicht_time

            if change_time == 's':
                eval(f"self.ui.label_{change_time}.setText(str(add_zero({summ})))") if summ < 60 else eval(
                    f'self.ui.label_{change_time}.setText("00")')
            else:
                eval(f"self.ui.label_{change_time}.setText(str(add_zero({summ})))")

        else:
            elem_value = int(eval(f"self.ui.label_{change_time}.text()"))
            summ = elem_value - add_or_vicht_time

            eval(f'self.ui.label_{change_time}.setText("00")') if summ < 0 else eval(
                f"self.ui.label_{change_time}.setText(str(add_zero({summ})))")

    def click_btn_add_1(self):
        self.change_time(self.ui.pushButton_add_1.objectName())

    def click_btn_add_5(self):
        self.change_time(self.ui.pushButton_add_5.objectName())

    def click_btn_add_10(self):
        self.change_time(self.ui.pushButton_add_10.objectName())

    def click_btn_add_20(self):
        self.change_time(self.ui.pushButton_add_20.objectName())

    def click_btn_add_30(self):
        self.change_time(self.ui.pushButton_add_30.objectName())

    def group_off_elem(self, boolean):
        self.ui.groupBox_2.setEnabled(boolean)
        self.ui.pushButton_clear.setEnabled(boolean)
        self.ui.pushButton_exit.setEnabled(boolean)

    def reset_time(self):
        self.ui.label_m.setText("00")
        self.ui.label_s.setText("00")

        self.ui.label_s.setStyleSheet("color: yellow;")
        self.ui.label_m.setStyleSheet("color: yellow;")

    def msg_FAQ_action(self):
        self.msg("Information", "Ви можете додати до (або відняти від) хвилин(и) або секунд(и)\nвідповідне значення,"  
                                                " натиснувши на кнопки з цифрами.")

    def msg(self, rison, message):
        msg = QMessageBox()
        if rison == "Error": 
            msg.setWindowTitle(rison)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if rison == "Information":
            msg.setWindowTitle(rison)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()