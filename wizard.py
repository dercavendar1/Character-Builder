import math
import random

import dice
from character import Character


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
        stats['College'] = 'College of Storms'
        stats['Magic Slots'] = self.magic_slots
        return stats

    def levelUP(self):
        self.hp = self.hp + (dice.d6(1) + self.conMod)
        self.level += 1
        self.magic_slots += 1

    def lightning_bolt(self, hit, evade, enemyMod):
        if ((hit > evade + enemyMod) and self.magic_slots > 0):
            damage = (dice.d6(1) + dice.d6(1) +
                      dice.d6(1) + dice.d6(1)) + self.intMod
            self.magic_slots -= 1
        elif((hit <= evade + enemyMod) and self.magic_slots > 0):
            damage = (dice.d6(1) + dice.d6(1)) + self.intMod
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
        stats['College'] = 'College of Arcane Magics'
        stats['Magic Slots'] = self.magic_slots
        return stats

    def fireball(self, hit, evade, enemyMod):
        if ((hit > evade + enemyMod) and self.magic_slots > 0):
            damage = (dice.d4(1) + dice.d4(1) + dice.d4(1) +
                      dice.d4(1) + dice.d4(1) + dice.d4(1)) + self.intMod
            self.magic_slots -= 1
        elif((hit <= evade + enemyMod) and self.magic_slots > 0):
            damage = ((dice.d4(1) + dice.d4(1) + dice.d4(1)) + self.intMod)
            self.magic_slots -= 1
        elif(self.magic_slots <= 0):
            print("no magic left")
            damage = 0
        return damage

    def levelUP(self):
        self.hp = self.hp + (dice.d6(1) + self.conMod)
        self.level += 1
        self.magic_slots += 1
