import math
import random

import funcs
from character import Character


def bard_fight(player, enemy):
    while (player.hp > 0 and enemy.hp > 0):
        attack_type = input("Unarmed or Armed? ")
        if(attack_type.lower() == 'armed'):
            hit = funcs.d20(1)
            evade = funcs.d20(1) + enemy.dexMod
            enemy.hp = enemy.hp - player.finesseWeaponAttack(hit, evade)
            hit = funcs.d20(1)
            evade = funcs.d20(1) + player.dexMod
            player.hp = player.hp - enemy.unarmedAttack(hit, evade)
        else:
            hit = funcs.d20(1)
            evade = funcs.d20(1) + enemy.dexMod
            enemy.hp = enemy.hp - player.unarmedAttack(hit, evade)
            hit = funcs.d20(1)
            evade = funcs.d20(1) + player.dexMod
            player.hp = player.hp - enemy.unarmedAttack(hit, evade)
        print('Your Health ', player.getStats()["Health"])
        print('Enemy Health ', enemy.getStats()["Health"])


class Bard(Character):

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):

        super().__init__(strength, constitution, dexterity,
                         intelligence, wisdom, charisma)
        if self.charisma < 13:
            self.charisma = 13
        self.hp = (8 + self.conMod)

    def levelUP(self):
        self.hp = self.hp + (funcs.d8(1) + self.conMod)
        self.level += 1

    def getStats(self):
        stats = super().getStats()
        return stats


class Valor(Bard):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.charisma = charisma + 1
        self.strength = strength + 1
        self.dexterity = dexterity + 1
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['College'] = 'College of Valor'
        return stats


class Eloquent(Bard):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.charisma = charisma + 3
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)

    def getStats(self):
        stats = super().getStats()
        stats['College'] = 'College of Eloquence'
        return stats
