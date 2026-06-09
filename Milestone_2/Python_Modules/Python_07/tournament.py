#!/usr/bin/env python3


from typing import Protocol, cast
import ex0
import ex1
import ex2


class HealableCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def heal(self) -> str: ...


class TransformCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def transform(self) -> str: ...
    def revert(self) -> str: ...


if __name__ == "__main__":
    normal = ex2.NormalStrategy()
    attack = ex2.AggresiveStrategy()
    defense = ex2.DefensiveStrategy()
    heal_factory = ex1.HealingCreatureFactory()
    transform_factory = ex1.TransformCreatureFactory()
    flame_factory = ex0.FlameFactory()

    fire_cre = flame_factory.create_base()
    heal_cre = cast(HealableCreature, heal_factory.create_evolved())
    transform_cre = cast(TransformCreature, transform_factory.create_base())

    try:
        defense.act(heal_cre)
        # print(normal.act(fire_cre))
        # print(normal.act(transform_cre))
    except Exception as error:
        print(error)