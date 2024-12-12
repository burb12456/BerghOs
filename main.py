from RANDCLASS import said, ask
from commands import Dice, Todo, count, tamer, JsonTest, encrpytion, settingmenu, notebook, password
from pathfinder import main
from spreadsheet import Style
from game import game
import re
import os
commands = ['dice', 'todo', 'CabbavsGogeta', 'count', 'timer', 'jjtest', 'enc','game', 'clear', 'settings', 'pathfinder', 'notes', 'login', 'style']
joe = False
gooer = False
logged = False
command = 'clear'
if os.name in ('nt', 'dos'): 
    command = 'cls'
    os.system(command)


said('Welcome to BURGHOS')
ask('press enter to start')
input('press enter to start:')

while True:
    ask(('Enter a command'))
    command = input('Enter a command: ')
    if command == commands[0]:
        Dice()
    if command == commands[1]:
        Todo()   
    if command == commands[2]:
        said('Gogeta SSJ4 stomps Cabba no diff')
    if command == commands[3]:
        count()
    if command == commands[4]:
        tamer()
    if command == commands[5]:
        JsonTest()
    if command == commands[6]:
        encrpytion()
    if command == commands[7]:
        game()
    if command == commands[8]:
        ask('are you sure you would like to clear the console? (yes/no):')
        clear = input('are you sure you would like to clear the console? (yes/no):')
        if clear == 'yes':
            command = 'clear'
            if os.name in ('nt', 'dos'): 
                command = 'cls'
            os.system(command)
    if command == commands[9]:
        settingmenu()
    if command == commands[10]:
        main()

    if command == commands[11]:
        notebook()
    if command == commands[12]:
        ask('username:')
        Ask = input('username:')
        if Ask == 'Burgh':
            ask('password')
            pask = input('password:')
            if pask == password:
                logged = True
                said('Welcome back.')
            else:
                said('WRONG')
        else:
            said('No user known as ' + str(Ask))
    if command == commands[13]:
            Style()
    if command == 'help':
        said('commands consist of:')
        print(commands)
    else:
        said('No such command')


    
    


