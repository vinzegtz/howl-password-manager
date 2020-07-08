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

from .windows_database_path import WindowDatabasePath
from .window_password import WindowPasswordForm


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
        self.windowDatabasePathForm = WindowDatabasePath(self)

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
