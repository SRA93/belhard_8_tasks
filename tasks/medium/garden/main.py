from gardener import Gardener
from tomato import Tomato
from tomato_bush import TomatoBush

if __name__ == '__main__':

    bush_one = TomatoBush(Tomato(8), Tomato(4), Tomato(3))
    bush_two = TomatoBush(Tomato(6), Tomato(1), Tomato(2))

    gardener_person = Gardener('SRA93', bush_one, bush_two)
    gardener_person.work()

    while True:

        if gardener_person.harvest() is None:
            gardener_person.work()

        else:
            print(f'Cобрано {len(gardener_person.harvest())} спелых томатов.')

            break
