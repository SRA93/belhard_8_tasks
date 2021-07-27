from house import House
from person import Person
from townhouse import TownHouse

if __name__ == '__main__':

    build_1 = House('2-ой пятый перулок 9 мая, 4', 15000, 40)
    build_2 = House('Центральная, 10', 65000, 80)
    build_3 = TownHouse('Замкадная 33', 50000)

    houses = (build_1, build_2, build_3)

    buyer = Person('Джон Смитович', 41)
    buyer.info()
    buyer.earn_money(1000)

    for i in houses:

        while True:

            if buyer.make_deal(i):
                print(buyer.realty)
                break

            else:
                buyer.earn_money(10000)
                print(f'{buyer.name} заработал {buyer.money} долларов')
