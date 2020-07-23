import json
import pickle
import random

from barbarian import *
from bard import *
from character import *
from dice import *
from fighter import *
from rogue import *
from wizard import *

# Function that serves as the battle loop#######################################


def battle(player, enemy):
    # Battle Loop for both Barbarian Classes####################################
    if(isinstance(player, Barbarian)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.heavyWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################


# Battle Loop for Bard##########################################################
    if(isinstance(player, Bard)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.finesseWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

#  Battle Loop for Bow Fighter##################################################
    if(isinstance(player, Bow)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.finesseWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(10) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

# Battle Loop for Sword Fighter#################################################
    if(isinstance(player, Sword)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.heavyWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

# Battle Loop for Assasin#######################################################
    if(isinstance(player, Assasin)):
        while (player.hp > 0 and enemy.hp > 0):
            print('Stealth Attack First Strike!')
            enemy.hp -= player.stealth_attack()
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.finesseWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

# Battle Loop for Thief#########################################################
    if(isinstance(player, Thief)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Armed? ")
            if(attack_type.lower() == 'armed'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.finesseWeaponAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

# Battle Loop for Storm Sub Class Wizard########################################
    elif(isinstance(player, Storms)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Lightning Bolt? ")
            if(attack_type.lower() == 'bolt' or attack_type.lower == 'lightning bolt' or attack_type.lower == 'lightning'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - \
                    player.lightning_bolt(hit, evade, enemy.dexMod)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])
################################################################################

# Battle Loop for Arcane Wizard#################################################
    elif(isinstance(player, Arcanum)):
        while (player.hp > 0 and enemy.hp > 0):
            attack_type = input("Unarmed or Fireball? ")
            if(attack_type.lower() == 'fire' or attack_type.lower == 'fireball' or attack_type.lower == 'ball'):
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - \
                    player.fireball(hit, evade, enemy.dexMod)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            else:
                hit = dice.d20(1)
                evade = dice.d20(1) + enemy.dexMod
                enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
                hit = dice.d20(1)
                evade = dice.d20(1) + player.dexMod
                player.hp = player.hp - enemy.unarmedAttack(hit, evade)
            print('Your Health ', player.getStats()["Health"])
            print('Enemy Health ', enemy.getStats()["Health"])


################################################################################
load = input('Would you like to load your last saved character? ')
# Load Previously Saved Character###############################################
if (load == 'yes'):
    try:
        file = open('savedcharacter.obj', 'rb')
        player = pickle.load(file)
    except:
        # TODO: Figure Out How to handle no file exception without rewriting entire character creation block in the exception

        print("No Saved Data Creating a Base Character\n")
        error = True
        strength = dice.d20(8)
        constitution = dice.d20(10)
        dexterity = dice.d20(8)
        wisdom = dice.d20(8)
        intelligence = dice.d20(8)
        charisma = dice.d20(8)

        player = Character(strength, constitution, dexterity,
                           intelligence, wisdom, charisma)
        print(player.getStats())

    #Allows user to choose what class their character is and resets character#####
        characterClass = None
        while characterClass not in ('bard', 'wizard', 'fighter', 'rogue', 'barbarian'):
            characterClass = input(
                'What Class Do You Want (Barbarian, Bard, Fighter, Rogue, or Wizard)? ').lower()
    ###############################################################################

    # Branching Paths that allow user to choose sub class appropriate to chosen class
    # Barbarian Class Branch########################################################
        if (characterClass.lower() == 'barbarian'):
            player = Barbarian(player.strength, player.constitution, player.dexterity,
                               player.intelligence, player.wisdom, player.charisma)
            print(player.getStats())
            answer = None
            while answer not in ("totem", "tank"):
                answer = input("What Sub Class (Totem or Tank): ").lower()
                if(answer == "totem"):
                    player = Totem(player.strength, player.constitution, player.dexterity,
                                   player.intelligence, player.wisdom, player.charisma)
                elif(answer == "tank"):
                    player = Tank(player.strength, player.constitution, player.dexterity,
                                  player.intelligence, player.wisdom, player.charisma)
                else:
                    print("Please enter Totem or Tank.")
    ################################################################################

    # Bard Class Branch#############################################################
        if (characterClass.lower() == 'bard'):
            player = Bard(player.strength, player.constitution, player.dexterity,
                          player.intelligence, player.wisdom, player.charisma)
            print(player.getStats())
            answer = None
            while answer not in ("eloquent", "valor"):
                answer = input("What Sub Class (Eloquent or Valor): ").lower()
                if(answer == "eloquent"):
                    player = Eloquent(player.strength, player.constitution, player.dexterity,
                                      player.intelligence, player.wisdom, player.charisma)
                elif(answer == "valor"):
                    player = Valor(player.strength, player.constitution, player.dexterity,
                                   player.intelligence, player.wisdom, player.charisma)
                else:
                    print("Please enter Eloquent or Valor.")
    ################################################################################

    # Fighter Class  Branch#########################################################
        if (characterClass.lower() == 'fighter'):
            player = Fighter(player.strength, player.constitution, player.dexterity,
                             player.intelligence, player.wisdom, player.charisma)
            print(player.getStats())
            answer = None
            while answer not in ("sword", "bow"):
                answer = input("What Sub Class (Sword or Bow): ").lower()
                if(answer == "sword"):
                    player = Sword(player.strength, player.constitution, player.dexterity,
                                   player.intelligence, player.wisdom, player.charisma)
                elif(answer == "bow"):
                    player = Bow(player.strength, player.constitution, player.dexterity,
                                 player.intelligence, player.wisdom, player.charisma)
                else:
                    print("Please enter Sword or Bow.")
    ################################################################################

    # Rogue Class Branch############################################################
        if (characterClass.lower() == 'rogue'):
            player = Rogue(player.strength, player.constitution, player.dexterity,
                           player.intelligence, player.wisdom, player.charisma)
            print(player.getStats())
            answer = None
            while answer not in ("assasin", "thief"):
                answer = input("What Sub Class (Assasin or Thief): ").lower()
                if(answer == "sword"):
                    player = Assasin(player.strength, player.constitution, player.dexterity,
                                     player.intelligence, player.wisdom, player.charisma)
                elif(answer == "bow"):
                    player = Thief(player.strength, player.constitution, player.dexterity,
                                   player.intelligence, player.wisdom, player.charisma)
                else:
                    print("Please enter Assasin or Thief.")
    ################################################################################

    # Wizard Class Branch###########################################################
        if (characterClass.lower() == 'wizard'):
            player = Wizard(player.strength, player.constitution, player.dexterity,
                            player.intelligence, player.wisdom, player.charisma)
            print(player.getStats())
            answer = None
            while answer not in ("arcane", "storm"):
                answer = input("What Speciality (Arcane or Storm): ").lower()
                if(answer == "arcane"):
                    player = Arcanum(player.strength, player.constitution, player.dexterity,
                                     player.intelligence, player.wisdom, player.charisma)
                elif(answer == "storm"):
                    player = Storms(player.strength, player.constitution, player.dexterity,
                                    player.intelligence, player.wisdom, player.charisma)
                else:
                    print("Please enter Arcane or Storm.")

    #lets player set a starting level ##############################################
            levels = int(input("What Level do you want to start from? "))

            for i in range(1, levels):
                player.levelUP()
                enemy.levelUP()
################################################################################
# End Of Character Creation Branches############################################

# Initial Character Creation with Random stats##################################

else:
    strength = dice.d20(8)
    constitution = dice.d20(10)
    dexterity = dice.d20(8)
    wisdom = dice.d20(8)
    intelligence = dice.d20(8)
    charisma = dice.d20(8)

    player = Character(strength, constitution, dexterity,
                       intelligence, wisdom, charisma)
    print(player.getStats())

#Allows user to choose what class their character is and resets character#####
    characterClass = None
    while characterClass not in ('bard', 'wizard', 'fighter', 'rogue', 'barbarian'):
        characterClass = input(
            'What Class Do You Want (Barbarian, Bard, Fighter, Rogue, or Wizard)? ').lower()
###############################################################################

# Branching Paths that allow user to choose sub class appropriate to chosen class

# Barbarian Class Branch########################################################
    if (characterClass.lower() == 'barbarian'):
        player = Barbarian(player.strength, player.constitution, player.dexterity,
                           player.intelligence, player.wisdom, player.charisma)
        print(player.getStats())
        answer = None
        while answer not in ("totem", "tank"):
            answer = input("What Sub Class (Totem or Tank): ").lower()
            if(answer == "totem"):
                player = Totem(player.strength, player.constitution, player.dexterity,
                               player.intelligence, player.wisdom, player.charisma)
            elif(answer == "tank"):
                player = Tank(player.strength, player.constitution, player.dexterity,
                              player.intelligence, player.wisdom, player.charisma)
            else:
                print("Please enter Totem or Tank.")
################################################################################

# Bard Class Branch#############################################################
    if (characterClass.lower() == 'bard'):
        player = Bard(player.strength, player.constitution, player.dexterity,
                      player.intelligence, player.wisdom, player.charisma)
        print(player.getStats())
        answer = None
        while answer not in ("eloquent", "valor"):
            answer = input("What Sub Class (Eloquent or Valor): ").lower()
            if(answer == "eloquent"):
                player = Eloquent(player.strength, player.constitution, player.dexterity,
                                  player.intelligence, player.wisdom, player.charisma)
            elif(answer == "valor"):
                player = Valor(player.strength, player.constitution, player.dexterity,
                               player.intelligence, player.wisdom, player.charisma)
            else:
                print("Please enter Eloquent or Valor.")
################################################################################

# Fighter Class  Branch#########################################################
    if (characterClass.lower() == 'fighter'):
        player = Fighter(player.strength, player.constitution, player.dexterity,
                         player.intelligence, player.wisdom, player.charisma)
        print(player.getStats())
        answer = None
        while answer not in ("sword", "bow"):
            answer = input("What Sub Class (Sword or Bow): ").lower()
            if(answer == "sword"):
                player = Sword(player.strength, player.constitution, player.dexterity,
                               player.intelligence, player.wisdom, player.charisma)
            elif(answer == "bow"):
                player = Bow(player.strength, player.constitution, player.dexterity,
                             player.intelligence, player.wisdom, player.charisma)
            else:
                print("Please enter Sword or Bow.")
################################################################################

# Rogue Class Branch############################################################
    if (characterClass.lower() == 'rogue'):
        player = Rogue(player.strength, player.constitution, player.dexterity,
                       player.intelligence, player.wisdom, player.charisma)
        print(player.getStats())
        answer = None
        while answer not in ("assasin", "thief"):
            answer = input("What Sub Class (Assasin or Thief): ").lower()
            if(answer == "sword"):
                player = Assasin(player.strength, player.constitution, player.dexterity,
                                 player.intelligence, player.wisdom, player.charisma)
            elif(answer == "bow"):
                player = Thief(player.strength, player.constitution, player.dexterity,
                               player.intelligence, player.wisdom, player.charisma)
            else:
                print("Please enter Assasin or Thief.")
################################################################################

# Wizard Class Branch###########################################################
    if (characterClass.lower() == 'wizard'):
        player = Wizard(player.strength, player.constitution, player.dexterity,
                        player.intelligence, player.wisdom, player.charisma)
        print(player.getStats())
        answer = None
        while answer not in ("arcane", "storm"):
            answer = input("What Speciality (Arcane or Storm): ").lower()
            if(answer == "arcane"):
                player = Arcanum(player.strength, player.constitution, player.dexterity,
                                 player.intelligence, player.wisdom, player.charisma)
            elif(answer == "storm"):
                player = Storms(player.strength, player.constitution, player.dexterity,
                                player.intelligence, player.wisdom, player.charisma)
            else:
                print("Please enter Arcane or Storm.")

#lets player set a starting level ##############################################
        levels = int(input("What Level do you want to start from? "))

        for i in range(1, levels):
            player.levelUP()
            enemy.levelUP()
################################################################################
# End Of Character Creation Branches############################################

#Creates an enemy with reduced possible stats###################################
strength = dice.d16(8)
constitution = dice.d16(8)
dexterity = dice.d16(8)
intelligence = dice.d16(8)
wisdom = dice.d16(8)
charisma = dice.d16(8)

enemy = Character(strength, constitution, dexterity,
                  intelligence, wisdom, charisma)

while(enemy.level < player.level):
    enemy.levelUP()
################################################################################

print(player.getStats(), '\n')
print(enemy.getStats(), '\n')

battle(player, enemy)

if (player.hp > enemy.hp):
    print("\nYou Win")
    modDiff = (enemy.totalMods / player.totalMods)
    expGained = int(300 * modDiff)
    player.exp = player.exp + expGained
    print(
        f'You Got {expGained} EXP!!! only {(player.level * 300) - player.exp} left to the next level!')
else:
    print("\nYou Lose")

if(player.exp >= (player.level * 300)):
    while(player.exp >= (player.level * 300)):
        player.levelUP()

# Saves current character#######################################################
savecharacter = input('Do you want to save this character? ')
if(savecharacter.lower() == 'yes'):
    file = open(b"savedcharacter.obj", "wb")
    pickle.dump(player, file)

# TODO: Format the Character sheet for organized presentation
# Creates a printable character sheet###########################################
# characterSheet = input('Do you want a printable Character Sheet? ')
# characterSheet = open(r"Character Sheet", "a")
# characterSheet.write(json.dumps(player.getStats()))
# characterSheet.close()
