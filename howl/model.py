import sqlite3
from os import path


# Class to manage the connections and the operations to the database
class DB:
    __instance = None
    
    databaseConfigFolder = 'database'
    databaseName = 'howldb.db'
    
    packagePath = path.abspath(path.dirname('app.py'))
    databasePath = path.join(packagePath, f'{databaseConfigFolder}/{databaseName}')
    
    connection = None
    cursor = None

    def __new__(cls):
        if not DB.__instance:
            DB.__instance = object.__new__(cls)
        
        return DB.__instance

    @staticmethod
    def getInstance():
        if not DB.__instance:
            DB.__instance = DB()
        
        return DB.__instance

    @staticmethod
    def createPasswordsTable():
        instance = DB.getInstance()

        instance.__openConnection()
        instance.cursor.execute('''CREATE table passwords (
            id INT AUTO_INCREMENT PRIMARY KEY,
            service_name VARCHAR(100) NOT NULL,
            website VARCHAR(200),
            description VARCHAR(200),
            username VARCHAR(100) NOT NULL,
            password VARCHAR(128) NOT NULL,
            key_name VARCHAR(100) NOT NULL
        )''')
        
        instance.__closeConnection()

    @staticmethod
    def getAllPasswords():
        instance = DB.getInstance()

        instance.__openConnection()

        instance.cursor.execute('SELECT * FROM passwords')
        passwords = instance.cursor.fetchall()

        instance.__closeConnection()

        return passwords
 
    @staticmethod
    def savePassword(password):
        instance = DB.getInstance()
        instance.__openConnection()

        instance.cursor.execute('INSERT INTO passwords(service_name, website, description, username, password, key_name) VALUES (?, ?, ?, ?, ?, ?)', password)
        instance.connection.commit()

        instance.__closeConnection()

    @staticmethod
    def __openConnection():
        instance = DB.getInstance()
        print(instance.databasePath)
        instance.connection = sqlite3.connect(instance.databasePath)
        instance.cursor = instance.connection.cursor()
    
    @staticmethod
    def __closeConnection():
        instance = DB.getInstance()
        instance.connection.close()