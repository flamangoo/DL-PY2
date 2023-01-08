BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('id должен быть целым положительным числом')
        if id_ <= 0:
            raise ValueError('id должен быть больше 0')
        if not isinstance(name, str):
            raise TypeError('Переменная name (название книги) должна быть типа str')
        if pages <= 0 or not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть целым положительным числом')

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list[Book] = None):  # аргумент по умолчанию
        if books is None:
            self.books = []  # если пользователь не передает значение, инициализируем пустой список
        else:
            for _ in books:
                self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1  # если книг нет, то возвращаем 1
        else:
            return self.books[-1].id_ + 1  # возвращаем следующий id

    def get_index_by_book_id(self, id_) -> int:
        if id_ <= 0 or not isinstance(id_, int):
            raise TypeError('id должен быть целым положительным числом')
        for index, book in enumerate(self.books):
            if id_ == book.id_:
                return index
            else:
                raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
