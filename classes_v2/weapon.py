# --- Weapon and Attack Classes ---
from abc import ABC, abstractmethod
from random import randint


class AttackType(ABC):
    @abstractmethod
    def calculate_attack(self):
        pass

class SwordAttack(AttackType):
    def calculate_attack(self):
        return randint(1, 10)

class BowAttack(AttackType):
    def calculate_attack(self):
        return randint(1, 6)

class MagicAttack(AttackType):
    def calculate_attack(self):
        return randint(5, 15)

class TeethAttack(AttackType):
    def calculate_attack(self):
        return randint(1, 5)

class PawAttack(AttackType):
    def calculate_attack(self):
        return randint(2, 6)


class Weapon(ABC):
    def __init__(self, min_distance=0, max_distance=0, attack_type=None, weapon_type=None):
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.attack_type = attack_type
        self.weapon_type = weapon_type

    def attack(self):
        if not self.attack_type:
            raise ValueError("Attack type must be defined")
        return self.attack_type.calculate_attack()

class Sword(Weapon):
    def __init__(self):
        super().__init__(min_distance=1, max_distance=3, attack_type=SwordAttack(), weapon_type="Sword")

class Bow(Weapon):
    def __init__(self):
        super().__init__(min_distance=4, max_distance=10, attack_type=BowAttack(), weapon_type="Bow")

class MagicStaff(Weapon):
    def __init__(self):
        super().__init__(min_distance=10, max_distance=20, attack_type=MagicAttack(), weapon_type="Magic Staff")

class Teeth(Weapon):
    def __init__(self):
        super().__init__(min_distance=0, max_distance=1, attack_type=TeethAttack(), weapon_type="Big Sharp Teeth")

class Paw(Weapon):
    def __init__(self):
        super().__init__(min_distance=0, max_distance=1, attack_type=PawAttack(), weapon_type="Paws")