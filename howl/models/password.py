from .database import DatabaseConnection


class PasswordModel(DatabaseConnection):

    def __init__(self):
        super().__init__()
    
    def createTable(self):
        self.openConnection()

        self.cursor.execute('''CREATE table passwords (
            id INT AUTO_INCREMENT PRIMARY KEY,
            service_name VARCHAR(100) NOT NULL,
            website VARCHAR(200),
            description VARCHAR(200),
            username VARCHAR(100) NOT NULL,
            password VARCHAR(128) NOT NULL,
            key_name VARCHAR(100) NOT NULL
        )''')

        self.closeConnection()
    
    def getAll(self):
        self.openConnection()

        self.cursor.execute('SELECT * FROM passwords')
        passwords = self.cursor.fetchall()

        self.closeConnection()

        return passwords
    
    def createOne(self, password):
        self.openConnection()

        self.cursor.execute('INSERT INTO passwords(service_name, website, description, username, password, key_name) VALUES (?, ?, ?, ?, ?, ?)', password)
        self.connection.commit()

        self.closeConnection()
    
    def updateOneByKeyName(self, password, keyName):
        self.openConnection()

        self.cursor.execute(f'UPDATE passwords SET service_name = ?, website = ?, description = ?, username = ?, password = ? WHERE key_name = "{keyName}"', password)
        self.connection.commit()

        self.closeConnection()
    
    def deletePasswordByKeyName(self, keyName):
        self.openConnection()

        self.cursor.execute(f'DELETE FROM passwords WHERE key_name = "{keyName}"')
        self.connection.commit()

        self.closeConnection()

    def getPasswordByKeyName(self, keyName):
        self.openConnection()

        self.cursor.execute(f'SELECT * FROM passwords WHERE key_name = "{keyName}"')
        password = self.cursor.fetchone()

        self.closeConnection()

        return password