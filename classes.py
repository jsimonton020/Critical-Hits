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

    def upgrade_dice(self, d_choice):
        self.dice[d_choice].upgrade()


class Dice:

    RANKS = {1: 4, 2: 6, 3: 8, 4: 10, 5: 12, 6: 20}

    def __init__(self, rank):
        self.rank = rank
        self.sides = Dice.RANKS[rank]

    def dice_roll(self):
        dice_numbers = []
        dice = random.randint(1, self.sides)
        dice_numbers.append(dice)
        while dice == self.sides:
            dice = random.randint(1, self.sides)
            dice_numbers.append(dice)
        return dice_numbers

    def upgrade(self):
        self.rank += 1
        self.sides = Dice.RANKS[self.rank]

    def __repr__(self):
        return 'd{}'.format(self.sides)


def d_bag(rank, amount):
    bag = []
    for i in range(0, amount):
        d = Dice(rank)
        bag.append(d)
    return bag


def set_player():
    choice = input("What is your name?: ")
    play_dice = d_bag(1, 1)
    player = Character(choice, 50, play_dice)
    return player


def set_enemies():
    slime_dice = d_bag(1, 1)
    slime = Character("Slime", 20, slime_dice)

    bat_dice = d_bag(1, 2)
    bat = Character("Bat", 35, bat_dice)

    gob_dice = d_bag(2, 1)
    goblin = Character("Goblin", 50, gob_dice)

    hob_dice = d_bag(2, 2)
    hobgob = Character("Hobgoblin", 65, hob_dice)

    orc_dice = d_bag(3, 1)
    orc = Character("Orc", 80, orc_dice)

    troll_dice = d_bag(3, 2)
    troll = Character("Cave Troll", 95, troll_dice)

    owl_dice = d_bag(4, 1)
    owlbear = Character("Owlbear", 110, owl_dice)

    chim_dice = d_bag(4, 2)
    chimera = Character("Chimera", 125, chim_dice)

    giant_dice = d_bag(5, 2)
    giant = Character("Giant", 140, giant_dice)

    drag_dice = d_bag(6, 2)
    dragon = Character("Dragon", 155, drag_dice)

    enemy_list = [dragon, giant, chimera, owlbear,
                  troll, orc, hobgob, goblin, bat, slime]
    return enemy_list


def spend_points(player):
    while True:
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
                spend_points(player)

            elif choice == "2" and points >= 2:
                for i, d in enumerate(player.dice, start=1):
                    print("{} : {}".format(i, d))
                d_choice = int(input("Die to upgrade?: "))
                d_choice -= 1
                player.upgrade_dice(d_choice)
                player.points -= 2
                spend_points(player)

            elif choice == "3" and points >= 3:
                p_dice = d_bag(1, 1)
                player.dice += p_dice
                player.points -= 3
                spend_points(player)

            elif choice == "4":
                game_restart(player)

            else:
                print("Please select from the list")
                spend_points(player)
        except (ValueError, IndexError):
            print("Invalid Selection")
            continue
        else:
            break


def shai_surprise():
    print("You start to celebrate the hard fought victory... ")
    print("You look over your shoulder and see him...")
    print("He gets down on all fours and bursts into a sprint...")
    print("IT'S SHIA LEBOUF!!!!!")
    shia_dice = d_bag(6, 4)
    shia = Character("Shia LaBeouf", 250, shia_dice)
    return shia


def game_restart(player):
    player.hp = player.max_hp
    return set_enemies()


def check_points(player):
    points = player.points
    return points
