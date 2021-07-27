from house import House


class TownHouse(House):
    def __init__(self, adress, cost):
        super().__init__(adress, cost, 60)

    def __repr__(self):
        return f'Таунхаус: {self.address}'
