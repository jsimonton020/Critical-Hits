#!/usr/bin/python3
from classes import Character, Dice, d_bag, set_enemies
import random
import os
import sys

play_dice = d_bag(6,1)
player = Character("Player", 50, play_dice, 0)
enemy_list = set_enemies()
enemy = enemy_list.pop()

os.system('clear')
print("\nWelcome to Critical Hits!\n")
print("You have", player.points, "points.")

while True:
    print("\n")
    print(enemy.name, "hit points:", enemy.hp)
    print(player.name, "hit points:", player.hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        os.system('clear')

        p_roll = player.roll()
        print(player.name, "hit for", p_roll)
        if p_roll >= 6 and p_roll < 12:
            print("CRITICAL HIT!")
        if p_roll >= 12 and p_roll < 18:
            print("MEGA HIT!")
        if p_roll >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        enemy.hp -= p_roll

        e_roll = enemy.roll()
        print(enemy.name, "hit for", e_roll)
        if e_roll >= 6 and e_roll < 12:
            print("CRITICAL HIT!")
        if e_roll >= 12 and e_roll < 18:
            print("MEGA HIT!")
        if e_roll >= 18:
            print("M-M-M-M-M-MONSTER HIT!")
        player.hp -= e_roll

        if enemy.hp <= 0 and player.hp > 0:
            print(enemy.name, "Down!\n")
            print(player.name, "hit points:", player.hp)
            if len(enemy_list) == 0:
                print("You have defeated all the enemies!")
                break
            else:
                enemy = enemy_list.pop()
                print("\nA new enemy approaches!")

        if player.hp <= 0 and enemy.hp > 0:
            print("\nYou died!\n")
            print(enemy.name, "hit points:", enemy.hp)
            count = len(enemy_list)
            print(count, "enemies left.")
            if count == 9:
                player.points += 1
            elif count == 8:
                player.points += 2
            elif count == 7:
                player.points += 3
            elif count == 6:
                player.points += 4
            elif count == 5:
                player.points += 5
            elif count == 4:
                player.points += 6
            elif count == 3:
                player.points += 7
            elif count == 2:
                player.points += 8
            elif count == 1:
                player.points += 9
            print(player.points, "points gained")
            break

        if player.hp and enemy.hp <= 0:
            print("\nDraw!\n")
            print(player.name, "hit points: 0")
            print(enemy.name, "hit points: 0")
            count = len(enemy_list)
            print(count, "enemies left.")
            if count == 9:
                player.points += 1
            elif count == 8:
                player.points += 2
            elif count == 7:
                player.points += 3
            elif count == 6:
                player.points += 4
            elif count == 5:
                player.points += 5
            elif count == 4:
                player.points += 6
            elif count == 3:
                player.points += 7
            elif count == 2:
                player.points += 8
            elif count == 1:
                player.points += 9
            print(player.points, "points gained")
            break

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()

    else:
        os.system('clear')
        print("\nPlease choose from the list\n")
