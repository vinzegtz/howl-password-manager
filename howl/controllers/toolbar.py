from functools import partial
from mypassword import Password, PasswordLevel
from PyQt5.QtWidgets import QAction

from ..models.password import PasswordModel


'''
Toolbar Controller
'''
class ToolbarController:
    
    def __init__(self, view, tableController):
        self.menuItemFile = view.menuItemFile
        self.menuItemEdit = view.menuItemEdit
        self.menuItemHelp = view.menuItemHelp
        self.windowPasswordForm = view.windowPasswordForm
        self.windowDatabasePathForm = view.windowDatabasePathForm
        self.tblPasswords = view.tblPasswords
        self.tableController = tableController

        self.passwordModel = PasswordModel()

        self.connectSignals()
    
    def connectSignals(self):
        self.menuItemFile.triggered[QAction].connect(partial(self.clickFileActions))
        self.menuItemEdit.triggered[QAction].connect(partial(self.clickEditActions))
        self.menuItemHelp.triggered[QAction].connect(lambda : print('click'))
    
    def clickFileActions(self, action):
        if action.text() == 'New password':
            self.newPasswordAction()

    def clickEditActions(self, action):
        if self.tableController.selectedCell != None:
            if action.text() == 'Edit password':
                self.editPasswordAction()
            elif action.text() == 'Delete password':
                self.deletePasswordAction()
        
        if action.text() == 'Change DB path':
            self.windowDatabasePathForm.showForUpdate()
    
    def newPasswordAction(self):
        password = Password(length=32, level=PasswordLevel.FOUR)

        self.windowPasswordForm.cleanForm()
        self.windowPasswordForm.txtPassword.setText(password.password)
        self.windowPasswordForm.showForCreate()

    def editPasswordAction(self):
        keyName = self.tblPasswords.item(self.tableController.selectedCell[0], 5).text()
        password = self.passwordModel.getPasswordByKeyName(keyName)
        
        self.windowPasswordForm.fillForm(password)
        self.windowPasswordForm.showForUpdate()

    def deletePasswordAction(self):
        keyName = self.tblPasswords.item(self.tableController.selectedCell[0], 5).text()
            
        self.passwordModel.deletePasswordByKeyName(keyName)

        self.tblPasswords.clear()
        self.tableController.loadTableInfo()
        self.tableController.selectedCell = None