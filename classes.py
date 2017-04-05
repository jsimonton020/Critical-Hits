import random
import os
import sys
import json


class Character:

    def __init__(self, name, hp, dice, points=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.dice = dice
        self.points = points

    def roll(self):
        damage = 0
        count = 0
        for d in self.dice:
            roll, _count = d.dice_roll()
            print(roll)
            count += _count
            damage += sum(roll)
        return damage, count

    def upgrade_dice(self, d_choice):
        self.dice[d_choice].upgrade()


class Dice:

    RANKS = {1: 4, 2: 6, 3: 8, 4: 10, 5: 12, 6: 20}

    def __init__(self, rank):
        self.rank = rank
        self.sides = Dice.RANKS[rank]

    def dice_roll(self, count=1):
        dice_numbers = []
        dice = random.randint(1, self.sides)
        dice_numbers.append(dice)
        while dice == self.sides:
            dice = random.randint(1, self.sides)
            dice_numbers.append(dice)
            count += 1
        return dice_numbers, count

    def upgrade(self):
        self.rank += 1
        self.sides = Dice.RANKS[self.rank]

    def __repr__(self):
        return 'd{}'.format(self.sides)


def character_roll(player, enemy):
    p_roll, count = player.roll()
    print(player.name, "hit for", p_roll)
    if count >= 5:
        print("OMG OMG OMG OMG OMG!!!")
    elif count == 4:
        print("M-M-M-M-M-MONSTER HIT!")
    elif count == 3:
        print("MEGA HIT!")
    elif count == 2:
        print("CRITICAL HIT!")
    enemy.hp -= p_roll

    e_roll, count = enemy.roll()
    print(enemy.name, "hit for", e_roll)
    if count >= 5:
        print("OMG OMG OMG OMG OMG!!!")
    elif count == 4:
        print("M-M-M-M-M-MONSTER HIT!")
    elif count == 3:
        print("MEGA HIT!")
    elif count == 2:
        print("CRITICAL HIT!")
    player.hp -= e_roll


def down(player, enemy, enemy_list):
        print("You have defeated", enemy.name + "!")
        print(player.name, "hit points:", player.hp)
        pause()
        count = check_enemy(enemy_list)
        if count == 0 and enemy.name == "Shia LaBeouf":
            fanfare()
            sys.exit()

        elif count == 0:
            enemy = shia_surprise()
            return enemy

        elif count > 0:
            os.system('clear')
            print("A new enemy approaches")
            enemy = enemy_list.pop()
            return enemy


def died(player, enemy, enemy_list):
        print("\nYou died!\n")
        print(enemy.name, "hit points:", enemy.hp)
        print(len(enemy_list) + 1, "enemies left.")
        pts = get_points(enemy_list)
        player.points += pts
        print(pts, "point(s) gained.")
        pause()
        spend_points(player)
        enemy_list = game_restart(player)
        return enemy_list


def draw(player, enemy, enemy_list):
        print("\nDraw!\n")
        print(player.name, "hit points: 0")
        print(enemy.name, "hit points: 0")
        print(len(enemy_list), "enemies left.")
        pts = get_points(enemy_list)
        player.points += pts + 1
        print(pts + 1, "point(s) gained.")
        pause()
        spend_points(player)
        enemy_list = game_restart(player)
        return enemy_list


def d_bag(rank, amount):
    bag = []
    for i in range(0, amount):
        d = Dice(rank)
        bag.append(d)
    return bag


def set_player():
    os.system('clear')
    choice = input("What is your name?: ")
    play_dice = d_bag(1, 4)
    player = Character(choice, 50, play_dice, 50)
    return player


def set_enemies():
    slime_dice = d_bag(1, 1)
    slime = Character("Slime", 15, slime_dice)

    bat_dice = d_bag(1, 1)
    bat = Character("Bat", 30, bat_dice)

    gob_dice = d_bag(2, 1)
    goblin = Character("Goblin", 45, gob_dice)

    hob_dice = d_bag(2, 1)
    hobgob = Character("Hobgoblin", 60, hob_dice)

    orc_dice = d_bag(3, 1)
    orc = Character("Orc", 75, orc_dice)

    troll_dice = d_bag(3, 1)
    troll = Character("Cave Troll", 90, troll_dice)

    owl_dice = d_bag(4, 1)
    owlbear = Character("Owlbear", 105, owl_dice)

    chim_dice = d_bag(4, 1)
    chimera = Character("Chimera", 120, chim_dice)

    giant_dice = d_bag(5, 1)
    giant = Character("Giant", 135, giant_dice)

    drag_dice = d_bag(6, 1)
    dragon = Character("Dragon", 150, drag_dice)

    enemy_list = [dragon, giant, chimera, owlbear,
                  troll, orc, hobgob, goblin, bat, slime]
    return enemy_list


def spend_points(player):
    while player.points > 0:
        os.system('clear')
        points = check_points(player)
        print("Player points:", points)
        print("1. More HP: 1 point")
        print("2. Upgrade Die: 2 points")
        print("3. Add 1 D4: 3 points")
        print("4. All Finished")
        choice = input("What would you like to spend your points on?: ")
        try:
            if choice == "1" and points >= 1:
                print("Player max hp:", player.max_hp)
                player.max_hp += 20
                print("Player max hp upgraded to:", player.max_hp)
                player.points -= 1
                pause()
                spend_points(player)

            elif choice == "1" and points < 1:
                print("Not enough points")
                pause()
                spend_points(player)

            elif choice == "2" and points >= 2:
                for i, d in enumerate(player.dice, start=1):
                    print("{} : {}".format(i, d))
                d_choice = int(input("Die to upgrade?: "))
                d_choice -= 1
                player.upgrade_dice(d_choice)
                player.points -= 2
                for i, d in enumerate(player.dice, start=1):
                    print("Die upgraded")
                    print("{} : {}".format(i, d))
                    pause()
                spend_points(player)

            elif choice == "2" and points < 2:
                print("Not enough points")
                pause()
                spend_points(player)

            elif choice == "3" and points >= 3:
                p_dice = d_bag(1, 1)
                player.dice += p_dice
                player.points -= 3
                print("Added 1 d4 to your dice bag")
                pause()
                spend_points(player)

            elif choice == "3" and points < 3:
                print("Not enough points")
                pause()
                spend_points(player)

            elif choice == "4":
                break

            else:
                print("Please select from the list")
                pause()
                spend_points(player)
        except (ValueError, IndexError):
            print("Invalid Selection")
            continue


def shia_surprise():
    os.system('clear')
    print("You have defeated all the enemies!")
    pause()
    print("You start to celebrate the hard fought victory... ")
    pause()
    print("You look over your shoulder and see him...")
    pause()
    print("He gets down on all fours and bursts into a sprint...")
    pause()
    os.system('clear')
    print("IT'S SHIA LEBOUF!!!!!")
    shia_dice = d_bag(6, 3)
    enemy = Character("Shia LaBeouf", 200, shia_dice)
    return enemy


def game_restart(player):
    player.hp = player.max_hp
    enemy_list = set_enemies()
    return enemy_list


def get_points(enemy_list):
    count = len(enemy_list)
    points = range(9, -1, -1)
    return points[count]


def check_points(player):
    points = player.points
    return points


def check_enemy(enemy_list):
    count = len(enemy_list)
    return count


def pause():
    input("Press ENTER to continue...")


def fanfare():
    print("Winner")


def save_game(player, enemy, enemy_list):
    path = '/home/jon/critical_hits/save_game.txt'
    os.system('clear')
    print("1: Yes")
    print("2: No")
    choice = input("Would you like to save the game?: ")
    if choice == "1":
        print("do stuff")
        data = player, enemy, enemy_list
        # how do I save json to save_game.txt
        json.dumps(data)
        sys.exit()
    elif choice == "2":
        sys.exit()
    else:
        save_game()


# def load_game():
    # load game state from JSON file


def initialize():
    os.system('clear')
    print("Welcome to Critical Hits!")
    print("1: New Game")
    print("2: Load Game")
    choice = input(": ")
    if choice == "1":
        player = set_player()
        enemy_list = set_enemies()
        return player, enemy_list
    elif choice == "2":
        load_game()
