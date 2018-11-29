import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'darwin':
    base = ""