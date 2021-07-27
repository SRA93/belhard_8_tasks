"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.
До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}
После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""

import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        start_time = time.time()
        print(f'Время начала: {start_time}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        end_time = time.time()
        difference = end_time - start_time
        print(f'Время окончания: {end_time}')
        print(f'Всего затрачено времени на выполнение: {difference}')

        return result

    return wrapper


def cl_benchmark(cls):
    attrs = {key: value for key, value in cls.__dict__.items() if callable(value)}

    for name, val in attrs.items():
        decorated = benchmark(val)
        setattr(cls, name, decorated)

    return cls


@cl_benchmark
class Phone:
    brand = str
    model = str
    issue_year = int

    def __init__(self, brand: str, model: str, issue_year: int):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        return (f'Бренд: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'Год выпуска: {self.issue_year}')

    def get_info(self):
        return self.brand, self.model, self.issue_year

    @staticmethod
    def receive_call(name: str):
        print(f'Звонит {name}')


mob_phone = Phone('iFruit', '5', 2013)

print(mob_phone)
mob_phone.receive_call('Майк')
print(mob_phone.get_info())
