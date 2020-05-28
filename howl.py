import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


# Howl Password Manager GUI
class HowlPasswordManager(QMainWindow):

    __centralWidget = None

    def __init__(self):
        super().__init__()

        # Main window properties
        self.setWindowTitle('Howl Password Manager')
        self.setFixedSize(640, 360)

        # Cental widget
        self.__centralWidget = QWidget(self)
        self.setCentralWidget(self.__centralWidget)


# Client
def main():
    # QApplication instance
    howl = QApplication(sys.argv)

    # Show main window
    mainView = HowlPasswordManager()
    mainView.show()

    # Main loop
    sys.exit(howl.exec())


if __name__ == '__main__':
    main()