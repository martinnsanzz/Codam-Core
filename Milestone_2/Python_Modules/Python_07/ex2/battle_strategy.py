from abc import ABC, abstractmethod
from ex0.creature import Creature
import ex1


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class CustomError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CustomError(f"Invalid Creature {creature.name} \
for this normal strategy")
        print(creature.attack())


class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature) and \
               isinstance(creature, ex1.TransformCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CustomError(f"Invalid Creature {creature.name} \
for this aggresive strategy")
        print(creature.transform())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature) and \
               isinstance(creature, ex1.HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CustomError(f"Invalid Creature {creature.name} \
for this defensive strategy")
        print(creature.heal())
