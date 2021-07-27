"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    a_type: str

    @abstractmethod
    def says(self):
        pass


class Cat(Animal):

    def __init__(self, name: str, a_type: str):

        self.name = name
        self.a_type = a_type

    def says(self):
        print(f"Кошка {self.name} говорит МЯУ")


class Dog(Animal):

    def __init__(self, name: str, a_type: str):

        self.name = name
        self.a_type = a_type

    def says(self):
        print(f"Собака {self.name} говорит ГАВ")


class Cow(Animal):

    def __init__(self, name: str, a_type: str):

        self.name = name
        self.a_type = a_type

    def says(self):
        print(f"Корова {self.name} говорит МУ")
