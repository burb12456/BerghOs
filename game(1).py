import random
import time
import sys

from RANDCLASS import said , ask
basic = []
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.maxHealth = random.randint(95, 175)
        self.maxEnergy = random.randint(10, 25)
        self.health = self.maxHealth
        self.energy = self.maxEnergy
        self.power = random.randint(4, 10)

    def describeFighter(self):
        #No need for newlines
        print(f"Name: {self.name}  HP: {self.health}/{self.maxHealth} Energy: {self.energy}/{self.maxEnergy} Power: {self.power}")
    
    def updateFighter(self, health, energy):
        if health > self.maxHealth:
            health = self.maxHealth

        if health < 0:
            health = 0

        if energy > self.maxEnergy:
            energy = self.maxEnergy

        self.health = health
        self.energy = energy

class Attack:
    def __init__(self, name: str, energyUsage: int, attackPower: int, criticalRate: int, cate: int):
        self.name = name
        self.energyUsage = energyUsage
        self.attackPower = attackPower
        self.criticalRate = criticalRate
        self.cate = cate
        if cate == 0:
            basic.append(name)

    
    
    def use(self, user: Fighter, target: Fighter):
        damageDealt = round((user.power + self.attackPower) * 1.2)
        energyUsed = round((self.energyUsage - (round(user.power / 4))))
        criticalAttack = False

        if self.criticalRate != 0:
            criticalRoll = random.randint(1, 100)
            criticalHit = range(1, self.criticalRate)
            
            if criticalRoll in criticalHit:
                damageDealt *= 2
                criticalAttack = True

        if user.energy < self.energyUsage:
            damageDealt = 0
            energyUsed = -self.energyUsage / 2

        if self.attackPower == 0:
            damageDealt = 0

        return([damageDealt, energyUsed, criticalAttack])

fighters = [Fighter("..."), Fighter("Enemy Fighter")]
ask("What will your fighter's name be?")
playerName = input("What will your fighter's name be? ").title()

fighters[0] = Fighter(playerName)

attacks = {
    "slap": Attack("Slap", 2, 4, 75, 0),
    "punch": Attack("Punch", 4, 8, 30, 0),
    "kick": Attack("Kick", 7, 17, 25, 0),
    "fireball": Attack("Fireball", 10, 23, 20, 0),
    "deathray": Attack("Deathray", 15, 35, 45, 0),
    "rest": Attack("Rest", -10, 0, 0, 0)
}

currentTurn = 0
while 0 != fighters[0].health and 0 != fighters[1].health:
    time.sleep(2.5)

    for fighter in fighters:
        said("~" * 18)
        fighter.describeFighter()

    attackUser = None
    attackTarget = None

    if currentTurn == 0:
        attackUser = fighters[0]
        attackTarget = fighters[1]
        ask('Which attack do you want to use? ')
        attackChoice = input(f"Which attack do you want to use? \n :")
        if attackChoice == 'basic':
            said(basic)

        if attackChoice == "q":
            break
        
        attackChoice = attacks[attackChoice]

        attackResults = attackChoice.use(attackUser, attackTarget)

        attackUser.updateFighter(attackUser.health, attackUser.energy - attackResults[1])
        attackTarget.updateFighter(attackTarget.health - attackResults[0], attackTarget.energy)

        said(f"\n{attackUser.name} used {attackChoice.name} dealing {attackResults[0]}{'*' if attackResults[2] else ''} damage, using {attackResults[1]} energy.")

        currentTurn = 1
        continue
    
    if currentTurn == 1:
        attackUser = fighters[1]
        attackTarget = fighters[0]

        possibleAttacks = []
        for attack in list(attacks.values()):
            lowerName = attack.name.lower()

            if attack.energyUsage > attackUser.energy:
                continue

            if lowerName == "rest":
                if attackUser.energy >= (attackUser.maxEnergy / 2):
                    continue

            possibleAttacks.append(lowerName)

        attackChoice = random.choice(possibleAttacks)
        attackChoice = attacks[attackChoice]

        if attackUser.energy <= attackUser.maxEnergy / 6:
            attackChoice = attacks["rest"]

        attackResults = attackChoice.use(attackUser, attackTarget)

        attackUser.updateFighter(attackUser.health, attackUser.energy - attackResults[1])
        attackTarget.updateFighter(attackTarget.health - attackResults[0], attackTarget.energy)

        said(f"\n{attackUser.name} used {attackChoice.name} dealing {attackResults[0]}{'*' if attackResults[2] else ''} damage, using {attackResults[1]} energy.")

        currentTurn = 0
        continue

fightWinner = None

if fighters[1].health == 0:
    fightWinner = fighters[0]

if fighters[0].health == 0:
    fightWinner = fighters[1]

said(f"\n{fightWinner.name} won the fight!")