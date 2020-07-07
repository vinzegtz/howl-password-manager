"""
Configuration
"""
import json
from os import path

# Prohect path
PROJECT_PATH = path.abspath(path.dirname('app.py'))

# Config folder name
CONFIG_FOLDER = 'config'

# Config file name
USER_CONFIG_FILE = 'user.json'


# Load user Config
try:
    configFile = open(path.join(PROJECT_PATH, f'{CONFIG_FOLDER}/{USER_CONFIG_FILE}'))
    userConfig = json.load(configFile)
    configFile.close()
except:
    userConfig = None


# Database name
if userConfig != None and 'databaseName' in userConfig and userConfig['databaseName'] != '':
    DATABASE_NAME = userConfig['databaseName']
else:
    DATABASE_NAME = 'howldb.db'

# Default database folder
DATABASE_CONFIG_FOLDER = 'database'

# Database path
if userConfig != None and 'databasePath' in userConfig and userConfig['databasePath'] != '':
    DATABASE_PATH = userConfig['databasePath']
else:
    DATABASE_PATH = path.join(PROJECT_PATH, f'{DATABASE_CONFIG_FOLDER}/{DATABASE_NAME}')