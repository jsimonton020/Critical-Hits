import random


class Character:

    def __init__(self, name, hp, dice, points=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.dice = dice
        self.points = points

    def roll(self):
        damage = 0
        for d in self.dice:
            roll = d.dice_roll()
            print(roll)
            damage += sum(roll)
        return damage


class Dice:

    def __init__(self, sides):
        self.sides = sides

    def dice_roll(self):
        dice_numbers = []
        dice = random.randint(1, self.sides)
        dice_numbers.append(dice)
        while dice == self.sides:
            dice = random.randint(1, self.sides)
            dice_numbers.append(dice)
        return dice_numbers

    def __repr__(self):
        return 'd{}'.format(self.sides)


def d_bag(sides, amount):
    bag = []
    for i in range(0, amount):
        d = Dice(sides)
        bag.append(d)
    return bag


def set_player():
    play_dice = d_bag(6, 1)
    player = Character("Player", 50, play_dice, 0)
    return player


def set_enemies():
    slime_dice = d_bag(6, 1)
    slime = Character("Slime", 20, slime_dice)

    bat_dice = d_bag(6, 2)
    bat = Character("Bat", 35, bat_dice)

    gob_dice = d_bag(8, 1)
    goblin = Character("Goblin", 50, gob_dice)

    hob_dice = d_bag(8, 2)
    hobgob = Character("Hobgoblin", 65, hob_dice)

    orc_dice = d_bag(10, 1)
    orc = Character("Orc", 80, orc_dice)

    troll_dice = d_bag(10, 2)
    troll = Character("Cave Troll", 95, troll_dice)

    owl_dice = d_bag(12, 1)
    owlbear = Character("Owlbear", 110, owl_dice)

    chim_dice = d_bag(12, 2)
    chimera = Character("Chimera", 125, chim_dice)

    giant_dice = d_bag(20, 1)
    giant = Character("Giant", 140, giant_dice)

    drag_dice = d_bag(20, 2)
    dragon = Character("Dragon", 155, drag_dice)

    enemy_list = [dragon, giant, chimera, owlbear,
                  troll, orc, hobgob, goblin, bat, slime]
    return enemy_list


def spend_points(player):
    points = player.points
    print("Player points:", points)
    print("1. More HP")
    print("2. Upgrade Die")
    print("3. Add 1 D6")
    choice = input("What would you like to spend your points on?: ")

    if choice == "1":
        print("Player max hp:", player.max_hp)
        player.max_hp += 20
        print("Player max hp upgraded to:", player.max_hp)
        player.points -= 1

    elif choice == "2":
        for i, d in enumerate(player.dice, start=1):
            print("{} : {}".format(i, d))
        d_choice = input("Die to upgrade?")
        d_choice -= 1
#        code goes here to upgrade die
        player.points -= 1

    elif choice == "3":
        p_dice = d_bag(6, 1)
        player.dice += p_dice
        player.points -= 1

    else:
        print("Please select from the list")


def game_restart(player):
    player.hp = player.max_hp
    return set_enemies()
