import math
import random

import funcs
from character import Character


def storm_fight(player, enemy):
    while (player.hp > 0 and enemy.hp > 0):
        attack_type = input("Unarmed or Lightning Bolt? ")
        if(attack_type.lower() == 'bolt' or attack_type.lower() == 'lightning' or attack_type.lower() == 'magic'):
            hit = funcs.d20(1)
            evade = funcs.d20(1) + enemy.dexMod
            enemy.hp = enemy.hp - \
                player.lightning_bolt(hit, evade, enemy.dexMod)
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
        print('Your Health ', player.hp)
        print('Enemy Health ', enemy.hp)


def arcane_fight(player, enemy):
    while (player.hp > 0 and enemy.hp > 0):
        attack_type = input("Unarmed or Fireball? ")
        if(attack_type.lower() == 'ball' or attack_type.lower() == 'fireball' or attack_type.lower() == 'magic'):
            hit = funcs.d20(1)
            evade = funcs.d20(1) + enemy.dexMod
            enemy.hp = enemy.hp - \
                player.fireball(hit, evade, enemy.dexMod)
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
        print('Your Health ', player.hp)
        print('Enemy Health ', enemy.hp)


class Wizard(Character):

    def __init__(self, strength, constitution, dexterity,
                 intelligence, wisdom, charisma):

        super().__init__(strength, constitution, dexterity,
                         intelligence, wisdom, charisma)
        if self.intelligence < 13:
            self.intelligence = 13

    def getStats(self):
        stats = super().getStats()
        return stats


class Storms(Wizard):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.intelligence = intelligence + 2
        self.wisdom = wisdom + 1
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)
        self.magic_slots = 2

    def getStats(self):
        stats = super().getStats()
        stats = f'SubClass= Storm Wizard\n' + stats + \
            f'\n|Magic Slots    |{self.magic_slots}|\n--------------------'
        return stats

    def levelUP(self):
        self.hp = self.hp + (funcs.d6(1) + self.conMod)
        self.level += 1
        self.magic_slots += 1

    def lightning_bolt(self, hit, evade, enemyMod):
        if ((hit > evade + enemyMod) and self.magic_slots > 0):
            damage = (funcs.d6(1) + funcs.d6(1) +
                      funcs.d6(1) + funcs.d6(1)) + self.intMod
            self.magic_slots -= 1
        elif((hit <= evade + enemyMod) and self.magic_slots > 0):
            damage = (funcs.d6(1) + funcs.d6(1)) + self.intMod
            self.magic_slots -= 1
        elif(self.magic_slots <= 0):
            print("no magic left")
            damage = 0
        return damage


class Arcanum(Wizard):
    def __init__(self, strength, constitution, dexterity, intelligence, wisdom, charisma):
        super().__init__(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.intelligence = intelligence + 3
        self.strMod = int(float(self.strength - 10) / 2)
        self.conMod = int(float(self.constitution - 10) / 2)
        self.dexMod = int(float(self.dexterity - 10) / 2)
        self.intMod = int(float(self.intelligence - 10) / 2)
        self.wisMod = int(float(self.wisdom - 10) / 2)
        self.chaMod = int(float(self.charisma - 10) / 2)
        self.magic_slots = 2

    def getStats(self):
        stats = super().getStats()
        stats = f'SubClass= Arcane Wizard\n' + stats + \
            f'\n|Magic Slots    |{self.magic_slots}|\n--------------------'
        return stats

    def fireball(self, hit, evade, enemyMod):
        if ((hit > evade + enemyMod) and self.magic_slots > 0):
            damage = (funcs.d4(1) + funcs.d4(1) + funcs.d4(1) +
                      funcs.d4(1) + funcs.d4(1) + funcs.d4(1)) + self.intMod
            self.magic_slots -= 1
        elif((hit <= evade + enemyMod) and self.magic_slots > 0):
            damage = ((funcs.d4(1) + funcs.d4(1) + funcs.d4(1)) + self.intMod)
            self.magic_slots -= 1
        elif(self.magic_slots <= 0):
            print("no magic left")
            damage = 0
        return damage

    def levelUP(self):
        self.hp = self.hp + (funcs.d6(1) + self.conMod)
        self.level += 1
        self.magic_slots += 1
