from RANDCLASS import said, ask
from commands import Dice, Todo, count, tamer, JsonTest, encrpytion, settingmenu
from pathfinder import pathfinder
from game import game
import re
import os
joe = False
gooer = False



said('Welcome to SeanOS')



while True:
    command = input('Enter a command: ')
    if command == 'dice':
        Dice()
    if command == 'todo':
        Todo()   
    if command == 'CabbavsGogeta':
        said('Gogeta ssj4 stomps Cabba no diff')
    if command == 'count':
        count()
    if command == 'timer':
        tamer()
    if command == 'jjtest':
        JsonTest()
    if command == 'enc':
        encrpytion()
    if command == 'game':
        game()
    if command == 'clear':
        ask('are you sure you would like to clear the console? (yes/no):')
        clear = input('are you sure you would like to clear the console? (yes/no):')
        if clear == 'yes':
            command = 'clear'
            if os.name in ('nt', 'dos'): 
                command = 'cls'
            os.system(command)
    if command == 'settings':
        settingmenu()
    if command == 'pathfinder':
        pathfinder()


    
    


