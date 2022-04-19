from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from EntityDisc import Disc

class Tower:
    def __init__(self, max_discs: int = None, discs: List[Disc] = None):
        if max_discs is None:
            self._max_discs = 8
        else:
            self._max_discs = max_discs

        if discs is None:
            self._discs = []
        else:
            if len(discs) <= self._max_discs:
                for disc in discs:
                    disc.tower = self
                self._discs = discs
            else:
                raise AttributeError(f"Discs exceed tower limit (this tower just support {self._max_discs} discs,"
                                     f"received {(len(discs))} discs).")

    @property
    def max_discs(self) -> int:
        return self._max_discs

    @max_discs.setter
    def max_discs(self, new_max_discs):
        self._max_discs = new_max_discs

    @property
    def discs(self) -> List[Disc]:
        return self._discs

    @discs.setter
    def discs(self, new_discs: List[Disc]):
        self._discs = new_discs

    def add_disc(self, disc: Disc):
        if len(self.discs) < self.max_discs:
            self.discs.append(disc)
            disc.tower = self
        else:
            raise AttributeError("Tower is full.")

    def remove_disc(self) -> Disc:
        removed_disc = None
        if self.discs:
            removed_disc = self.discs.pop()
            removed_disc.tower = None
        return removed_disc

    def transfer_disc(self, new_tower: Tower) -> bool:
        successful_transfer = False
        if not new_tower.discs:
            removed_disc = self.remove_disc()
            new_tower.add_disc(removed_disc)
            successful_transfer = True
        elif new_tower.discs[-1].size > self.discs[-1].size:
            removed_disc = self.remove_disc()
            new_tower.add_disc(removed_disc)
            successful_transfer = True
        return successful_transfer

    def __repr__(self) -> str:
        return f"Tower({self.discs})"
