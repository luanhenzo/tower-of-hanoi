from EntityTower import Tower

class Disc:
    def __init__(self, size: int, tower: Tower = None):
        if size < 1:
            raise AttributeError
        else:
            self.size = size
        self.tower = tower

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, new_size):
        self.size = new_size

    @property
    def tower(self):
        return self.tower

    @tower.setter
    def tower(self, new_tower):
        self.tower = new_tower
