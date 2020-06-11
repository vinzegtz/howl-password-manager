import sqlite3


# Class to manage the connections and the operations to the database
class DB:
    __instance = None
    
    databaseName = 'howldb.db'
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
    def __openConnection():
        instance = DB.getInstance()

        instance.connection = sqlite3.connect(instance.databaseName)
        instance.cursor = instance.connection.cursor()
    
    @staticmethod
    def __closeConnection():
        instance = DB.getInstance()
        instance.connection.close()