#!/usr/bin/python3
import random
import sys

CRIT = 6
hp = 50

def dice_roll():
    dice_numbers = []
    dice = random.randint(1,6)
    dice_numbers.append(dice)
    while dice == CRIT:
        dice = random.randint(1,6)
        dice_numbers.append(dice)
    return dice_numbers

print("\nWelcome to Critical Hits!\n")

while True:
    print("\nTarget hit points:", + hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        d6 = dice_roll()
        print(d6)
        print("You hit for", sum(d6))
        hp = hp - sum(d6)
        if hp <= 0:
                print("\nEnemy Down!\n")
                break
    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()
    else:
        print("\nPlease choose from the list\n")
