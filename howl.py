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
        self.__view.generateButton.clicked.connect(lambda :self.__setRandomText())
    
    def __setRandomText(self):
        self.__view.passwordInput.setText('Hello World!')
        self.__view.passwordInput.setFocus()


# Howl Password Manager GUI
class HowlPasswordManager(QMainWindow):

    centralWidget = None

    def __init__(self):
        super().__init__()

        # Main window properties
        self.setWindowTitle('Howl Password Manager')
        self.setFixedSize(640, 360)

        # Central widget and general layout
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        
        self.generalLayout.setAlignment(Qt.AlignTop)
        self.centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self.centralWidget)

        # Create GUI
        self.__createHeader()
        self.__createMainInput()
    
    def __createHeader(self):
        self.headerLayout = QVBoxLayout()
        self.mainTitle = QLabel()

        # Set title properties
        self.mainTitle.setText('<h1>Howl Password Manager</h1>')

        # Add widgets to the header layout
        self.headerLayout.addWidget(self.mainTitle)

        # Set layout properties
        # self.headerLayout.setAlignment(Qt.AlignTop)

        # Add widgets to the general layout
        self.generalLayout.addLayout(self.headerLayout)

    def __createMainInput(self):
        self.generatePasswordLayout = QHBoxLayout()
        self.passwordInput = QLineEdit()
        self.generateButton = QPushButton()
        self.copyButton = QPushButton()

        # Set button properties
        self.generateButton.setText('Generate')
        self.copyButton.setText('Copy')

        # Set input properties
        self.passwordInput.setReadOnly(True)

        # Add widgets to the main input layout
        self.generatePasswordLayout.addWidget(self.generateButton)
        self.generatePasswordLayout.addWidget(self.passwordInput)
        self.generatePasswordLayout.addWidget(self.copyButton)

        # Set layout properties
        # self.generatePasswordLayout.setAlignment(Qt.AlignTop)

        # Add widgets to the general layout
        self.generalLayout.addLayout(self.generatePasswordLayout)


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