from mypassword import Password, PasswordLevel
from os import path
from PyQt5.QtCore import Qt
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

    def __createDatabaseIfNotExists(self):
        model = DB.getInstance()

        if not path.exists(model.databaseName):
            print('Create database and tables')
            model.createPasswordsTable()
        
        print('Database ininitalized')