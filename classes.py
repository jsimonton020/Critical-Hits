#!/usr/bin/python3
import random
import os
import sys

class Character:
    def __init__(self, name, hp, dice, points=0):
        self.name = name
        self.hp = hp
        self.dice = dice
        self.points = points
    def roll(self):
        damage = 0
        for d in self.dice:
            roll = d.dice_roll()
            print(roll)
            damage += sum(roll)
        return damage

class Dice:
    def __init__(self, sides):
        self.sides = sides
    def dice_roll(self):
        dice_numbers = []
        dice = random.randint(1, self.sides)
        dice_numbers.append(dice)
        while dice == self.sides:
            dice = random.randint(1, self.sides)
            dice_numbers.append(dice)
        return dice_numbers

def d_bag(sides, amount):
    bag = []
    for i in range(0, amount):
        d = Dice(sides)
        bag.append(d)
    return bag

def set_enemies():
    slime_dice = d_bag(6,1)
    slime = Character("Slime", 20, slime_dice)

    bat_dice = d_bag(6,2)
    bat = Character("Bat", 35, bat_dice)

    gob_dice = d_bag(8,1)
    goblin = Character("Goblin", 50, gob_dice)

    hob_dice = d_bag(8,2)
    hobgob = Character("Hobgoblin", 65, hob_dice)

    orc_dice = d_bag(10,1)
    orc = Character("Orc", 80, orc_dice)

    troll_dice = d_bag(10,2)
    troll = Character("Cave Troll", 95, troll_dice)

    owl_dice = d_bag(12,1)
    owlbear = Character("Owlbear", 110, owl_dice)

    chim_dice = d_bag(12,2)
    chimera = Character("Chimera", 125, chim_dice)

    giant_dice = d_bag(20,1)
    giant = Character("Giant", 140, giant_dice)

    drag_dice = d_bag(20,2)
    dragon = Character("Dragon", 155, drag_dice)

    e = [dragon, giant, chimera, owlbear,
         troll, orc, hobgob, goblin, bat, slime]
    return e

#def set_player():
#    hp =
#    points =
#    sides =
#    amount =
#    play_dice = d_bag(sides, amount)
#    player = Character("Player", hp, play_dice, points)
