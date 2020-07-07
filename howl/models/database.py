import sqlite3
from os import path
from config import config


class DatabaseConnection:
    
    def __init__(self):
        self.databasePath = config.DATABASE_PATH
        self.connection = None
        self.cursor = None
    
    def openConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()