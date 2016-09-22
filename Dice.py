#!/usr/bin/python3

import random
import os
import sys

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
    def roll(self):
        dice = (random.randint(1, self.sides))
        return dice

d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)

print("Which Roll:")
print("1: d6")
print("2: d8")
print("3: d10")
print("4: d12")
print("5: d20")

choice = input(">")
if choice == "1":
    print(d6.roll())
elif choice == "2":
    print(d8.roll() + 4)
elif choice == "3":
    print(d10.roll())
elif choice == "4":
    print(d12.roll())
elif choice == "5":
    print(d20.roll() + 4)
else:
    os.execl(sys.executable, sys.executable, *sys.argv)


os.execl(sys.executable, sys.executable, *sys.argv)
