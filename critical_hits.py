#!/usr/bin/python3
from classes import (set_enemies, set_player, character_roll, down,
                     died, draw)
import os
import sys

player = set_player()
enemy_list = set_enemies()
enemy = enemy_list.pop()


os.system('clear')
print("\nWelcome to Critical Hits!\n")
print("You have", player.points, "points.")

while len(enemy_list) > 0:
    print(enemy.name, "hit points:", enemy.hp)
    print(player.name, "hit points:", player.hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        os.system('clear')
        character_roll(player, enemy)
        if enemy.hp <= 0 and player.hp > 0:
            enemy = down(player, enemy, enemy_list)
        if player.hp <= 0 and enemy.hp > 0:
            enemy_list = died(player, enemy, enemy_list)
            enemy = enemy_list.pop()
        if player.hp <= 0 and enemy.hp <= 0:
            enemy_list = draw(player, enemy, enemy_list)
            enemy = enemy_list.pop()

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()

    else:
        os.system('clear')
        print("\nPlease choose from the list\n")
