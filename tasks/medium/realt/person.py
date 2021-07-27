class Person:

    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        self.money = 0
        self.realty = list()

    def info(self):

        print(f'Имя: {self.name} '
              f'Возраст: {self.age} '
              f'Недвижимость в собственности: {self.realty} '
              f'Денег на счете: {self.money}.')

    def earn_money(self, money: int):

        self.money += money

    def make_deal(self, obj):

        if self.money >= obj.cost:
            self.money -= obj.cost
            self.realty.append(obj)
            return True

        else:
            print('Работа работой, но время от времени надо работать!')
            return False
