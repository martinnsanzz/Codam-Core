#!/usr/bin/env python3


from typing import Callable


class Grimoire:
    @staticmethod
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    @staticmethod
    def fireball(target: str, power: int) -> str:
        return f"Fireball deals {power} fire damage to {target}"

    @staticmethod
    def freeze(target: str, power: int) -> str:
        return f"Freeze immobilizes {target} with {power} ice power"

    @staticmethod
    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} for {power} damage"

    @staticmethod
    def shield(target: str, power: int) -> str:
        return f"Shield grants {target} {power} defense"

    @staticmethod
    def dark_curse(target: str, power: int) -> str:
        return f"Dark Curse weakens {target} by {power} points"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) -> \
        Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], str],
                       spell: Callable[[str, int], str]) -> \
        Callable[[str, int], str | Callable[[str, int], str]]:
    def condition_cast(target: str, power: int) -> \
            str | Callable[[str, int], str]:
        if callable(condition):
            return spell(target, power)
        return "Spell fizzled"
    return condition_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    ...


if __name__ == "__main__":
    test_values = [7, 5, 20]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined = spell_combiner(Grimoire.dark_curse,
                              Grimoire.heal)
    amplifier = power_amplifier(Grimoire.fireball, 5)

    cast = conditional_caster(test_values, Grimoire.shield)

    print(combined(test_targets[2], test_values[1]))
    print(amplifier(test_targets[0], test_values[2]))
    print(cast(test_targets[1], test_values[0]))