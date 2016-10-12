#!/usr/bin/python3
import random
import sys
import os

CRIT = 6
gen_hp = random.randint(50, 100)


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def dice_roll(self):
        dice_numbers = []
        dice = random.randint(1, 6)
        dice_numbers.append(dice)
        while dice == CRIT:
            dice = random.randint(1, 6)
            dice_numbers.append(dice)
        return dice_numbers

player = Character("Player", gen_hp)
enemy = Character("Enemy", gen_hp)

os.system('clear')
print("\nWelcome to Critical Hits!\n")

while True:
    print("\n")
    print(enemy.name, "hit points:", enemy.hp)
    print(player.name, "hit points:", player.hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        os.system('clear')
        p_roll = player.dice_roll()
        print(p_roll)
        print(player.name, "hit for", sum(p_roll))
        if sum(p_roll) >= 6 and sum(p_roll) < 12:
            print("CRITICAL HIT!")
        if sum(p_roll) >= 12 and sum(p_roll) < 18:
            print("MEGA HIT!")
        if sum(p_roll) >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        enemy.hp = enemy.hp - sum(p_roll)

        e_roll = enemy.dice_roll()
        print("\n")
        print(e_roll)
        print(enemy.name, "hit for", sum(e_roll))
        if sum(e_roll) >= 6 and sum(e_roll) < 12:
            print("CRITICAL HIT!")
        if sum(e_roll) >= 12 and sum(e_roll) < 18:
            print("MEGA HIT!")
        if sum(e_roll) >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        player.hp = player.hp - sum(e_roll)

        if enemy.hp <= 0 and player.hp > 0:
            print(enemy.name, "Down!\n")
            print(player.name, "hit points:", player.hp)
            break

        if player.hp <= 0 and enemy.hp > 0:
            print("\nYou died!\n")
            print(enemy.name, "hit points:", enemy.hp)
            break

        if player.hp and enemy.hp <= 0:
            print("\nDraw!\n")
            print(player.name, "hit points: 0")
            print(enemy.name, "hit points: 0")
            break

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()
    else:
        os.system('clear')
        print("\nPlease choose from the list\n")


def restart_p():
    restart = input("Would you like to play again? >")
    if restart == "yes" or restart == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif restart == "no" or restart == "n":
        print("Closing Critical Hits")
        sys.exit()
    else:
        print("invalid input")
        restart_p()
restart_p()
