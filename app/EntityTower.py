from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from EntityDisc import Disc

class Tower:
    def __init__(self, discs: List[Disc] = []):
        self.discs = discs

    @property
    def discs(self) -> List[Disc]:
        return self.discs

    def add_disc(self, disc: Disc):
        self.discs.append(disc)
        disc.tower = self

    def remove_disc(self):
        removed_disc = self.discs.pop()
        removed_disc.tower = None
