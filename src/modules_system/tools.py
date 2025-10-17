# utils tools
from os import system
import sys
from time import strftime as timetoday


def clear():
    OS = sys.platform
    if OS.startswith('win'):
        system('cls')
    else:
        system('clear')


def timecurrency():
    time_now = timetoday('%d-%m-%y %H:%M:%S')
    return time_now
