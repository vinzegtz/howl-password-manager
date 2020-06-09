import sys

from mypassword import Password, PasswordLevel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class HowlPasswordManagerController:
    
    def __init__(self, view, application):
        self.__view = view
        self.__application = application
        self.__clipBoard = application.clipboard()

        self.__connectSignals()
        self.__loadTableInfo()
    
    def __connectSignals(self):
        self.__view.btnGeneratePass.clicked.connect(lambda :self.__generatePassword())
        self.__view.btnCopyPass.clicked.connect(lambda :self.__copyPassword())
    
    def __generatePassword(self):
        password = Password(length=32, level=PasswordLevel.FOUR)

        self.__view.lblCopyMessage.setVisible(False)

        self.__view.txtPassword.setText(password.password)
        self.__view.txtPassword.setFocus()
    
    def __copyPassword(self):
        password = self.__view.txtPassword.text()
        self.__clipBoard.setText(password)

        if not self.__view.lblCopyMessage.isVisible():
            self.__view.lblCopyMessage.setVisible(True)
    
    def __doubleClick(self):
        print('double click')
    
    def __loadTableInfo(self):
        rows = self.__getTableItems()
        
        self.__view.tblPasswords.setRowCount(len(rows))

        for x, row in enumerate(rows):
            for y, item in enumerate(row):
                self.__view.tblPasswords.setItem(x, y, item)

        self.__view.tblPasswords.itemDoubleClicked.connect(lambda :self.__doubleClick())
    
    def __getTableItems(self):
        tableItemService = QTableWidgetItem('Github')
        tableItemWebsite = QTableWidgetItem('https://github.com')
        tableItemDescription = QTableWidgetItem('My projects repo')
        tableItemUser = QTableWidgetItem('mu_username')
        tableItemPassword = QTableWidgetItem('T0dr24#_drof8PL!')
        tableItemKeyName = QTableWidgetItem('red panda')
        
        tableItemService.setFlags(Qt.ItemIsEnabled)
        tableItemWebsite.setFlags(Qt.ItemIsEnabled)
        tableItemDescription.setFlags(Qt.ItemIsEnabled)
        tableItemUser.setFlags(Qt.ItemIsEnabled)
        tableItemPassword.setFlags(Qt.ItemIsEnabled)
        tableItemKeyName.setFlags(Qt.ItemIsEnabled)

        tableRows = []
        tableRow = []
        tableRow.append(tableItemService)
        tableRow.append(tableItemWebsite)
        tableRow.append(tableItemDescription)
        tableRow.append(tableItemUser)
        tableRow.append(tableItemPassword)
        tableRow.append(tableItemKeyName)

        tableRows.append(tuple(tableRow))
        
        return tableRows


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
        self.__createPasswordsTable()
    
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
        self.lytMainInput = QVBoxLayout()
        self.txtPassword = QLineEdit()
        self.btnGeneratePass = QPushButton()
        self.btnCopyPass = QPushButton()
        self.lblCopyMessage = QLabel()

        # Set button properties
        self.btnGeneratePass.setText('Generate')
        self.btnCopyPass.setText('Copy')

        # Set input properties
        self.txtPassword.setReadOnly(True)

        # Set label properties
        self.lblCopyMessage.setText('Copied!')
        self.lblCopyMessage.setAlignment(Qt.AlignRight)
        self.lblCopyMessage.setVisible(False)

        # Add widgets to the main input layout
        self.lytGeneratePass.addWidget(self.btnGeneratePass)
        self.lytGeneratePass.addWidget(self.txtPassword)
        self.lytGeneratePass.addWidget(self.btnCopyPass)

        # Set layout properties
        # self.lytMainInput.setAlignment(Qt.AlignRight)

        # Add widgets to the general layout
        self.lytMainInput.addLayout(self.lytGeneratePass)
        self.lytMainInput.addWidget(self.lblCopyMessage)
        
        self.lytGeneral.addLayout(self.lytMainInput)
    
    def __createPasswordsTable(self):
        tableLabels = (
            'Service',
            'Website',
            'Description',
            'User',
            'Password',
            'Key name'
        )

        self.tblPasswords = QTableWidget()
        # self.tblPasswords.setRowCount(1)
        self.tblPasswords.setColumnCount(6)
        self.tblPasswords.setHorizontalHeaderLabels(tableLabels)

        self.lytGeneral.addWidget(self.tblPasswords)

# Client
def main():
    # QApplication instance
    howl = QApplication(sys.argv)

    # Show main window
    mainView = HowlPasswordManager()
    mainView.show()

    # Set view in the controller
    HowlPasswordManagerController(view=mainView, application=howl)

    # Main loop
    sys.exit(howl.exec())


if __name__ == '__main__':
    main()