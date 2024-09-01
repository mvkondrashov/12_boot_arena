import random

from arena_things import create_thing

NAMES = [
    "Oliver", "Charlotte", "Liam", "Amelia", "Noah", "Isla", "James", "Ava",
    "William", "Mia", "Elijah", "Sophia", "Lucas", "Grace", "Mason", "Ella",
    "Henry", "Harper", "Ethan", "Lily"
]
PEOPLE = []


class Person:

    def __init__(self, name, health_points, base_attack, base_defence):
        self.name = name
        self.health_points = health_points
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.inventory = []


class Paladin(Person):

    def __init__(self, name, health_points, base_attack, base_defence):
        super().__init__(name, health_points, base_attack, base_defence)
        self.health_points = 2 * health_points


class Warrior(Person):

    def __init__(self, name, health_points, base_attack, base_defence):
        super().__init__(name, health_points, base_attack, base_defence)
        self.base_attack = 2 * base_attack


def create_person():
    random_name = random.choice(NAMES)
    random_hp = random.randint(100, 130)
    random_attack = random.randint(50, 100)
    random_defense = random.randint(0, 10)
    selected_option = random.choice(
        [Paladin(random_name, random_hp, random_attack, random_defense),
         Warrior(random_name, random_hp, random_attack, random_defense)]
    )
    return selected_option


def dress_person(person):
    count = random.randint(1, 4)
    for index in range(count):
        person.inventory.append(create_thing())
