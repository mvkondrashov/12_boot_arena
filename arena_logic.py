import random

from arena_person import create_person, dress_person, PEOPLE


def reduction_of_lives(defending_person, attacking_person):
    all_item_defence, all_item_attack = 0, 0
    for item in defending_person.inventory:
        all_item_defence += item.defence
    for item in attacking_person.inventory:
        all_item_attack += item.attack

    attack_damage = (attacking_person.base_attack + all_item_attack) * (
            (defending_person.base_defence + all_item_defence) / 100)

    defending_person.health_points -= attack_damage

    return int(attack_damage)


def main():
    for index in range(10):
        person = create_person()
        PEOPLE.append(person)
        dress_person(person)
    count = 0
    while True:
        count += 1
        defending_person = random.choice(PEOPLE)
        attacking_person = random.choice(
            [item for item in PEOPLE if item != defending_person]
        )
        damage = reduction_of_lives(defending_person, attacking_person)
        print(
            f'\033[34mРаунд {count}\033[0m. {attacking_person.name}'
            f' наносит удар по {defending_person.name} на {damage} ур')
        if defending_person.health_points <= 0:
            PEOPLE.remove(defending_person)
            print(f"{'_' * 10} ~~~ {'_' * 10}")
            if len(PEOPLE) == 1:
                print(f'\033[31m{PEOPLE[0].name}\033[0m'
                      f' одержал победу в турнире!')
                break
            print(f'{attacking_person.name} одержал победу!')
            print(f"{'_' * 10} ~~~ {'_' * 10}")


if __name__ == '__main__':
    main()
