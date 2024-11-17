import random
import time
import sys
import json


timers = []
try:
    with open('setting.json', 'r') as file:
        settings = json.load(file)

except FileNotFoundError:
    settings = {}
    print('not found')
text_speed = float(settings.get('text_speed', 0.01)) # Provide default text speed

class rolladice():
    def __init__(self, dicenumber, dicesize):
        self.disesize = dicesize
        self.dicenumber = dicenumber
        counter = -1
        frfr = []
        for i in range(dicenumber):
            diceresult = random.randint(1, dicesize)
            frfr.append(diceresult)   
        for i in range(dicenumber):
            counter += 1    
            print('dice number ', counter + 1, ' result:', frfr[counter])      
        total = frfr.count(5)
        print('total score:', sum(frfr)) 

class said():
    def __init__(self, text):
        self.text = text
        counter = 1
        while len(text) + 1 > counter:
            print(text[:counter])
            counter += 1
            time.sleep(text_speed)
            if not len(text) + 1 == counter:
                sys.stdout.write('\033[F')  
class ask():
    def __init__(self, text):
        self.text = text
        counter = 1
        while len(text) + 1 > counter:
            print(text[:counter])
            counter += 1
            time.sleep(text_speed)
            sys.stdout.write('\033[F') 
        
         
class timer():
    def __init__(self, timerr, timer_instance):
        self.timerr = timerr
        self.timer_instance = timer_instance
        erm = timerr
        while (erm) > 0:
            erm -= 1
            time.sleep(1)
            timers.append(str(timerr)  +' second timer: ' + str(erm) + ' seconds' )

        said('Timer done!!!')

class ATJSON():
    def __init__(self, filename, function, value):
        self.filename = filename
        self.function = function
        self.value = value
        if function == ' todo':
            pass

