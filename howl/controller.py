from mypassword import Password, PasswordLevel
from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTableWidgetItem

from .models.password import PasswordModel


# Class to manage the logic and flow of the main window
class Manager:

    def __init__(self, view, application):
        self.selectedCell = None
        self.passwordModel = PasswordModel()

        self.__view = view
        self.__application = application
        self.__clipBoard = application.clipboard()

        self.__createDatabaseIfNotExists()

        self.__connectSignals()
        self.__loadTableInfo()

    '''
    Main window logic
    '''
    def __connectSignals(self):
        # Main window
        self.__view.btnGeneratePass.clicked.connect(lambda :self.__setRandomPassword())
        self.__view.btnCopyPass.clicked.connect(lambda :self.__copyPasswordToClipboard())

        self.__connectSignalsToolBar()
        self.__connectSignalsPasswordForm()
 
    def __setRandomPassword(self):
        password = Password(length=32, level=PasswordLevel.FOUR)

        self.__view.lblCopyMessage.setVisible(False)
        self.__view.txtPassword.setText(password.password)
        self.__view.txtPassword.setFocus()

    def __copyPasswordToClipboard(self):
        password = self.__view.txtPassword.text()
        self.__clipBoard.setText(password)

        if not self.__view.lblCopyMessage.isVisible():
            self.__view.lblCopyMessage.setVisible(True)

    '''
    Toolbar logic
    '''
    def __connectSignalsToolBar(self):
        self.__view.menuItemFile.triggered[QAction].connect(self.__clickFileActions)
        self.__view.menuItemEdit.triggered[QAction].connect(self.__clickEditActions)
        self.__view.menuItemHelp.triggered[QAction].connect(lambda : print('click'))

    def __clickFileActions(self, action):
        if action.text() == 'New password':
            self.__newPasswordAction()

    def __clickEditActions(self, action):
        if self.selectedCell != None:
            if action.text() == 'Edit password':
                self.__editPasswordAction()
            elif action.text() == 'Delete password':
                self.__deletePasswordAction()
        
        if action.text() == 'Change DB path':
                self.__view.windowDatabasePath.show()

    def __newPasswordAction(self):
        password = Password(length=32, level=PasswordLevel.FOUR)

        self.__view.windowPasswordForm.cleanForm()
        self.__view.windowPasswordForm.txtPassword.setText(password.password)
        self.__view.windowPasswordForm.showForCreate()

    def __editPasswordAction(self):
        keyName = self.__view.tblPasswords.item(self.selectedCell[0], 5).text()
        password = self.passwordModel.getPasswordByKeyName(keyName)
        
        self.__view.windowPasswordForm.fillForm(password)
        self.__view.windowPasswordForm.showForUpdate()

    def __deletePasswordAction(self):
        keyName = self.__view.tblPasswords.item(self.selectedCell[0], 5).text()
            
        self.__deletePasswordInDB(keyName)

    '''
    Password form logic
    '''
    def __connectSignalsPasswordForm(self):
        self.__view.windowPasswordForm.btnSave.clicked.connect(self.__createPasswordInDB)
        self.__view.windowPasswordForm.btnUpdate.clicked.connect(self.__updatePasswordInDB)

    def __createPasswordInDB(self):
        password = (
            self.__view.windowPasswordForm.txtService.text(),
            self.__view.windowPasswordForm.txtWebsite.text(),
            self.__view.windowPasswordForm.txtDescription.text(),
            self.__view.windowPasswordForm.txtUser.text(),
            self.__view.windowPasswordForm.txtPassword.text(),
            self.__view.windowPasswordForm.txtKeyname.text(),
        )

        self.passwordModel.createOne(password)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
        self.__view.windowPasswordForm.close()

    def __updatePasswordInDB(self):
        keyName = self.__view.windowPasswordForm.txtKeyname.text()
        password = (
            self.__view.windowPasswordForm.txtService.text(),
            self.__view.windowPasswordForm.txtWebsite.text(),
            self.__view.windowPasswordForm.txtDescription.text(),
            self.__view.windowPasswordForm.txtUser.text(),
            self.__view.windowPasswordForm.txtPassword.text()
        )

        self.passwordModel.updateOneByKeyName(password, keyName)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
        self.__view.windowPasswordForm.close()
        self.__cleanSelectedCell()

    def __deletePasswordInDB(self, keyName):
        self.passwordModel.deletePasswordByKeyName(keyName)

        self.__view.tblPasswords.clear()
        self.__loadTableInfo()
        self.__cleanSelectedCell()

    '''
    Table logic
    '''
    def __createDatabaseIfNotExists(self):
        if not path.exists(self.passwordModel.databasePath):
            print('Create database and tables')
            self.passwordModel.createTable()
        
        print('Database ininitalized')

    def __loadTableInfo(self):
        rows = self.__getTableItems()
        
        self.__view.tblPasswords.setRowCount(len(rows))

        for x, row in enumerate(rows):
            for y, item in enumerate(row):
                self.__view.tblPasswords.setItem(x, y, item)

        self.__view.tblPasswords.itemDoubleClicked.connect(lambda : print('double click'))
        self.__view.tblPasswords.itemClicked.connect(self.__setSelectedCell)

    def __getTableItems(self):
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

    def __setSelectedCell(self, item):
        self.selectedCell = (item.row(), item.column())
    
    def __cleanSelectedCell(self):
        self.selectedCell = None