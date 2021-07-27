"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says

"""


class Cat:

    @staticmethod
    def says():
        print('кошка говорит мяу')


class Duck:

    @staticmethod
    def says():
        print('утка говорит кря')


class Cow:

    @staticmethod
    def says():
        print('корова говорит муу')


def animal_says(object_name):
    object_name.says()


kote = Cat()
utka = Duck()
korova = Cow()
