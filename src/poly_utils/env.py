import os
from dotenv import load_dotenv

def load_env(env_path=None):
    if env_path:
        load_dotenv(env_path)
    else:
        load_dotenv()
    cfg = {
        'PK': os.getenv('PK'),
        'BROWSER_ADDRESS': os.getenv('BROWSER_ADDRESS'),
        'SPREADSHEET_URL': os.getenv('SPREADSHEET_URL'),
        'DATA_PATH': os.getenv('DATA_PATH', './data'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
    }
    return cfg
