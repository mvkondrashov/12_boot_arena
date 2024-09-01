import random

THING_NAME = [
    'axe', 'ring', 'armor', 'helmet', 'boots', 'gloves', 'sword', 'bow'
]


class Thing:

    def __init__(self, name, defence, attack, health_points):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.health_points = health_points


def create_thing():
    name = random.choice(THING_NAME)
    defence = random.randrange(1, 10)
    attack = random.randrange(0, 30)
    health_points = random.randrange(0, 30)

    return Thing(
        name=name, defence=defence, attack=attack, health_points=health_points
    )
