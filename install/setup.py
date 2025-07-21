import os
import configparser

_pip = "pip install "
_cfg = configparser.ConfigParser()

os.system('Python -V')
input ('Нажмите любую клавишу что бы продолжить...')

_cfg.read(os.getcwd()+chr(92)+'install.ini')
os.system("pip install --upgrade pip")
os.system(_pip + _cfg.get('NAMES','aiogram'))
os.system(_pip + _cfg.get('NAMES','tk'))

input ('Нажмите любую клавишу что бы продолжить...')