#!/usr/bin/python3

import random

CRIT = 6
hp = random.randint(10, 50)

class Character:
    def __init__(self):
        self.name = ""
        self.health = ""
        self.health_max = ""
    def dice_roll():
        dice_numbers = []
        dice = random.randint(1,6)
        dice_numbers.append(dice)
        while dice == CRIT:
            dice = random.randint(1,6)
            dice_numbers.append(dice)
        return dice_numbers

class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = ""
        self.health = random.randint(1, player.health)

class Player(Character):
    def __init__(self):
        self.state = ""
        self.health = ""
        self.health_max = ""
