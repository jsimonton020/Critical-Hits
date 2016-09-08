#!/usr/bin/python3
import random
import sys

CRIT = 6

def dice_roll():
    dice_numbers = []
    dice = random.randint(1,6)
    dice_numbers.append(dice)
    while dice == CRIT:
        dice = random.randint(1,6)
        dice_numbers.append(dice)
    return dice_numbers

while True:
    print("Welcome to Critical Hits!")
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        print(dice_roll())
    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()
    else:
        print("\nPlease choose from the list\n")


#dice_roll()
#print(dice_numbers)

#hit = (sum(dice_numbers))
#print("You hit for", + hit)
