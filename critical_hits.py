#!/usr/bin/python3
import random
import sys
import os

CRIT = 6
#gen_hp = random.randint(30, 100)
#max_gen = gen_hp

class Character:
    def __init__(self, state, name, hp, hp_max):
        self.state = state
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
    def dice_roll():
        dice_numbers = []
        dice = random.randint(1,6)
        dice_numbers.append(dice)
        while dice == CRIT:
            dice = random.randint(1,6)
            dice_numbers.append(dice)
        return dice_numbers

player = Character("normal", "player", 50, 50)
enemy = Character("normal", "enemy", 50, 50)

print("\nWelcome to Critical Hits!\n")

while True:
    print("\nTarget hit points:", enemy.hp)
    print("Player hit points:", player.hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        os.system('clear')
        p_roll = Character.dice_roll()
        print(p_roll)
        print("You hit for", sum(p_roll))
        if sum(p_roll) >= 6 and sum(p_roll) < 12:
            print("CRITICAL HIT!")
        if sum(p_roll) >= 12 and sum(p_roll) < 18:
            print("MEGA HIT!")
        if sum(p_roll) >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        enemy.hp = enemy.hp - sum(p_roll)
        e_roll = Character.dice_roll()
        print(e_roll)
        print("Enemy hit for", sum(e_roll))
        if sum(e_roll) >= 6 and sum(e_roll) < 12:
            print("CRITICAL HIT!")
        if sum(e_roll) >= 12 and sum(e_roll) < 18:
            print("MEGA HIT!")
        if sum(e_roll) >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        player.hp = player.hp - sum(e_roll)
        if enemy.hp <= 0 and player.hp > 0:
            print("\nEnemy Down!\n")
            print("Player hit points:", player.hp)
            break
        if player.hp <= 0 and enemy.hp > 0:
            print("\nYou died!\n")
            print("Enemy hit points:", enemy.hp)
            break
        if player.hp and enemy.hp <= 0:
            print("\nDraw!\n")
            print("Player hit points:", player.hp)
            print("Enemy hit points:", enemy.hp)
            break

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()
    else:
        print("\nPlease choose from the list\n")
        os.system('clear')
