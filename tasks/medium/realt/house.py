class House:

    address: str
    area: int
    cost: int

    def __init__(self, address, cost, area):

        self.address = address
        self.area = area
        self.cost = cost

    def increase(self, value: int):

        self.cost += value

    def decrease(self, value: int):

        self.cost -= value

    def __repr__(self):
        return f'Дом: {self.address}'
