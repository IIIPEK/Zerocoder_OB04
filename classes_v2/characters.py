from abc import ABC, abstractmethod
from random import randint

# --- Strategy for Weapon Selection ---
class WeaponSelectionStrategy(ABC):
    @abstractmethod
    def select(self, character):
        pass

class RandomWeaponSelection(WeaponSelectionStrategy):
    def select(self, character):
        if character.weapons:
            character.weapon = randint(0, len(character.weapons) - 1)
            print(f"{character.name} selects {character.weapons[character.weapon].weapon_type}")

# --- Strategy for Fight Behavior ---
class FightStrategy(ABC):
    @abstractmethod
    def execute(self, character, enemy):
        pass

class DefaultFightStrategy(FightStrategy):
    def execute(self, character, enemy):
        if enemy:
            distance = character.get_distance(enemy)
            weapon = character.weapons[character.weapon]
            if weapon.min_distance <= distance <= weapon.max_distance:
                damage = weapon.attack()
                enemy.take_damage(damage, character)
            elif distance < weapon.min_distance:
                print(f"{character.name} is too close from {enemy.name} to attack by {weapon.weapon_type}, distance is {distance}.")
            else:
                print(f"{character.name} is too far from {enemy.name} to attack. Distance: {distance}.")
            character.move()
            character.weapon_selection_strategy.select(character)

# --- Base Character Class ---
class Character(ABC):
    def __init__(self, name, health=100, weapons=None, position=0, speed=1,
                 weapon_selection_strategy=RandomWeaponSelection(),
                 fight_strategy=DefaultFightStrategy()):
        self.name = name
        self.health = health
        self.weapons = weapons or []
        self.weapon = 0 if self.weapons else None
        self.position = position
        self.speed = speed
        self.weapon_selection_strategy = weapon_selection_strategy
        self.fight_strategy = fight_strategy

    def move(self):
        self.position += randint(-self.speed, self.speed)
        print(f"{self.name} moves to {self.position}")
        return self.position

    def fight(self, enemy):
        self.fight_strategy.execute(self, enemy)

    def take_damage(self, damage, enemy):
        print(f"{self.name} takes {damage} damage from {enemy.name}")
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def get_distance(self, enemy):
        return abs(self.position - enemy.position)

# --- Fighter and Monster Classes ---
class Fighter(Character):
    def __init__(self, name, health=100, weapons=None, position=0, speed=2):
        super().__init__(name, health, weapons, position, speed)
        self.weapon_selection_strategy.select(self)

class Monster(Character):
    def __init__(self, name, health=100, weapons=None, position=0, speed=3):
        super().__init__(name, health, weapons, position, speed)
        self.weapon_selection_strategy.select(self)

