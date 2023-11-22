from abc import ABC, abstractmethod
from enum import Enum, unique
from dataclasses import dataclass
from random import choice, randint
from icecream import ic


@unique
class DamageType(Enum):
    PHYSICAL = '🗡️'
    FIRE = '🔥'
    ICE = '🧊'
    LIGHTNING = '⚡'
    POISON = '💀'
    HEALING = '❤️'

@unique
class DamageRange(Enum):
    MELEE = 0
    RANGE = 1

@dataclass
class Skill:
    name: str
    type: DamageType
    range: DamageRange
    damage: int = 0



class Character(ABC):
    classname = None

    @abstractmethod
    def __init__(self, name=None):
        self.name = name
        self._health = 100
        self._mana = 100
        self._resist = None
        self._skills = ()
        self._attack_var_percent = 20

    @property # getter
    def health(self):
        return self._health

    @health.setter # setter
    def health(self, value):
        if value > 100:
            self._health = 100
        else:
            self._health = value if value > 0 else 0

    @property # getter
    def mana(self):
        return self._mana

    @mana.setter # setter
    def mana(self, value):
        if value > 100:
            self._mana = 100
        else:
            self._mana = value if value > 0 else 0


    def __str__(self):
        return f'{self.classname} {self.name} 🔴{self._health} 🔵{self._mana}'

    def __repr__(self):
        return str(self)

    def attack(self):
        picked_skill = Skill(**choice(self._skills).__dict__)
        damage_change = picked_skill.damage * randint(-self._attack_var_percent, self._attack_var_percent) / 100
        ic(damage_change)
        picked_skill.damage += int(damage_change)
        return picked_skill


class Rus(Character):
    classname = 'Рус'
    
    def __init__(self, name):
        super().__init__(name)
        self._skills = (
            Skill('Славянский прострел сундука', DamageType.PHYSICAL, DamageRange.RANGE, 15),
            Skill('Древнерусский удар с вертушки', DamageType.PHYSICAL, DamageRange.MELEE, 20),
            Skill('Бахнул воды байкальской и погнал!', DamageType.HEALING, DamageRange.MELEE, 10),
        )

    def attack(self):
        picked_skill = super().attack()
        if picked_skill.type == DamageType.HEALING:
            self.health += picked_skill.damage
            picked_skill.damage = 0
        return picked_skill


class Lizard(Character):
    classname = 'Ящер'
    def __init__(self, name):
        super().__init__(name)
        self._skills = (
            Skill("Ящерский удар хвостом", DamageType.PHYSICAL, DamageRange.MELEE, 10),
            Skill("Взрыв Гипербореи", DamageType.FIRE, DamageRange.RANGE, 20),
            Skill("Отравленная чешуя", DamageType.POISON, DamageRange.MELEE, 15),
        )
        self._resist = DamageType.POISON


radislav = Rus('Радислав Багиров')
lizard = Lizard('Проклятущий')
