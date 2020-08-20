from mypassword import Password, PasswordLevel


'''
Main window controller
'''
class MainController:

    def __init__(self, view, app):
        self.btnGeneratePass = view.btnGeneratePass
        self.btnCopyPass = view.btnCopyPass
        self.lblCopyMessage = view.lblCopyMessage
        self.txtPassword = view.txtPassword
        self.clipboard = app.clipboard()

        self.connectSignals()
    
    def connectSignals(self):
        self.btnGeneratePass.clicked.connect(lambda :self.generateRandomPassword())
        self.btnCopyPass.clicked.connect(lambda :self.copyPassToClipboard())

    def generateRandomPassword(self):
        password = Password(length=32, level=PasswordLevel.FOUR)

        self.lblCopyMessage.setVisible(False)
        self.txtPassword.setText(password.password)
        self.txtPassword.setFocus()
    
    def copyPassToClipboard(self):
        password = self.txtPassword.text()
        self.clipboard.setText(password)

        if not self.lblCopyMessage.isVisible():
            self.lblCopyMessage.setVisible(True)