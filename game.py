import time
from RANDCLASS import said, ask
import random
import time
def game():
    dumb = 0

    player_HP = 92
    player_attack = 1
    skip = 0
    item = []
    a = 1
    # menu
    print("smorgasbord the game")
    print("press enter to start")
    joe = input()
    if skip == 0:
        Text = said("You're in a strange grassland, that is home to loads of grass. Maybe you can survive, but you don't know where you are, and you don't know what you are doing.")
        
    while 5 > 0:
        # Wake up
        
        print("What would you like to do: inspect surroundings, inspect grass, inspect soil, inspect dirt, inspect rocks, inspect smth idk")
        if skip == 0:
            Password = input('> ')
        else: 
            Password = "inspect surroundings" 

        if Password == "inspect grass":
            if skip == 0:
                Text = said("The grass on the ground has a very grassy texture, it's moist and it's grass green.")
                if skip == 0:
                    poop = input("Would you like to pick it up? ")
                else: 
                    poop = "yes"
                if poop == "yes":
                    item.append("grass")
        elif Password == "inspect soil":
            Text = said("The soil is dry and sandy, it's sandy and dry.")
            poop = input("Would you like to pick it up? ")
            if poop == "yes":
                Text = said("It falls through the cracks of your hands")
        elif Password == "inspect smth idk":
            Text = said("Denied!!!")
        elif Password == "inspect surroundings":
            if skip == 0:
                Text = said("On the grassland is a cave. Would you like to inspect it?")
                poop = input("yes or no ")
            else: 
                poop = "yes"
            if poop == "yes":
                if skip == 0:
                    Text = said("You enter the cave. Inside is a giant hole. The walls are made out of rock, the floor is made out of rocks, the ceiling is made out of rocks. It's a rocky world.")
                while 5 > 0:
                    # Cave thingy
                    if skip == 0:
                        poop = input("What would you like to do? inspect hole, inspect wall, inspect floor, inspect ceiling, inspect rocks, inspect smth idk ")
                    else:
                        poop = "inspect hole"
                    if poop == "inspect hole":
                        if skip == 0 :
                            Text = said("You walk into the hole and suddenly trip over, and everything goes black.")
                        while 5 > 0:
                            # How was the FALLLLL
                            if skip == 0:
                                poop = input("Would you like to wake up? ")
                            else: 
                                poop = "yes"
                            if poop == "yes":
                                if skip == 0:
                                    Text = said("You land on a mattress. The mattress is surrounded by a large puddle.")
                                while 5 > 0:
                                    # Mattress
                                    if skip == 0:
                                        poop = input("Would you like to inspect the puddle or maybe the mattress? ")
                                    else:
                                        poop = "puddle"
                                    if poop == "puddle":
                                        if skip == 0:
                                            Text = said("You look closely at the puddle, but all you see is your reflection?")
                                            poop = input("Would you like to jump in? ")

                                        else:
                                            poop = "yes"
                                        if poop == "yes":
                                            if skip == 0:
                                                Text = said("You jump in and wet your feet, legs, and other body parts.")
                                            while 5 > 0:
                                                # the water
                                                if skip == 0:
                                                    poop = input("Would you like to inspect your surroundings? ")
                                                else: poop = "yes"
                                                if poop == "yes":
                                                    if skip == 0:
                                                        Text = said("You suddenly see a dummy standing right in front of you. You have no idea how you didn't notice this early since it's litrally 2 cm from your face. ")
                                                        ask = input("Touch the dummy?")
                                                    else:
                                                        ask = "yes"
                                                    if ask == "yes":

                                                        while 5 > 0:

                                                                Text = said("Suddenly the dummy starts moving.")
                                                                Dummy_Speak = said("'Wot you doin', touchin' me'")
                                                                Dummy_Speak = said("'You wanna fight blud, I'll give you one mate'")
                                                                dummy_HP = 100
                                                                dummy_attack = 10
                                                                dummy_defence = 4
                                                                while 5 > 0:
                                                                    while a > 0:
                                                                        # fight
                                                                        poop = input("What would you like to do? attack, defend, talk, items  ")
                                                                        if poop == "attack":
                                                                            roll = random.randint(1, player_attack)
                                                                            Text = said("You punch the dummy. You only do " + str(roll) + " damage!")
                                                                            a = 0
                                                                        if poop == "defend":
                                                                            Text = said("You try to block the dummys next attack")
                                                                            a = 0
                                                                        if poop == "talk":
                                                                            Text = said("You try to talk to the dummy.")
                                                                            Text = said("The dummy growls at you.")
                                                                            a = 0
                                                                        if poop =="items":
                                                                            Text = said("You try to inspect your bag.")
                                                                            ask = input("Inside is:" + str(item))
                                                                            a = 0
                                                                    Roll = random.randint(1, dummy_attack)
                                                                    Text = said("Now the dummy fights back. He does " + str(Roll) + " damage!")
                                                                    a = 1
                                                                        
                                                                            
                                                                            # fight
                                                                            

                                                                    
                                                                    
                                    elif poop == "mattress":
                                        Text = said("You look closely at the mattress, it's old and dirty but comfy nevertheless.")

