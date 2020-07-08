import sqlite3
from os import path
from ..config.config import Config

class DatabaseConnection:
    
    def __init__(self):
        databaseConfig = Config.loadDatabaseConfig()
        
        self.databasePath = databaseConfig['path']
        self.connection = None
        self.cursor = None
    
    def openConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()