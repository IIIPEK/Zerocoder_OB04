from abc import ABC, abstractmethod
from random import randint

class AttackType(ABC):
    @abstractmethod
    def calculate_attack(self):
        pass

class SwordAttack(AttackType):
    def calculate_attack(self):
        self.last_attack = randint(1, 10)
        return self.last_attack

class BowAttack(AttackType):
    def calculate_attack(self):
        self.last_attack = randint(1, 6)
        return self.last_attack

class MagicAttack(AttackType):
    def calculate_attack(self):
        self.last_attack = randint(5, 15)
        return self.last_attack

class TeethAttack(AttackType):
    def calculate_attack(self):
        self.last_attack = randint(1,3)
        return self.last_attack

class PawAttack(AttackType):
    def calculate_attack(self):
        self.last_attack = randint(2,4)
        return self.last_attack


class Weapon(ABC):
    def __init__(self, min_distance=0, max_distance=0,attack_type:AttackType=None, weapon_type=None):
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.attack_type = attack_type
        self.weapon_type = weapon_type
        self.last_attack_power = 0

    @abstractmethod
    def attack(self):
        if not self.attack_type:
            raise ValueError("attack_type must be defined")
        self.last_attack_power = self.attack_type.calculate_attack()
        return self.last_attack_power


class Sword(Weapon):
    def __init__(self, min_distance=1, max_distance=3, attack_type=SwordAttack(), weapon_type="Sword"):
        super().__init__(min_distance, max_distance, attack_type, weapon_type)

    def attack(self):
        print(f'{self.weapon_type} attack: {super().attack()}')
        return self.last_attack_power

class Bow(Weapon):
    def __init__(self, min_distance=4, max_distance=10, attack_type=BowAttack(), weapon_type="Bow"):
        super().__init__(min_distance, max_distance, attack_type, weapon_type)


    def attack(self):
        print(f'{self.weapon_type} attack: {super().attack()}')
        return self.last_attack_power

class MagicStaff(Weapon):
    def __init__(self, min_distance=10, max_distance=20, attack_type=MagicAttack(), weapon_type="Magic Staff"):
        super().__init__(min_distance, max_distance, attack_type, weapon_type)

    def attack(self):
        print(f'{self.weapon_type} attack: {super().attack()}')
        return self.last_attack_power


class Teeth(Weapon):
    def __init__(self, min_distance=0, max_distance=1, attack_type=TeethAttack(), weapon_type=""):
        super().__init__(min_distance, max_distance, attack_type, weapon_type)

    def attack(self):
        print(f'{self.weapon_type} attack: {super().attack()}')
        return self.last_attack_power

class Paw(Weapon):
    def __init__(self, min_distance=1, max_distance=2, attack_type=TeethAttack(), weapon_type=""):
        super().__init__(min_distance, max_distance, attack_type, weapon_type)

    def attack(self):
        print(f'{self.weapon_type} attack: {super().attack()}')
        return self.last_attack_power