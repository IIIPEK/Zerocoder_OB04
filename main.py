from unittest.mock import MagicMixin
from xml.sax.handler import version

from classes.weapon import Sword, Bow, Teeth, Paw, MagicStaff
from classes.characters import Fighter, Monster

figter = Fighter("Figter", weapons=[Sword(), Bow(), MagicStaff()],position=10)
monster = Monster("Monster", weapons=[Teeth(), Paw()],position=30, speed=4)

step = 0
while figter.is_alive() and monster.is_alive():
    figter.fight(monster)
    monster.fight(figter)
    print(f"{'-'*50}\nRound {step}: {figter.name} health: {figter.health}, {monster.name} health: {monster.health}")
    step += 1

if figter.is_alive():
    print(f"{figter.name} wins!")
else:
    print(f"{monster.name} wins!")



