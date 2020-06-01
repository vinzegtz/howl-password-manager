import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class HowlPasswordManagerController:
    
    def __init__(self, view):
        self.__view = view
        self.__connectSignals()
    
    def __connectSignals(self):
        self.__view.btnGeneratePass.clicked.connect(lambda :self.__setRandomText())
    
    def __setRandomText(self):
        self.__view.txtPassword.setText('Hello World!')
        self.__view.txtPassword.setFocus()


# Howl Password Manager GUI
class HowlPasswordManager(QMainWindow):

    wgtCentral = None

    def __init__(self):
        super().__init__()

        # Main window properties
        self.setWindowTitle('Howl Password Manager')
        self.setFixedSize(640, 360)

        # Central widget and general layout
        self.lytGeneral = QVBoxLayout()
        self.wgtCentral = QWidget(self)
        
        self.lytGeneral.setAlignment(Qt.AlignTop)
        self.wgtCentral.setLayout(self.lytGeneral)
        self.setCentralWidget(self.wgtCentral)

        # Create GUI
        self.__createHeader()
        self.__createMainInput()
    
    def __createHeader(self):
        self.lytHeader = QVBoxLayout()
        self.lblMainTitle = QLabel()

        # Set title properties
        self.lblMainTitle.setText('<h1>Howl Password Manager</h1>')

        # Add widgets to the header layout
        self.lytHeader.addWidget(self.lblMainTitle)

        # Set layout properties
        # self.lytHeader.setAlignment(Qt.AlignTop)

        # Add widgets to the general layout
        self.lytGeneral.addLayout(self.lytHeader)

    def __createMainInput(self):
        self.lytGeneratePass = QHBoxLayout()
        self.txtPassword = QLineEdit()
        self.btnGeneratePass = QPushButton()
        self.btnCopyPass = QPushButton()

        # Set button properties
        self.btnGeneratePass.setText('Generate')
        self.btnCopyPass.setText('Copy')

        # Set input properties
        self.txtPassword.setReadOnly(True)

        # Add widgets to the main input layout
        self.lytGeneratePass.addWidget(self.btnGeneratePass)
        self.lytGeneratePass.addWidget(self.txtPassword)
        self.lytGeneratePass.addWidget(self.btnCopyPass)

        # Set layout properties
        # self.lytGeneratePass.setAlignment(Qt.AlignTop)

        # Add widgets to the general layout
        self.lytGeneral.addLayout(self.lytGeneratePass)


# Client
def main():
    # QApplication instance
    howl = QApplication(sys.argv)

    # Show main window
    mainView = HowlPasswordManager()
    mainView.show()

    # Set view in the controller
    HowlPasswordManagerController(view=mainView)

    # Main loop
    sys.exit(howl.exec())


if __name__ == '__main__':
    main()