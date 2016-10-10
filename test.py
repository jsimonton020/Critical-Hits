#!/usr/bin/python3
from classes import set_enemies, set_player, game_restart, spend_points, shai_surprise
import os
import sys

player = set_player()
enemy_list = set_enemies()
enemy = enemy_list.pop()


def get_points():
    count = len(enemy_list)
    points = range(9, -1, -1)
    return points[count]

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

        p_roll = player.roll()
        print(player.name, "hit for", p_roll)
        if p_roll >= 4 and p_roll < 8:
            print("CRITICAL HIT!")
        if p_roll >= 8 and p_roll < 12:
            print("MEGA HIT!")
        if p_roll >= 12:
            print("M-M-M-M-M-MONSTER HIT!")
        enemy.hp -= p_roll

        e_roll = enemy.roll()
        print(enemy.name, "hit for", e_roll)
        if e_roll >= 4 and e_roll < 8:
            print("CRITICAL HIT!")
        if e_roll >= 8 and e_roll < 12:
            print("MEGA HIT!")
        if e_roll >= 12:
            print("M-M-M-M-M-MONSTER HIT!")
        player.hp -= e_roll

        if enemy.hp <= 0 and player.hp > 0:
            print(enemy.name, "Down!\n")
            print(player.name, "hit points:", player.hp)
            if len(enemy_list) == 0:
                print("You have defeated all the enemies!")
                enemy = shai_surprise()
                print("Normal Tuesday night for", enemy.name)
                if enemy.hp <= 0:
                    print("You have defeated", enemy.name + "!")
            else:
                enemy = enemy_list.pop()
                print("\nA new enemy approaches!")

        if player.hp <= 0 and enemy.hp > 0:
            print("\nYou died!\n")
            print(enemy.name, "hit points:", enemy.hp)
            print(len(enemy_list), "enemies left.")
            pts = get_points()
            player.points += pts
            print(pts, "points gained.")
            spend_points(player)
            enemy_list = game_restart(player)
            enemy = enemy_list.pop()

        if player.hp and enemy.hp <= 0:
            print("\nDraw!\n")
            print(player.name, "hit points: 0")
            print(enemy.name, "hit points: 0")
            print(len(enemy_list), "enemies left.")
            enemy = enemy_list.pop()
            pts = get_points()
            player.points += pts
            print(pts, "points gained.")
            spend_points(player)
            enemy_list = game_restart(player)
            enemy = enemy_list.pop()

    elif choice == "2":
        print("Closing Critical Hits")
        sys.exit()

    else:
        os.system('clear')
        print("\nPlease choose from the list\n")
