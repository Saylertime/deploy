bind = '127.0.0.1:8000'
workers = 3
user = 'alexeyglinkin'
timeout = 120

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)