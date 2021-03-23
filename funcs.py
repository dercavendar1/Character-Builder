import json
import pickle
import random

from barbarian import *
from bard import *
from character import *
from fighter import *
from rogue import *
from wizard import *

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

# General Functions#############################################################
# Function that serves as the battle loop#######################################


def battle(player, enemy):
# Battle Loop for both Barbarian Classes########################################
    if(isinstance(player, Barbarian)):
        barbarian_fight(player, enemy)
# Battle Loop for Bard##########################################################
    if(isinstance(player, Bard)):
        bard_fight(player, enemy)
#  Battle Loop for Bow Fighter##################################################
    if(isinstance(player, Bow)):
        bow_fight(player, enemy)
# Battle Loop for Sword Fighter#################################################
    if(isinstance(player, Sword)):
        sword_fight(player, enemy)
# Battle Loop for Assasin#######################################################
    if(isinstance(player, Assasin)):
        assasin_fight(player, enemy)
# Battle Loop for Thief#########################################################
    if(isinstance(player, Thief)):
        thief_fight(player, enemy)
# Battle Loop for Storm Sub Class Wizard########################################
    elif(isinstance(player, Storms)):
        storm_fight(player, enemy)
# Battle Loop for Arcane Wizard#################################################
    elif(isinstance(player, Arcanum)):
        arcane_fight(player, enemy)
#End Battle Loop Function#######################################################
