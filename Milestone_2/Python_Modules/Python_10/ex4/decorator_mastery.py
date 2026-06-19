#!/usr/bin/env python3


from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    ...


def power_validator(min_power: int) -> Callable:
    ...


def retry_spell(max_attempts: int) -> Callable:
    ...


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...

    def cast_spell(self, spell_name: str, power: int) -> str:
        ...


if __name__ == "__main__":
    ...