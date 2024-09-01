class Thing:

    def __init__(self, name, defence, attack, health_points):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.health_points = health_points


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


