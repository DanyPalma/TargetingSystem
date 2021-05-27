# Made by github.com/cfrankovich

import os
import sys
from sys import platform
import json
from colorama import Fore, Back, Style 

import Ping as ping
import Calc as calc
import Globals as gb
import Help as hp
import About as ab
import EightBall as eb
import Settings as st

# Test Command
def ping():
    print('pong!')

# Exit Command
def exitapp():
    if gb.clearonexit:
        if gb.linux:
            os.system('clear')
        else:
            os.system('cls')
    gb.running = False

# Clear Command
def clear():
    if gb.linux:
        os.system('clear')
    else:
        os.system('cls')

# Literally Does Nothing
def nothing():
    print('', end='')

comlist = {
    'calc' : calc.calculator,
    'ping' : ping,
    'exit' : exitapp,
    'clear' : clear,
    'cls' : clear,
    '' : nothing,
    'help' : hp.help,
    'about' : ab.about,
    '8ball' : eb.eightball,
    'settings' : st.settings
}


def applySettings():
    try:
        f = open('Config.json', encoding='utf-8')
    except Exception:
        print(f'{Style.RED}Error loading the {Style.BRIGHT}Config.json{Style.NORMAL} file.')
    config = json.load(f)
    gb.prefix = config['prefix']
    gb.clearonstartup = config['clearonstart']
    gb.clearonexit = config['clearonexit']
    gb.clearcalccli = config['clearcalccli']
    

def getinput():
    try:
        com = input(gb.prefix + ' ')
    except:
        print(f'{Fore.RED}Something is wrong with the {Style.BRIGHT}prefix{Style.NORMAL} setting in the {Style.BRIGHT}Config.json{Style.NORMAL} file!')
        exit() 
    return com


def main():
    while gb.running:
        gb.command = getinput()
        command = gb.command
        keyword = command.split(' ')[0]
        try:
            comlist[keyword]()
        except:
            print(f'{Fore.RED}Command {Style.BRIGHT}{keyword}{Style.NORMAL} not found!{Fore.WHITE}')

if __name__ == '__main__':
    gb.initialize()
    applySettings()
    if gb.clearonstartup: 
        if platform == 'linux' or platform == 'linux2':
            gb.linux = True
            os.system('clear')
        elif platform == 'win32':
            gb.linux = False
            os.system('cls')
        elif platform == 'darwin':
            print('ew... mac user... CRINGE!')
            sys.exit()
        else:
            print('wtf is ur OS')
            sys.exit()
    main()
