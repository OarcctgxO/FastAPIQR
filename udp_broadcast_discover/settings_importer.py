"""
Импортирует файл settings из родительской директории.
Использование: from settings_importer import settings.
"""
from os.path import dirname, abspath
from sys import path
parent_dir = dirname(dirname(abspath(__file__)))
if parent_dir not in path:
    path.insert(0, parent_dir)
import settings