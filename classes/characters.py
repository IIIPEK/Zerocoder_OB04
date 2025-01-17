from abc import ABC, abstractmethod
from random import randint
from .weapon import Weapon

class Character(ABC):
    def __init__(self, name, health=100, weapons =None, position=0, speed=1):
        self.name = name
        self.weapons = weapons
        self.health = health
        self.weapon = None
        self.position = position
        self.speed = speed



    @abstractmethod
    def move(self):
        self.position += randint(-self.speed, self.speed)
        print(f"{self.name} moves to {self.position}")
        return self.position

    @abstractmethod
    def select_weapon(self,number):
        if number < len(self.weapons):
            self.weapon = number
            print(f"{self.name} selects {self.weapons[self.weapon].weapon_type} weapon")
            return self.weapons[self.weapon]
        else:
            print(f"{self.name} doesn't have {number} weapon")
            return None

    @abstractmethod
    def fight(self,enemy):
        if enemy:
            return self.weapons[self.weapon].attack()
        return 0


    @abstractmethod
    def take_damage(self, damage, enemy):
        print(f"{self.name} takes {damage} damage from {enemy.name}")
        self.health -= damage
        return self.health

    @abstractmethod
    def is_alive(self):
        return self.health > 0

    @abstractmethod
    def get_distance(self, enemy = None):
        if enemy:
            return abs(self.position - enemy.position)
        return None

class Fighter(Character):
    def __init__(self, name, health=100, weapons=None, position=0, speed=2):
        super().__init__(name, health, weapons, position, speed)
        if len(self.weapons) > 0:
            self.weapon = randint(0, len(self.weapons) - 1)

    def move(self):
        return super().move()

    def select_weapon(self,number):
        return super().select_weapon(number)

    def fight(self, enemy):
        if enemy:
            if self.weapons[self.weapon].max_distance >= self.get_distance(enemy) >= \
                    self.weapons[self.weapon].min_distance:
                return enemy.take_damage(super().fight(enemy),self)
            else:
                print(f"{self.name} is too far from {enemy.name} to attack by {self.weapons[self.weapon].weapon_type}, distance is {self.get_distance(enemy)}..")
                self.move()
                self.select_weapon(randint(0, len(self.weapons) - 1))
                return 0
        print(f"{self.name} attacks his own shadow.")
        return 0

    def take_damage(self, damage,enemy):
        if randint(1, 5) % 2 == 0:
            return super().take_damage(damage,enemy)
        print(f"*** {self.name} dodges the attack.***")
        return self.health

    def is_alive(self):
        return self.health > 0

    def get_distance(self, enemy = None):
        if enemy:
            return abs(self.position - enemy.position)
        return None

class Monster(Character):
    def __init__(self, name, health=100, weapons=None, position=0, speed=1):
        super().__init__(name, health, weapons, position, speed)
        if len(self.weapons) > 0:
            self.weapon = randint(0, len(self.weapons) - 1)

    def move(self):
        return super().move()

    def select_weapon(self,number):
        return super().select_weapon(number)

    def fight(self, enemy):
        if enemy:
            if self.get_distance(enemy) <= self.weapons[self.weapon].max_distance and self.get_distance(enemy) >= self.weapons[self.weapon].min_distance:
                return enemy.take_damage(super().fight(enemy), self)
            else:
                print(f"{self.name} is too far from {enemy.name} to attack, distance is {self.get_distance(enemy)}.")
                self.select_weapon(randint(0, len(self.weapons) - 1))
                self.move()
                return 0
        print(f"{self.name} growls and snaps teeth.")
        return 0

    def take_damage(self, damage, enemy):
        if randint(1, 5) % 2 == 1:
            return super().take_damage(damage, enemy)
        print(f"### {self.name} dodges the attack.###")
        return self.health

    def is_alive(self):
        return self.health > 0

    def get_distance(self, enemy = None):
        if enemy:
            return abs(self.position - enemy.position)
        return None


