"""
Описать класс Device. Реализовать метод process_doc, который будет генерировать
raise NotImplementedError

Описать класс Scanner, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier
Реализовать метод process_doc, который будет печатать "Сканирую, отправляю факс: {name}"

Создать объект класса MFU. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Device:

    def process_doc(self, name):
        raise NotImplementedError


class Scanner(Device):

    def process_doc(self, name):
        print(f'Сканирую документ: {name}')


class Copier(Device):

    def process_doc(self, name):
        print(f'Делаю копию: {name}')


class MFU(Scanner, Copier):

    def process_doc(self, name):
        print(f'Сканирую, отправляю факс: {name}')


mfu = MFU()

mfu.process_doc('Приказ №1')

print(MFU.mro())
