from sys import exit, argv

from PyQt6.QtWidgets import QApplication

from Main_GUI import MainWindow

def main():
    app = QApplication(argv)

    appl = MainWindow()
    appl.show()

    exit(app.exec())


if __name__ == "__main__":
    main()