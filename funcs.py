import random

from barbarian import Barbarian, barbarian_fight
from bard import Bard, bard_fight
from fighter import Bow, Sword, bow_fight, sword_fight
from rogue import Assasin, assasin_fight, Thief, thief_fight
from wizard import Storms, Arcanum, arcane_fight, storm_fight

# DICE ROLL FUNCTIONS#################################


def d20(min_roll):
    roll = random.randint(min_roll, 20)
    return roll


def d16(min_roll):
    roll = random.randint(min_roll, 16)
    return roll


def d12(min_roll):
    roll = random.randint(min_roll, 12)
    return roll


def d8(min_roll):  # method for rolling an 8 sided die
    roll = random.randint(min_roll, 8)
    return roll


def d6(min_roll):  # method for rolling an 6 sided die
    roll = random.randint(min_roll, 6)
    return roll


def d4(min_roll):  # method for rolling an 4 sided die
    roll = random.randint(min_roll, 4)
    return roll
# END DICE ROLL FUNCTIONS##############################

# Function that serves as the battle loop######################################


def battle(player, enemy):
    if(isinstance(player, Barbarian)):
        barbarian_fight(player, enemy)
    if(isinstance(player, Bard)):
        bard_fight(player, enemy)
    if(isinstance(player, Bow)):
        bow_fight(player, enemy)
    if(isinstance(player, Sword)):
        sword_fight(player, enemy)
    if(isinstance(player, Assasin)):
        assasin_fight(player, enemy)
    if(isinstance(player, Thief)):
        thief_fight(player, enemy)
    elif(isinstance(player, Storms)):
        storm_fight(player, enemy)
    elif(isinstance(player, Arcanum)):
        arcane_fight(player, enemy)
