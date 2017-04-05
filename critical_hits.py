#!/usr/bin/python3
from classes import (initialize, save_game, character_roll, down,
                     died, draw)
import os

player, enemy_list = initialize()
enemy = enemy_list.pop()


while True:
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
        elif player.hp <= 0 and enemy.hp > 0:
            enemy_list = died(player, enemy, enemy_list)
            enemy = enemy_list.pop()
        elif player.hp <= 0 and enemy.hp <= 0:
            enemy_list = draw(player, enemy, enemy_list)
            enemy = enemy_list.pop()

    elif choice == "2":
        save_game(player, enemy, enemy_list)

    else:
        os.system('clear')
        print("\nPlease choose from the list\n")
