from ..models.password import PasswordModel


'''
Password form controller
'''
class PasswordController:
    
    def __init__(self, view, tableController):
        self.windowPasswordForm = view.windowPasswordForm
        self.tblPasswords = view.tblPasswords
        self.tableController = tableController

        self.passwordModel = PasswordModel()

        self.connectSignals()
    
    def connectSignals(self):
        self.windowPasswordForm.btnSave.clicked.connect(lambda :self.savePassword())
        self.windowPasswordForm.btnUpdate.clicked.connect(lambda :self.updatePassword())
    
    def savePassword(self):
        password = (
            self.windowPasswordForm.txtService.text(),
            self.windowPasswordForm.txtWebsite.text(),
            self.windowPasswordForm.txtDescription.text(),
            self.windowPasswordForm.txtUser.text(),
            self.windowPasswordForm.txtPassword.text(),
            self.windowPasswordForm.txtKeyname.text(),
        )

        if not self.isFormValid(self.windowPasswordForm):
            self.windowPasswordForm.lblValidation.setVisible(True)
        else:
            self.windowPasswordForm.lblValidation.setVisible(False)

            self.passwordModel.createOne(password)

            self.tblPasswords.clear()
            self.tableController.loadTableInfo()
            self.windowPasswordForm.close()

    def updatePassword(self):
        keyName = self.windowPasswordForm.txtKeyname.text()
        password = (
            self.windowPasswordForm.txtService.text(),
            self.windowPasswordForm.txtWebsite.text(),
            self.windowPasswordForm.txtDescription.text(),
            self.windowPasswordForm.txtUser.text(),
            self.windowPasswordForm.txtPassword.text()
        )

        if not self.isFormValid(self.windowPasswordForm):
            self.windowPasswordForm.lblValidation.setVisible(True)
        else:
            self.windowPasswordForm.lblValidation.setVisible(False)
            
            self.passwordModel.updateOneByKeyName(password, keyName)

            self.tblPasswords.clear()
            self.tableController.loadTableInfo()
            self.windowPasswordForm.close()
            self.tableController.selectedCell = None
    
    def isFormValid(self, passwordForm):
        isValid = True
        fields = {
            'service': passwordForm.txtService.text(),
            'website': passwordForm.txtWebsite.text(),
            'description': passwordForm.txtDescription.text(),
            'user': passwordForm.txtUser.text(),
            'password': passwordForm.txtPassword.text(),
            'keyname': passwordForm.txtKeyname.text()
        }

        for key, value in fields.items():
            if value == '':
                isValid = False
        
        return isValid