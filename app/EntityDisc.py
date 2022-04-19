from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from EntityTower import Tower

class Disc:
    def __init__(self, size: int, tower: Tower = None):
        if size > 8 or size < 1:
            raise AttributeError("Disc size may be between 1 and 8.")
        else:
            self._size = size
        self._tower = tower

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size < 1 or new_size > 8:
            raise AttributeError("Disc size may be between 1 and 8.")
        else:
            self._size = new_size

    @property
    def tower(self) -> Tower:
        return self._tower

    @tower.setter
    def tower(self, new_tower):
        self._tower = new_tower

    def __repr__(self) -> str:
        return f"Disc({self.size})"
