#!/usr/bin/python3
from classes import (set_enemies, set_player, character_roll, check_down,
                     check_died, check_draw)
import os
import sys

player = set_player()
enemy_list = set_enemies()
enemy = enemy_list.pop()


os.system('clear')
print("\nWelcome to Critical Hits!\n")
print("You have", player.points, "points.")

while True:
    print(enemy.name, "hit points:", enemy.hp)
    print(player.name, "hit points:", player.hp)
    print("1: Roll")
    print("2: Quit")
    choice = input("Make a selection: ")

    if choice == "1":
        os.system('clear')
        character_roll(player, enemy)
#        check_down(player, enemy, enemy_list)
#        check_died(player, enemy, enemy_list)
#        check_draw(player, enemy, enemy_list)

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()

    else:
        os.system('clear')
        print("\nPlease choose from the list\n")
