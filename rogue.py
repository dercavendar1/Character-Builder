import math
import random

import dice
from character import Character


def assasin_fight():
    while (player.hp > 0 and enemy.hp > 0):

        if(player.stealth_flag == True):
            print('Stealth Attack First Strike!')
            enemy.hp -= player.stealth_attack()
            print(enemy.hp)
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


def thief_fight:
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
        self.stealth_flag = False


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

        self.stealth_flag = False

    def getStats(self):
        stats = super().getStats()
        stats['SubClass'] = 'Assasin'
        return stats

    def stealth_attack(self):
        if(self.stealth_flag == False):
            damage = (dice.d8(1) + dice.d8(1) + dice.d8(1)) + \
                self.strMod + self.dexMod
            self.Stealth_flag = True
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
