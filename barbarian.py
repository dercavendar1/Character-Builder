import math
import random

import dice
from character import Character


def barbarian_fight():
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


class Barbarian(Character):

    """Sub Class of Character for barbarians, Adds option for sub classes"""

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):
        """initialize barbarian character see __init__ for character class"""
        super().__init__(strength, constitution, dexterity,
                         intelligence, wisdom, charisma)
        if self.constitution < 13:
            self.constitution = 13
        self.hp = (12 + self.conMod)

    def levelUP(self):
        self.hp = self.hp + (dice.d12(4) + self.conMod)
        self.level += 1

    def getStats(self):
        stats = super().getStats()
        return stats


class Totem(Barbarian):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.strength = strength + 4
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['Sub Class'] = 'Totem'
        return stats


class Tank(Barbarian):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.constitution = constitution + 4
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['Sub Class'] = 'Tank'
        return stats
