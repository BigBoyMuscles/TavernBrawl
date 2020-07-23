import math
import random

import dice
from character import Character


class Fighter(Character):

    """Sub Class for Fighter adds attr for sub class of fighter character"""

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):
        """initialize fighter character see __init__ for character class

        Args:
            subclass ([string]): the fighter subclass chosen
        """
        super().__init__(strength, constitution, dexterity,
                         intelligence, wisdom, charisma)
        if self.strength < 13:
            self.strength = 13
        self.hp = (8 + self.conMod)

    def getStats(self):
        stats = super().getStats()
        return stats

    def levelUP(self):
        self.hp = self.hp + (dice.d8(1) + self.conMod)
        self.level += 1


class Sword(Fighter):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.strength = strength + 3
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['Weapon'] = 'Sword'
        return stats

    def heavyWeaponAttack(self, hit, evade):
        if hit > (evade / 2):
            damage = (dice.d8(1)) + self.strMod
        else:
            damage = dice.d4(1) + self.strMod
        return damage


class Bow(Fighter):
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
        stats['Weapon'] = 'Bow'
        return stats

    def finesseWeaponAttack(self, hit, evade):
        if hit > (evade / 2):
            damage = (dice.d4(1) + dice.d4(1)) + self.dexMod
        else:
            damage = dice.d4(1) + self.dexMod
        return damage
