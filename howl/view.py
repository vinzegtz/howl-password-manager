from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


# Class to create the main window interface
class WindowManager(QMainWindow):

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

        # Other windows
        self.windowPasswordForm = WindowPasswordForm(self)

        # Create GUI
        self.__createHeader()
        self.__createMainInput()
        self.__createPasswordsTable()
        self.__createMenuBar()

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

        self.lytPasswordsTable = QVBoxLayout()
        self.lytPasswordsTableStatus = QHBoxLayout()
        self.tblPasswords = QTableWidget()
        self.lblPasswordsTableStatusTitle = QLabel()
        self.lblPasswordsTableStatusMessage = QLabel()

        self.tblPasswords.setColumnCount(6)
        self.tblPasswords.setHorizontalHeaderLabels(tableLabels)
        self.lblPasswordsTableStatusTitle.setText('Status: ')
        self.lblPasswordsTableStatusMessage.setText('-----')
        self.lblPasswordsTableStatusTitle.setAlignment(Qt.AlignRight)
        self.lblPasswordsTableStatusMessage.setAlignment(Qt.AlignRight)
        self.lytPasswordsTableStatus.setStretch(0, 0)
        self.lytPasswordsTableStatus.setStretch(0, 0)

        self.lytPasswordsTableStatus.addWidget(self.lblPasswordsTableStatusTitle)
        self.lytPasswordsTableStatus.addWidget(self.lblPasswordsTableStatusMessage)
        self.lytPasswordsTable.addWidget(self.tblPasswords)
        self.lytPasswordsTable.addLayout(self.lytPasswordsTableStatus)
        self.lytGeneral.addLayout(self.lytPasswordsTable)

    def __createMenuBar(self):
        menuBar = self.menuBar()
        
        self.menuItemFile = menuBar.addMenu('File')
        self.menuItemActionNewPassword = QAction('New password', self)
        self.menuItemActionNewPassword.setShortcut('Ctrl+N')
        self.menuItemFile.addAction(self.menuItemActionNewPassword)

        self.menuItemEdit = menuBar.addMenu('Edit')
        self.menuItemEdit.addAction('Change DB path')
        self.menuItemActionEditPassword = QAction('Edit password', self)
        self.menuItemActionEditPassword.setShortcut('Ctrl+E')
        self.menuItemEdit.addAction(self.menuItemActionEditPassword)
        self.menuItemActionDeletePassword = QAction('Delete password', self)
        self.menuItemActionDeletePassword.setShortcut('Ctrl+D')
        self.menuItemEdit.addAction(self.menuItemActionDeletePassword)

        self.menuItemHelp = menuBar.addMenu('Help')
        self.menuItemActionAbout = QAction('About', self)
        self.menuItemActionAbout.setShortcut('Ctrl+R')
        self.menuItemHelp.addAction(self.menuItemActionAbout)


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