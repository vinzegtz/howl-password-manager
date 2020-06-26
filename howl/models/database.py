import sqlite3
from os import path


class DatabaseConnection:
    
    def __init__(self):
        databaseConfigFolder = 'database'
        databaseName = 'howldb.db'
        projectPath = path.abspath(path.dirname('app.py'))
        
        self.databasePath = path.join(projectPath, f'{databaseConfigFolder}/{databaseName}')
        self.connection = None
        self.cursor = None
    
    def openConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()