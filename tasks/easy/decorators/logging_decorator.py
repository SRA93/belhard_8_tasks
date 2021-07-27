"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_deco(func):

    def wrapper(*args, **kwargs):

        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')

        return result

    return wrapper


def cl_deco(cls):

    attrs = {key: value for key, value in cls.__dict__.items() if callable(value)}

    for name, val in attrs.items():

        decorated = log_deco(val)
        setattr(cls, name, decorated)

    return cls


@cl_deco
class TextClass:

    def __init__(self):
        pass

    def text_func(self):
        print('Лето мешает вовремя выполнять ДЗ')


res = TextClass()
res.text_func()
