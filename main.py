from sys import exit, argv

from PyQt6.QtWidgets import QApplication

from Main_GUI import MainWindow

from Parser_data import Parser_data

def main():
    # pars_data = Parser_data('https://paimon.moe/characters')
    #
    # pars_data.pars_data()

    app = QApplication(argv)

    appl = MainWindow()
    appl.show()

    exit(app.exec())

if __name__ == "__main__":
    main()