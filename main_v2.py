print(f'{'='*25} Version 2{'='*25}')
from classes_v2.characters import Fighter, Monster
from classes_v2.weapon import Sword, Bow, Teeth, Paw, MagicStaff

if __name__ == "__main__":
    fighter = Fighter("Fighter", weapons=[Sword(), Bow(), MagicStaff()], position=10)
    monster = Monster("Monster", weapons=[Teeth(), Paw()], position=30)

    step = 0
    while fighter.is_alive() and monster.is_alive():
        fighter.fight(monster)
        monster.fight(fighter)
        print(f"{'-'*50}\nRound {step}: {fighter.name} health: {fighter.health}, {monster.name} health: {monster.health}")
        step += 1

    if fighter.is_alive():
        print(f"{fighter.name} wins!")
    else:
        print(f"{monster.name} wins!")
