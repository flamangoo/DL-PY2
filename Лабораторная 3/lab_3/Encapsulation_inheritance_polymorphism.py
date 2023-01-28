class Book:
    """ Базовый класс книги """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Возвращает название книги """
        return self._name

    @property
    def author(self) -> str:
        """ Возвращает имя автора книги """
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц книги """
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError('Количество страниц является числом типа int')
        if pages < 1:
            raise ValueError('Количество страниц должно быть больше 0')
        self._pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги """
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError('Продолжительность аудиокниги может быть только числом типа float')
        if duration <= 0:
            raise ValueError('Продолжительность аудиокниги не может быть меньше 0')
        self._duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
