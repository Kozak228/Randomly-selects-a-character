# Form implementation generated from reading ui file 'timer_GUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 261)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Img_app/timer.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #1E1E1E;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 1px solid #B8860B;\n"
"    color: yellow;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"  color: #00FF00;    \n"
"  background-color: #2F4F4F;\n"
"  selection-background-color: #00FA9A;\n"
"  selection-color: #800000;\n"
"}\n"
"QComboBox:disabled{\n"
"    color: #800000;\n"
"    border-color: #800000;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: black;\n"
"    color: yellow;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px dashed #00FA9A;\n"
"    color: #00FA9A;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #2F4F4F;\n"
"    color: #FF0000;\n"
"    border: 1px dashed #000080;\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: black;\n"
"    color: #800000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #FF4500;\n"
"}\n"
"QLabel:disabled{\n"
"    color: #800000;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    backgrond-color: #696969;\n"
"    color: #7FFF00;\n"
"    border: 1px solid #0000CD;\n"
"}\n"
"QGroupBox:disabled{\n"
"    color: #800000;\n"
"    border-color: 800000;\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: #FF4500;\n"
"}\n"
"QRadioButton:hover{\n"
"    color: #00FF00;\n"
"}\n"
"QRadioButton:pressed{\n"
"    background-color: #2F4F4F;\n"
"    color: #FF0000;\n"
"    border: 1px dashed #000080;\n"
"}\n"
"QRadioButton:disabled{\n"
"    color: #800000;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 230, 97))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_m = QtWidgets.QLabel(self.groupBox)
        self.label_m.setGeometry(QtCore.QRect(12, 16, 94, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_m.setFont(font)
        self.label_m.setStyleSheet("color: yellow;")
        self.label_m.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_m.setObjectName("label_m")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(118, 9, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(23, 68, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(148, 68, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_s = QtWidgets.QLabel(self.groupBox)
        self.label_s.setGeometry(QtCore.QRect(150, 18, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_s.setFont(font)
        self.label_s.setStyleSheet("color: yellow;")
        self.label_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_s.setObjectName("label_s")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(330, 63, 84, 38))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 110, 405, 143))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_add_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_10.setGeometry(QtCore.QRect(170, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_10.setFont(font)
        self.pushButton_add_10.setObjectName("pushButton_add_10")
        self.pushButton_add_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_1.setGeometry(QtCore.QRect(10, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_1.setFont(font)
        self.pushButton_add_1.setObjectName("pushButton_add_1")
        self.pushButton_add_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_5.setGeometry(QtCore.QRect(90, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_5.setFont(font)
        self.pushButton_add_5.setObjectName("pushButton_add_5")
        self.pushButton_add_30 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_30.setGeometry(QtCore.QRect(330, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_30.setFont(font)
        self.pushButton_add_30.setObjectName("pushButton_add_30")
        self.pushButton_add_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_20.setGeometry(QtCore.QRect(250, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_20.setFont(font)
        self.pushButton_add_20.setObjectName("pushButton_add_20")
        self.radioButton_s = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_s.setGeometry(QtCore.QRect(200, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_s.setFont(font)
        self.radioButton_s.setChecked(True)
        self.radioButton_s.setObjectName("radioButton_s")
        self.radioButton_m = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_m.setGeometry(QtCore.QRect(200, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_m.setFont(font)
        self.radioButton_m.setObjectName("radioButton_m")
        self.comboBox_action_time = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_action_time.setGeometry(QtCore.QRect(35, 112, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_action_time.setFont(font)
        self.comboBox_action_time.setObjectName("comboBox_action_time")
        self.comboBox_action_time.addItem("")
        self.comboBox_action_time.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_FAQ_add = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_FAQ_add.setGeometry(QtCore.QRect(370, 80, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_FAQ_add.setFont(font)
        self.pushButton_FAQ_add.setObjectName("pushButton_FAQ_add")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(250, 10, 46, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Img_app/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setIconSize(QtCore.QSize(39, 90))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(250, 60, 48, 43))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Img_app/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_clear.setIcon(icon2)
        self.pushButton_clear.setIconSize(QtCore.QSize(39, 91))
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.label_m.setText(_translate("MainWindow", "00"))
        self.label_5.setText(_translate("MainWindow", ":"))
        self.label_7.setText(_translate("MainWindow", "Хвилини"))
        self.label_8.setText(_translate("MainWindow", "Секунди"))
        self.label_s.setText(_translate("MainWindow", "00"))
        self.pushButton_exit.setText(_translate("MainWindow", "Повернуться\n"
"на головну"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Додати / Відняти час"))
        self.pushButton_add_10.setText(_translate("MainWindow", "10"))
        self.pushButton_add_1.setText(_translate("MainWindow", "1"))
        self.pushButton_add_5.setText(_translate("MainWindow", "5"))
        self.pushButton_add_30.setText(_translate("MainWindow", "30"))
        self.pushButton_add_20.setText(_translate("MainWindow", "20"))
        self.radioButton_s.setText(_translate("MainWindow", "Секунди"))
        self.radioButton_m.setText(_translate("MainWindow", "Хвилини"))
        self.comboBox_action_time.setItemText(0, _translate("MainWindow", "Додати"))
        self.comboBox_action_time.setItemText(1, _translate("MainWindow", "Відняти"))
        self.label.setText(_translate("MainWindow", "Виберіть, що зробити з часом:"))
        self.pushButton_FAQ_add.setText(_translate("MainWindow", "?"))
