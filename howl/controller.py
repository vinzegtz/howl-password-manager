from mypassword import Password, PasswordLevel
from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTableWidgetItem

from .model import DB


# Class to manage the logic and flow of the main window
class Manager:
    def __init__(self, view, application):
        self.selectedCell = None

        self.__view = view
        self.__application = application
        self.__clipBoard = application.clipboard()

        self.__createDatabaseIfNotExists()

        self.__connectSignals()
        self.__loadTableInfo()
    
    def __connectSignals(self):
        # Main window
        self.__view.btnGeneratePass.clicked.connect(lambda :self.__generatePassword())
        self.__view.btnCopyPass.clicked.connect(lambda :self.__copyPassword())

        # Menu
        self.__view.menuItemFile.triggered[QAction].connect(self.__clickFileActions)
        self.__view.menuItemEdit.triggered[QAction].connect(self.__clickEditActions)
        self.__view.menuItemHelp.triggered[QAction].connect(self.__click)

        # Form
        self.__view.windowPasswordForm.btnSave.clicked.connect(self.__savePassword)
        self.__view.windowPasswordForm.btnUpdate.clicked.connect(self.__updatePassword)

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

    def __setSelectedCell(self, item):
        self.selectedCell = (item.row(), item.column())

    def __clickFileActions(self, action):
        if action.text() == 'New password':
            password = Password(length=32, level=PasswordLevel.FOUR)

            self.__view.windowPasswordForm.cleanForm()
            self.__view.windowPasswordForm.txtPassword.setText(password.password)
            self.__view.windowPasswordForm.btnUpdate.hide()
            self.__view.windowPasswordForm.btnSave.show()
            self.__view.windowPasswordForm.show()

    def __clickEditActions(self, action):
        if action.text() == 'Edit password' and self.selectedCell != None:
            model = DB.getInstance()
            keyName = self.__view.tblPasswords.item(self.selectedCell[0], 5).text()

            password = model.getPasswordByKeyName(keyName)
            self.__view.windowPasswordForm.fillForm(password)
            self.__view.windowPasswordForm.btnUpdate.show()
            self.__view.windowPasswordForm.btnSave.hide()
            self.__view.windowPasswordForm.show()
        elif action.text() == 'Delete password' and self.selectedCell != None:
            model = DB.getInstance()
            keyName = self.__view.tblPasswords.item(self.selectedCell[0], 5).text()
            self.__deletePassword(keyName)

    def __loadTableInfo(self):
        rows = self.__getTableItems()
        
        self.__view.tblPasswords.setRowCount(len(rows))

        for x, row in enumerate(rows):
            for y, item in enumerate(row):
                self.__view.tblPasswords.setItem(x, y, item)

        self.__view.tblPasswords.itemDoubleClicked.connect(self.__doubleClick)
        self.__view.tblPasswords.itemClicked.connect(self.__setSelectedCell)
        
    def __getTableItems(self):
        model = DB.getInstance()
        passwords = model.getAllPasswords()
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

    def __savePassword(self):
        password = (
            self.__view.windowPasswordForm.txtService.text(),
            self.__view.windowPasswordForm.txtWebsite.text(),
            self.__view.windowPasswordForm.txtDescription.text(),
            self.__view.windowPasswordForm.txtUser.text(),
            self.__view.windowPasswordForm.txtPassword.text(),
            self.__view.windowPasswordForm.txtKeyname.text(),
        )

        model = DB.getInstance()
        model.savePassword(password)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
        self.__view.windowPasswordForm.close()
    
    def __updatePassword(self):
        password = (
            self.__view.windowPasswordForm.txtService.text(),
            self.__view.windowPasswordForm.txtWebsite.text(),
            self.__view.windowPasswordForm.txtDescription.text(),
            self.__view.windowPasswordForm.txtUser.text(),
            self.__view.windowPasswordForm.txtPassword.text(),
            self.__view.windowPasswordForm.txtKeyname.text(),
            self.__view.windowPasswordForm.txtKeyname.text(), # Where condition
        )

        model = DB.getInstance()
        model.updatePassword(password)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
        self.__view.windowPasswordForm.close()
    
    def __deletePassword(self, keyName):
        model = DB.getInstance()
        model.deletePasswordByKeyName(keyName)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
