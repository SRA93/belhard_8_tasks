class Tomato:

    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):

        self.index = index
        self.ripeness = self.states[0]

    def grow(self):

        try:
            self.ripeness = self.states[self.states.index(self.ripeness) + 1]

        except IndexError:

            print('Томат всё ;(')

    def is_ripe(self):

        if self.ripeness == self.states[-1]:
            return True

        else:
            return False
