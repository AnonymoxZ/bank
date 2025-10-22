# utils tools
from os import system
import sys
from time import strftime as timetoday, sleep
from pathlib import Path



br = f'\n{45*"-"}\n' # this a barra 

def clear():
    OS = sys.platform
    if OS.startswith('win'):
        system('cls')
    else:
        system('clear')


def timecurrency():
    time_now = timetoday('%d-%m-%y %H:%M:%S')
    return time_now


def filter_input(text:str):
    return text.lower().strip().replace(' ', '')


def pathdb():
    '''
    :to create db conection;
    '''
    path_dir = Path('..') / 'database'
    path_dir.mkdir(exist_ok=True, parents=True)
    path_db = path_dir / 'base.db'
    return path_db


def wait(sec=0):
    if sec != 0:
        sleep(sec)
    elif sec == 0:
        system('pause')

