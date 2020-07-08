from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from ..config.config import Config


class WindowDatabasePath(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Database Path')
        self.setFixedSize(600, 100)

        self.lytGeneral = QVBoxLayout()
        self.wgtCentral = QWidget(self)

        self.wgtCentral.setLayout(self.lytGeneral)
        self.setCentralWidget(self.wgtCentral)

        # Create GUI
        self.__createForm()

    def __createForm(self):
        self.lytForm = QVBoxLayout()
        self.lblDatabasePath = QLabel()
        self.txtDatabasePath = QLineEdit()
        self.btnSave = QPushButton()

        self.lblDatabasePath.setText('Database path')
        self.btnSave.setText('Save')

        self.lytForm.addWidget(self.lblDatabasePath)
        self.lytForm.addWidget(self.txtDatabasePath)
        self.lytForm.addWidget(self.btnSave)

        self.lytGeneral.addLayout(self.lytForm)

    def showForUpdate(self):
        databaseConfig = Config.loadDatabaseConfig()

        self.txtDatabasePath.setText(databaseConfig['path'])
        self.show()
