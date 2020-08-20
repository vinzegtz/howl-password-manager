import json
from os import path

class Config:
    configFilePath = path.join(path.abspath(path.dirname('app.py')), 'config/config.json')

    @staticmethod
    def createConfigFile():
        config = {}
        configProject = {}
        configDatabase = {}

        configProject['path'] = path.abspath(path.dirname('app.py'))
        configDatabase['path'] = path.join(configProject['path'], 'database/howl.db')

        config['project'] = configProject
        config['database'] = configDatabase

        with open(Config.configFilePath, 'w+') as f:
            json.dump(config, f)
    
    @staticmethod
    def loadDatabaseConfig():
        with open(Config.configFilePath) as f:
            config = json.load(f)
        
        return config['database']
    
    @staticmethod
    def saveDatabaseConfig(**kwargs):
        with open(Config.configFilePath) as f:
            config = json.load(f)
        
        for key, value in kwargs.items():
            config['database'][key] = value
        
        with open(Config.configFilePath, 'w+') as f:
            json.dump(config, f)
