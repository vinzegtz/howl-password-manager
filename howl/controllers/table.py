from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from ..models.password import PasswordModel


'''
Passwords table controller
'''
class TableController:
    
    def __init__(self, view):
        self.view = view
        self.tblPasswords = view.tblPasswords

        self.passwordModel = PasswordModel()
        self.selectedCell = None

        self.createDatabaseIfNotExists()
        self.loadTableInfo()

    
    def createDatabaseIfNotExists(self):
        if not path.exists(self.passwordModel.databasePath):
            print('Create database and tables')
            self.passwordModel.createTable()
        
        print('Database ininitalized')

    def loadTableInfo(self):
        rows = self.getTableItems()

        self.view.setTableLabels()
        self.tblPasswords.setRowCount(len(rows))

        for x, row in enumerate(rows):
            for y, item in enumerate(row):
                self.tblPasswords.setItem(x, y, item)

        self.tblPasswords.itemDoubleClicked.connect(lambda : print('double click'))
        self.tblPasswords.itemClicked.connect(self.setSelectedCell)

    def getTableItems(self):
        passwords = self.passwordModel.getAll()
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
    
    def setSelectedCell(self, item):
        self.selectedCell = (item.row(), item.column())