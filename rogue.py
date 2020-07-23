import math
import random

import dice
from character import Character


class Rogue(Character):

    """Sub Class for Rogues adds attr for sub class of Rogue character"""

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):

        super().__init__(strength, constitution, dexterity,
                         intelligence, wisdom, charisma)
        if self.dexterity < 13:
            self.dexterity = 13
        self.hp = (8 + self.conMod)

    def getStats(self):
        stats = super().getStats()
        return stats

    def levelUP(self):
        self.hp = self.hp + (dice.d8(1) + self.conMod)
        self.level += 1


class Assasin(Rogue):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.strength = strength + 1
        self.dexterity = dexterity + 2
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

        self.stealth_flag = false

    def getStats(self):
        stats = super().getStats()
        stats['SubClass'] = 'Assasin'
        return stats

    def stealth_attack(self):
        if(self.stealth_flag == False):
            damage = (dice.d8(1) + dice.d8(1) + dice.d8(1)) + \
                self.strMod + self.dexMod
        else:
            damage = 0
        return damage


class Thief(Rogue):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.dexterity = dexterity + 3
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['SubClass'] = 'Thief'
        return stats

    def finesseWeaponAttack(self, hit, evade):
        if hit > (evade / 2):
            damage = (dice.d4(1) + dice.d4(1)) + self.dexMod
        else:
            damage = dice.d4(1) + self.dexMod
        return damage
