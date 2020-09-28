from string import Template

class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.health = 10
        self.attack = 3
        self.strength = 3
        self.range_attack = 3
        self.special_attack = 4
        self.defense = 2
        self.monsters_killed = 0
        self.coins = 0,
        self.inventory = []

class Monster:
    def __init__(self, monster, health, attack, defense):
        self.monster = monster
        self.health = health
        self.attack = attack
        self.defense = defense

shop_items = ({'Name': 'Potion', 'Cost': '5'}, {'Name': 'Armor', 'Cost': '25'})

def fight_logic(enemy):
    print('You start to fight a', enemy.monster)
    print("What will you do?")
    print("1: Slash")
    print("2: Stab")
    print("3: Ranged Attack")
    print("4: Special Attack")
    ans = input("Select an option: ")

    if ans == "1":
        enemy.health -= user_hero.attack - enemy.defense
    elif ans == "2":
        enemy.health -= user_hero.strength - enemy.defense
    elif ans == "3":
        enemy.health -= user_hero.range_attack - enemy.defense
    elif ans == "4":
        enemy.health -= user_hero.special_attack - enemy.defense

    if enemy.health <= 0:
        print("Enemy Defeated! You gained 3 experience.")
        user_hero.experience += 3
        user_hero.health = 10
        game_play()
    else:
        print(enemy.monster,'has', enemy.health,'health remaining. They attack you.')
        user_hero.health -= enemy.attack - user_hero.defense
        print('You have', user_hero.health, 'health remaining')
        fight_logic(enemy)

def monster_fight():
    print("Hit")
    if user_hero.level == 1:
        new_enemy = Monster('Goblin', 4, 3, 1)
    elif user_hero.level == 2:
        new_enemy = Monster('Gargoyle', 6, 4, 2)
    elif user_hero.level == 3:
        new_enemy = Monster('Orc', 8, 5, 3)
    elif user_hero.level == 4:
        new_enemy = Monster('Mountain Troll', 10, 6, 4)

    fight_logic(new_enemy)

def enter_shop():
    item_num = 1
    print('Welcome to the Shop! What would you like to buy?')
    for x in shop_items:
        item_print = Template('$item_num: $item_name for $item_cost gold')
        print(item_print.substitute(item_num=item_num, item_name=x["Name"], item_cost=x["Cost"]))
        item_num += 1
    exit_prompt = Template('$item_num: Leave Shop')
    print(exit_prompt.substitute(item_num=item_num))
    ans = input('Select an option ')


def begin_travel():
    print("Travel in progress")

def game_play():
    print("What would you like to do?")
    print("1: Fight")
    print("2: Shop")
    print("3: Travel")
    print("4: View Stats")
    ans = input("Select a number: ")

    if ans == "1":
        monster_fight()
    elif ans == "2":
        enter_shop()
    elif ans == "3":
        begin_travel()
    elif ans == "4":
        print("Here are your stats:")
        print("Level:", user_hero.level)
        print("Experience:", user_hero.experience)
        print("Health:", user_hero.health)
        print("Attack:", user_hero.attack)
        print("Defense:", user_hero.defense)
        

print("Welcome Adventurer! Let's begin your journey.")
name = input("First, tell me your name: ")
if name:
    print("It's nice to meet you", name)
    user_hero = Hero(name)
    print("Here are your beginning stats:")
    print("Level:", user_hero.level)
    print("Experience:", user_hero.experience)
    print("Health:", user_hero.health)
    print("Attack:", user_hero.attack)
    print("Defense:", user_hero.defense)
    ans = input("Are you ready to play (yes/no)? ").lower()
    if ans == "yes":
        game_play()