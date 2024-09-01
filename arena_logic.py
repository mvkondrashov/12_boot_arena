import random

from arena_classes import Thing, Person, Paladin, Warrior

NAMES = [
    "Oliver", "Charlotte", "Liam", "Amelia", "Noah", "Isla", "James", "Ava",
    "William", "Mia", "Elijah", "Sophia", "Lucas", "Grace", "Mason", "Ella",
    "Henry", "Harper", "Ethan", "Lily"
]
PEOPLE = []


def create_things():
    pass


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
            person.inventory.append(create_things())


def do_battle():
    print('Я за мир. Боёв не будет.')


def main():
    create_person()
    dress_person()
    do_battle()


if __name__ == '__main__':
    main()
