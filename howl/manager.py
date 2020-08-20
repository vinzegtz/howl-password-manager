from os import path

from .controllers.main import MainController
from .controllers.table import TableController
from .controllers.toolbar import ToolbarController
from .controllers.password_form import PasswordController
from .controllers.database_form import DatabasePathController
from .config.config import Config


'''
Controllers manager
'''
class Manager:

    def __init__(self, view, application):
        # Create config file
        if not path.exists(Config.configFilePath):
            print('Create config file')
            Config.createConfigFile()

        self.mainController = MainController(view, application)
        self.tableController = TableController(view)
        self.toolbarController = ToolbarController(view, self.tableController)
        self.passwordController = PasswordController(view, self.tableController)
        self.databasePathController = DatabasePathController(view, self.tableController)