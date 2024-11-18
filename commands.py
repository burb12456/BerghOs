import re
import time
import json

filename = 'todo.json'
esk = 0
amount_timers = 0
global screen_size
global screen_speed
from RANDCLASS import rolladice, said, ask, timer, timers
def Dice():
    while True:
        ask('Roll a dice (e.g., 5d2): ')
        erm = input('Roll a dice (e.g., 5d2): ')  

        check = erm.isalpha()  
        check2 = erm.isspace()  

        letters = re.findall(r'[a-zA-Z]', erm)
        count = len(letters)  
        if 'd' in erm and count <= 1:
                
            john = erm.find('d')
            
            first_result = erm[:int(john)]
            last_result = erm[int(john + 1):]

            rolladice(int(first_result), int(last_result))
            break
            
        else:
            said('Please make sure your answer has something like 5d2')
def Todo():
    count = 0  # Initialize count

    try:
        with open(filename, 'r') as file:
            # Read JSON data or start with an empty list if the file is empty
            content = file.read().strip()
            todo = json.loads(content) if content else []
    except (FileNotFoundError, json.JSONDecodeError):
        todo = []  # Initialize with an empty list if the file doesn't exist or is invalid
        said("Starting with an empty list.")

    while True:
        ask('What would you like to do in your list:')
        Ask = input('What would you like to do in your list:')
        
        if Ask == 'help':
            said('Commands: view, add, remove, exit')
        elif Ask == 'add':
            ask('What would you like to add:')
            Additional_item = input('What would you like to add:')
            todo.append(Additional_item)  # Add item to the list
        elif Ask == 'view':
            if todo:
                said('Your list consists of:')
                for item in todo:
                    said(item)
            else:
                said("Your list is empty.")
        elif Ask == 'remove':
            ask('What would you like to remove:')
            Additional_item = input('What would you like to remove:')
            if Additional_item in todo:
                todo.remove(Additional_item)  # Remove item if it exists
            else:
                said('Not in list')

        elif Ask == 'check':
            ask('What items would you like to check off?')
            esk = input('What items would you like to check off?:')
            if esk in todo:

                ee = todo.index(esk)
                print(ee)
                todo.remove(esk)
                esk = esk + '✓'
                todo.insert(ee, str(esk))
            else:
                said('not in list')
        elif Ask == 'wipe':
            ask('are you sure? (yes/no) :')
            clearance = input('are you sure? (yes/no)')
            if clearance == 'yes':
                todo = []
                with open(filename, 'w') as file:
                    json.dump(todo, file, indent=4)
        elif Ask == 'exit':
            break
        
        # Save the updated todo list back to the file
        with open(filename, 'w') as file:
            json.dump(todo, file, indent=4)



def count():
    said('this is a count to one million in python 3, would you like to see it in action ( warning!: might slow down count):')
    germ = input('y/n')
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    countdown = 0
    while countdown <= 999999:
        countdown += 1
        if germ == 'y':
            print(countdown)
    print('done')

def tamer():
    if amount_timers == 0:
        ask('How long do you want your timer in (in seconds)')
        Ask = input('How long do you want your timer in (in seconds)')
        timer(Ask, amount_timers)
        amount_timers + 1
    else:
        ask('What would you like to do?:')
        Ask = input('What would you like to do?:')
        if Ask == 'help':
            said('Add Check')
        if Ask == 'add':
            ask('How long do you want your timer in (in seconds)')
            Ask = input('How long do you want your timer in (in seconds)')
            timer(100, amount_timers)
            amount_timers + 1
        if Ask == 'set':
            said('There are the timer on right now')
            while len(timers) > count:
                said(timers[count])
                count += 1

def JsonTest():
    # Step 1: Load existing data from the JSON file
    try:
        with open(filename, 'r') as file:
            # Check if file is empty
            if file.read().strip() == "":  
                data = []  # Initialize with an empty list if the file is empty
            else:
                file.seek(0)  # Reset pointer to the beginning of the file
                data = json.load(file)  # Load the JSON data
    except FileNotFoundError:
        data = []  # Start with an empty list if the file doesn't exist

    # Step 2: Add new data to the loaded data
    new_entry = {
        "name": "Joe"
    }
    data.append(new_entry)

    # Step 3: Save the updated data back to the JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def encrpytion():
    t = 1

    while t > 0:    
        ask('Which cipher would you like me to help with?')
        Ask = input('Which cipher would you like me to help with?:')
        if Ask == 'none':
            t = 0
        elif Ask == 'caeser':
            ask('e or d')
            Ask = input('e or d:')
            if Ask == 'd':
                while 1 > 0:
                    ask('give string')
                    Ask = input('givev string:')
                    shift = 1
                    if Ask.isalpha():
                        count = 0
                        full = ''
                        erer = 0
                        capital = False
                        while shift < 26:
                            while count < len(Ask):
                                erer = ord(Ask[count])
                                if Ask[count].isupper():
                                    capital = True
                                else:
                                    capital = False
                                
                                erer = erer + shift
                                if erer > ord('Z') and capital == True:
                                    erer -= 26
                                elif erer > ord('z') and capital == False:
                                    erer -= 26
                                full = full + chr(erer)
                                count += 1

                            print('shift of ', 26 - shift, ':' + full)
                            shift += 1
                            count = 0
                            full = ''
                            erer = 0
            elif Ask == 'e':
                ask('give string')
                Ask = input('givev string:')  
                ask('give key')
                key = input('givev key:')
                count = 0
                full = ''
                while count < len(Ask):
                    erer = ord(Ask[count])
                    if Ask[count].isupper():
                        capital = True
                    else:
                        capital = False
                    
                    erer += int(key)
                    if erer > ord('Z') and capital == True:
                        erer -= 26
                    elif erer > ord('z') and capital == False:
                        erer -= 26
                    full = full + chr(erer)
                    count += 1
                print(full)
def settingmenu():

    t = 1
    while t> 0:
        try:
            with open('settings.json', 'r') as file:
                settings = json.load(file)
        except FileNotFoundError:
            settings = {}  # Start
        ask('what would you like to do?')
        setting = input('what would you like to do?')
        if setting.lower() == 'help':
            said('options: textspeed, quit')
        elif setting.lower() == 'textspeed':
            ask('what would you like to change it to?')
            new_speed = input('what would you like to change it to?:')
            if int(new_speed) > 0.5:
                new_speed = 0.5
            if not isinstance(new_speed, (int, float)):
                said('it is not a number try again')
                new_speed = 0.01
            settings['text_speed'] = new_speed
            with open('setting.json', 'w') as file:
                json.dump(settings, file, indent=4)
        elif setting.lower == 'quit':
            t = 0
def notebook():
    pass

    