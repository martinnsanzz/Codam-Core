#!/usr/bin/env python3


from functools import wraps
from typing import Callable, Any
from time import perf_counter


class C:
    H = '\033[95m'  # Header
    B = '\033[94m'  # Blue
    C = '\033[96m'  # Cyan
    G = '\033[92m'  # Green
    W = '\033[93m'  # Warning
    F = '\033[91m'  # Fail
    E = '\033[0m'  # End
    Bo = '\033[1m'  # Bold
    U = '\033[4m'

    def msg(self, color: str, msg: str) -> None:
        print(getattr(self, color) + msg + C.E)


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_function(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}")
        elapsed_time = perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = perf_counter() - elapsed_time
        print(f"Spell completed in {round(elapsed_time, 3)}")
        return result
    return wrapper_function

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


@spell_timer
def slow_spell(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    print(C.U, end="")
    C().msg("Bo", "Testing spell timer...")
    print(slow_spell(10000000))