"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:

    fio: str
    phone: str

    def __init__(self, fio, phone):
        self.fio = fio
        self.phone = phone


class LibraryReader(Person):
    client_id: int
    books: list

    def __init__(self, fio: str, phone: str, client_id: int, books: list):

        super().__init__(fio, phone)
        self.client_id = client_id
        self.books = books

    def take_book(self, *args):

        for book_name in args:
            self.books.append(book_name)

        if len(args) < 4:
            print(f'{self.fio} взял книги: {self.books}')

        else:
            print(f'{self.fio} взял {len(args)} книги')

    def return_book(self, *args):

        if len(args) >= 3:
            print(f'{self.fio} вернул {len(args)} книги')

        for book_name in args:

            if book_name not in self.books:
                print(f'{self.fio} не брал {book_name}')

            else:
                self.books.remove(book_name)

        print(f'{self.fio} вернул {args}')


reader = LibraryReader('Петров', '+375331111111', 67333, [])
reader.take_book('Приключения', 'Словарь', 'Энциклопедия')
reader.return_book('Приключения', 'Словарь', 'Энциклопедия', 'Рассказы')
