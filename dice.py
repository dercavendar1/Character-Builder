import random


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
