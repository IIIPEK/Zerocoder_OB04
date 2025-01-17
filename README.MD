# Battle Simulation Game

This project is a simple battle simulation game that demonstrates the principles of Object-Oriented Programming (OOP) and adherence to the SOLID principles, particularly the Open/Closed Principle (OCP). The game simulates a fight between characters using different types of weapons.

## Project Structure

The project is organized into separate files and directories for better modularity and maintainability:

```
.
├── main_v2.py                # Main simulation logic
├── classes_v2
│   ├── weapon.py            # Weapon and attack classes
│   ├── characters.py        # Character and strategy classes
└── README.md                # Project documentation
```

## Features

- **Characters:**
  - `Fighter`: A skilled combatant with a variety of weapons.
  - `Monster`: A fierce opponent with powerful melee attacks.

- **Weapons:**
  - `Sword`: A melee weapon with a short attack range.
  - `Bow`: A ranged weapon with medium attack range.
  - `MagicStaff`: A long-range weapon with high attack power.
  - `Teeth`: A close-combat weapon used by monsters.
  - `Paw`: A heavy melee attack used by monsters.

- **Strategies:**
  - `WeaponSelectionStrategy`: Abstract base class for selecting weapons. Includes a random weapon selection implementation.
  - `FightStrategy`: Abstract base class for defining fight behavior. Includes a default implementation.

## How to Run

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your system.
3. Navigate to the project directory.
4. Run the simulation:
   ```bash
   python main_v2.py
   ```

## How It Works

1. The `main_v2.py` script initializes two characters: a `Fighter` and a `Monster`, each with a set of weapons.
2. Each character uses predefined strategies for:
   - Selecting a weapon.
   - Attacking the opponent based on their weapon's range and power.
3. The game loops through rounds where each character takes turns attacking, moving, and reacting until one character is defeated.

## Example Output

```
--------------------------------------------------
Round 0: Fighter health: 100, Monster health: 100
Fighter selects Sword
Fighter attacks Monster
Monster takes 8 damage from Fighter
Monster selects Teeth
Monster attacks Fighter
Fighter takes 4 damage from Monster
--------------------------------------------------
Round 1: Fighter health: 96, Monster health: 92
...
Fighter wins!
```

## Extending the Game

### Adding New Weapons
To add a new weapon, extend the `Weapon` class from `classes_v2.weapon.py` and define its attributes and behavior:
```python
class NewWeapon(Weapon):
    def __init__(self):
        super().__init__(min_distance=2, max_distance=5, attack_type=NewAttackType(), weapon_type="New Weapon")

    def attack(self):
        return super().attack()
```

### Adding New Characters
To add a new character type, extend the `Character` class from `classes_v2.characters.py` and define its specific behavior.

### Adding New Strategies
To add a new strategy, create a class that implements either the `WeaponSelectionStrategy` or `FightStrategy` abstract base class and implement the desired behavior.

## Dependencies

This project does not require any external libraries beyond Python's standard library.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

