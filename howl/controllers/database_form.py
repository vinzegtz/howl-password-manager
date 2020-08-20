from ..config.config import Config


'''
Database path form controller
'''
class DatabasePathController:

    def __init__(self, view, tableController):
        self.windowDatabasePathForm = view.windowDatabasePathForm
        self.tblPasswords = view.tblPasswords
        self.tableController = tableController

        self.connectSignals()
    
    def connectSignals(self):
        self.windowDatabasePathForm.btnSave.clicked.connect(lambda :self.updateDatabasePath())
    
    def updateDatabasePath(self):
        newDatabasePath = self.windowDatabasePathForm.txtDatabasePath.text()

        Config.saveDatabaseConfig(path=newDatabasePath)
        self.windowDatabasePathForm.close()

        self.tblPasswords.clear()
        self.tableController.loadTableInfo()
        self.tableController.selectedCell = None