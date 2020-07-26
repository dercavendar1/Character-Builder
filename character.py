import math
import random

import funcs


class Character():

    """Character class used to hold relevant stats for DnD character"""

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):
        """[initiliazes charachter with stats]

        Args:
            strength ([int]): physical strength, determines strength damage and feats of strength
            constitution ([int]): hardiness, determines HP and fortitude saves
            dexterity ([int]): agility, determines finesse damage and dodging
            intelligence ([int]): smartness, determines certain spell damage and saves against intelligence spells
            wisdom ([int]): wisdom, determines some spell damage and saves against wisdom spells
            charisma ([int]): likeableness, determines certain spell damage and saves against charming etc.
        """
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.exp = 0
        self.level = 1
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)
        self.hp = 6 + self.conMod
# total modifiers
        self.totalMods = (self.strMod + self.conMod +
                          self.dexMod + self.intMod + self.wisMod + self.chaMod)

    def levelUP(self):
        self.hp = self.hp + (dice.d6(1) + self.conMod)
        self.level += 1

    def getStats(self):
        return {"Level": self.level,
                "Health": self.hp,
                "Strength": self.strength,
                "Constitution": self.constitution,
                "Dexterity": self.dexterity,
                "Intelligence": self.intelligence,
                "Wisdom": self.wisdom,
                "Charisma": self.charisma}

    def unarmedAttack(self, hit, evade):
        if hit > evade:
            damage = (dice.d4(1)) + self.strMod
        else:
            damage = 0
        return damage

    def heavyWeaponAttack(self, hit, evade):
        if hit > evade:
            damage = (dice.d8(1)) + self.strMod
        else:
            damage = 0
        return damage

    def finesseWeaponAttack(self, hit, evade):
        if hit > evade:
            damage = (dice.d4(1) + dice.d4(1)) + self.dexMod
        else:
            damage = 0
        return damage
