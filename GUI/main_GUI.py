# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Img_app/main_app.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 214, 74))
        self.groupBox.setObjectName("groupBox")
        self.label_info_folder = QtWidgets.QLabel(self.groupBox)
        self.label_info_folder.setGeometry(QtCore.QRect(10, 20, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_info_folder.setFont(font)
        self.label_info_folder.setText("")
        self.label_info_folder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_folder.setWordWrap(True)
        self.label_info_folder.setObjectName("label_info_folder")
        self.pushButton_download_data = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_download_data.setGeometry(QtCore.QRect(121, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_download_data.setFont(font)
        self.pushButton_download_data.setObjectName("pushButton_download_data")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 342, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_img_charact = QtWidgets.QLabel(self.groupBox_2)
        self.label_img_charact.setGeometry(QtCore.QRect(166, 61, 170, 131))
        self.label_img_charact.setStyleSheet("")
        self.label_img_charact.setText("")
        self.label_img_charact.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_img_charact.setObjectName("label_img_charact")
        self.label_img_element = QtWidgets.QLabel(self.groupBox_2)
        self.label_img_element.setGeometry(QtCore.QRect(7, 61, 150, 131))
        self.label_img_element.setStyleSheet("")
        self.label_img_element.setText("")
        self.label_img_element.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_img_element.setObjectName("label_img_element")
        self.pushButton_rand_elem = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rand_elem.setGeometry(QtCore.QRect(32, 18, 101, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_rand_elem.setFont(font)
        self.pushButton_rand_elem.setObjectName("pushButton_rand_elem")
        self.pushButton_rand_charact = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rand_charact.setGeometry(QtCore.QRect(212, 17, 101, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_rand_charact.setFont(font)
        self.pushButton_rand_charact.setObjectName("pushButton_rand_charact")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear.setGeometry(QtCore.QRect(148, 20, 48, 34))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Img_app/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_clear.setIcon(icon1)
        self.pushButton_clear.setIconSize(QtCore.QSize(31, 76))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(253, 54, 59, 32))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_timer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_timer.setGeometry(QtCore.QRect(252, 12, 59, 32))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_timer.setFont(font)
        self.pushButton_timer.setObjectName("pushButton_timer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random character selection"))
        self.groupBox.setTitle(_translate("MainWindow", "Інформація про папку"))
        self.pushButton_download_data.setText(_translate("MainWindow", "Завантажити\n"
"дані"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Рандомний елемент та персонаж"))
        self.pushButton_rand_elem.setText(_translate("MainWindow", "Зарандомити\n"
"елемент "))
        self.pushButton_rand_charact.setText(_translate("MainWindow", "Зарандомити\n"
"персонажа"))
        self.pushButton_exit.setText(_translate("MainWindow", "Вихід"))
        self.pushButton_timer.setText(_translate("MainWindow", "Timer"))
