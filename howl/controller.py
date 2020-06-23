from mypassword import Password, PasswordLevel
from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTableWidgetItem

from .model import DB


# Class to manage the logic and flow of the main window
class Manager:
    def __init__(self, view, application):
        self.__view = view
        self.__application = application
        self.__clipBoard = application.clipboard()

        self.__createDatabaseIfNotExists()

        self.__connectSignals()
        self.__loadTableInfo()
    
    def __connectSignals(self):
        self.__view.btnGeneratePass.clicked.connect(lambda :self.__generatePassword())
        self.__view.btnCopyPass.clicked.connect(lambda :self.__copyPassword())

        self.__view.menuItemFile.triggered[QAction].connect(self.__clickFileActions)
        self.__view.menuItemEdit.triggered[QAction].connect(self.__click)
        self.__view.menuItemHelp.triggered[QAction].connect(self.__click)
    
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
    
    def __doubleClick(self, item):
        columnName = self.__view.tblPasswords.horizontalHeaderItem(item.column()).text()
        print(f'double click for {columnName}')
    
    def __click(self, action):
        print(f'Trigger for {action.text()}')

    def __clickFileActions(self, action):
        if action.text() == 'New password':
            password = Password(length=32, level=PasswordLevel.FOUR)

            self.__view.windowPasswordForm.cleanForm()
            self.__view.windowPasswordForm.txtPassword.setText(password.password)
            self.__view.windowPasswordForm.show()

    def __loadTableInfo(self):
        rows = self.__getTableItems()
        
        self.__view.tblPasswords.setRowCount(len(rows))

        for x, row in enumerate(rows):
            for y, item in enumerate(row):
                self.__view.tblPasswords.setItem(x, y, item)

        self.__view.tblPasswords.itemDoubleClicked.connect(self.__doubleClick)
    
    def __getTableItems(self):
        instance = DB.getInstance()
        passwords = instance.getAllPasswords()
        tableRows = []

        for password in passwords:
            tableRow = []

            tableItemService = QTableWidgetItem(password[1])
            tableItemWebsite = QTableWidgetItem(password[2])
            tableItemDescription = QTableWidgetItem(password[3])
            tableItemUser = QTableWidgetItem(password[4])
            tableItemPassword = QTableWidgetItem(password[5])
            tableItemKeyName = QTableWidgetItem(password[6])
            
            tableItemService.setFlags(Qt.ItemIsEnabled)
            tableItemWebsite.setFlags(Qt.ItemIsEnabled)
            tableItemDescription.setFlags(Qt.ItemIsEnabled)
            tableItemUser.setFlags(Qt.ItemIsEnabled)
            tableItemPassword.setFlags(Qt.ItemIsEnabled)
            tableItemKeyName.setFlags(Qt.ItemIsEnabled)

            tableRow.append(tableItemService)
            tableRow.append(tableItemWebsite)
            tableRow.append(tableItemDescription)
            tableRow.append(tableItemUser)
            tableRow.append(tableItemPassword)
            tableRow.append(tableItemKeyName)

            tableRows.append(tuple(tableRow))
        
        return tableRows

    def __createDatabaseIfNotExists(self):
        model = DB.getInstance()

        if not path.exists(model.databasePath):
            print('Create database and tables')
            model.createPasswordsTable()
        
        print('Database ininitalized')