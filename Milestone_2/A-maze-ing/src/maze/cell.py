from enum import Enum


class DIR(Enum):
    N = 0b0001 # 1
    S = 0b0010 # 2
    E = 0b0100 # 4
    W = 0b1000 # 8


class Cell():
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos: tuple[int, int] = pos
        self._is_entry_exit: bool = False
        self._visited: bool = False
        self._walls: int = 15

    @property
    def walls(self) -> int:
        return self._walls
    
    @walls.setter
    def walls(self, value: int) -> None:
        if value < 0 or value > 15:
            raise ValueError("Wall value must be in range '0' and '15'")
        self._walls = value

    @property
    def north(self) -> bool:
        return bool(self._walls & 1)
    
    @property
    def south(self) -> bool:
        return bool((self._walls >> 1) & 1)
    
    @property
    def east(self) -> bool:
        return bool((self._walls >> 2) & 1)
    
    @property
    def west(self) -> bool:
        return bool((self._walls >> 3) & 1)

    def remove_wall(self, direction: DIR) -> None:
        if self._walls & direction.value:
            self._walls ^= direction.value

    def mark_visited(self) -> None:
        self._visited = True

    def is_entry_exit(self) -> None:
        self._is_entry_exit = True
