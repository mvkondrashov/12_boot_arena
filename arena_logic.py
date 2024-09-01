import random

from arena_classes import Thing, Person, Paladin, Warrior
from arena_things import create_thing

NAMES = [
    "Oliver", "Charlotte", "Liam", "Amelia", "Noah", "Isla", "James", "Ava",
    "William", "Mia", "Elijah", "Sophia", "Lucas", "Grace", "Mason", "Ella",
    "Henry", "Harper", "Ethan", "Lily"
]
PEOPLE = []


def reduction_of_lives(defending_person, attacking_person):
    all_item_defence = 0
    for item in defending_person.inventory:
        all_item_defence += item.defence
    attack_damage = attacking_person.base_attack * (
                defending_person.base_defence + all_item_defence)
    defending_person.health_points -= attack_damage
    return attack_damage


def create_person():
    for person in range(10):
        random_name = random.choice(NAMES)
        random_hp = random.randint(100, 130)
        random_attack = random.randint(10, 30)
        random_defense = random.uniform(0, 10)
        selected_option = random.choice(
            [Paladin(random_name, random_hp, random_attack, random_defense),
             Warrior(random_name, random_hp, random_attack, random_defense)]
        )
        PEOPLE.append(selected_option)


def dress_person():
    for person in PEOPLE:
        count = random.randint(1, 4)
        for index in range(count):
            person.inventory.append(create_thing())


def do_battle():
    while True:
        defending_person = random.choice(PEOPLE)
        attacking_person = random.choice(
            [item for item in PEOPLE if item != defending_person]
        )

        print(f"{'_' * 10} ~~~ {'_' * 10}")
        print(f'Начала поединка между {attacking_person.name} и {defending_person.name}!')
        while True:
            damage = reduction_of_lives(defending_person, attacking_person)
            print(f'{attacking_person.name} наносит удар по {defending_person.name} на {damage} ур')
            if defending_person.health_points <= 0:
                PEOPLE.remove(defending_person)
                print(f'{attacking_person.name} одержал победу!')
                break




def main():
    create_person()
    dress_person()
    do_battle()


if __name__ == '__main__':
    main()
