"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def decorator_log(func):

    def wrapper(*args, **kwargs):

        print(f'Выполняем {func} с args: {args} и kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func}')

        return result
    return wrapper


class LoggingMeta(type):

    def __new__(mcs, name, bases, attr):

        class_two = super().__new__(mcs, name, bases, attr)
        dict_two = {k: v for k, v in attr.items() if callable(v)}

        for k, v in dict_two.items():
            meth = str(v.__name__)

            if meth.startswith('__'):
                continue

            else:
                val_two = decorator_log(v)
                setattr(class_two, k, val_two)

        return class_two


class Check(metaclass=LoggingMeta):

    check_word: str

    def __init__(self, check_word):
        self.check_word = check_word

    def check_func(self):
        print(f'{self.check_word}')


check = Check("Раз, раз, проверка")
check.check_func()
