from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class WindowPasswordForm(QMainWindow):
 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Password Management')
        self.setFixedSize(400, 360)
        
        self.lytGeneral = QVBoxLayout()
        self.wgtCentral = QWidget(self)

        self.wgtCentral.setLayout(self.lytGeneral)
        self.setCentralWidget(self.wgtCentral)

        # Create GUI
        self.__createForm()

    def __createForm(self):
        self.lytForm = QVBoxLayout()

        self.lblService = QLabel()
        self.lblWebsite = QLabel()
        self.lblDescription = QLabel()
        self.lblUser = QLabel()
        self.lblPassword = QLabel()
        self.lblKeyname = QLabel()

        self.txtService = QLineEdit()
        self.txtWebsite = QLineEdit()
        self.txtDescription = QLineEdit()
        self.txtUser = QLineEdit()
        self.txtPassword = QLineEdit()
        self.txtKeyname = QLineEdit()

        self.btnGeneratePassword = QPushButton()
        self.btnSave = QPushButton()
        self.btnUpdate = QPushButton()

        self.lblService.setText('Service')
        self.lblWebsite.setText('Website')
        self.lblDescription.setText('Description')
        self.lblUser.setText('User')
        self.lblPassword.setText('Password')
        self.lblKeyname.setText('Keyname')
        # self.btnGeneratePassword.setText('Generate pass')
        self.btnSave.setText('Save')
        self.btnUpdate.setText('Update')

        self.lytForm.addWidget(self.lblService)
        self.lytForm.addWidget(self.txtService)
        self.lytForm.addWidget(self.lblWebsite)
        self.lytForm.addWidget(self.txtWebsite)
        self.lytForm.addWidget(self.lblDescription)
        self.lytForm.addWidget(self.txtDescription)
        self.lytForm.addWidget(self.lblUser)
        self.lytForm.addWidget(self.txtUser)
        self.lytForm.addWidget(self.lblPassword)
        self.lytForm.addWidget(self.txtPassword)
        self.lytForm.addWidget(self.lblKeyname)
        self.lytForm.addWidget(self.txtKeyname)
        # self.lytForm.addWidget(self.btnGeneratePassword)
        self.lytForm.addWidget(self.btnSave)
        self.lytForm.addWidget(self.btnUpdate)

        self.lytGeneral.addLayout(self.lytForm)

    def cleanForm(self):
        self.txtService.setText('')
        self.txtWebsite.setText('')
        self.txtDescription.setText('')
        self.txtUser.setText('')
        self.txtPassword.setText('')
        self.txtKeyname.setText('')
        
        self.txtService.setFocus()

    def fillForm(self, password):
        self.txtService.setText(password[1])
        self.txtWebsite.setText(password[2])
        self.txtDescription.setText(password[3])
        self.txtUser.setText(password[4])
        self.txtPassword.setText(password[5])
        self.txtKeyname.setText(password[6])
        
        self.txtService.setFocus()

    def showForCreate(self):
        self.btnUpdate.hide()
        self.btnSave.show()
        self.show()

    def showForUpdate(self):
        self.btnUpdate.show()
        self.btnSave.hide()
        self.txtKeyname.setReadOnly(True)
        self.show()
