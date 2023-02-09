from typing import Union


class Plant:
    def __init__(self, age: int, height: Union[int, float], soil_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Растение"

        :param age: возраст растения
        :param height: высота растения
        :param soil_volume: объем почвы в емкости
        """

        self._age = None  # Будем считать, что это неизменная характеристика, тоже Protected
        self._init_age(age)

        self._height = None  # Также неизменная характеристика
        self._init_height(height)

        self._soil_volume = None  # Меняется только при удобрении - поэтому Protected
        self._init_soil_volume(soil_volume)

    def __str__(self) -> str:
        """ Печать экземпляра класса """
        return f'Это растение. Возраст - {self.age} лет, высота - {self.height} м, объем почвы: {self.soil_volume} л.'

    def __repr__(self) -> str:
        """ Вид экземпляра класса при примененении repr() """
        return f'{self.__class__.__name__}(age={self.age}, height={self.height}, soil_volume={self.soil_volume!r})'

    def _init_age(self, age: int) -> None:
        """
        Инициализация атрибута _age - возраст растения (годы)
        :param age: возвраст растения
        """
        if not isinstance(age, int):
            raise TypeError('Возраст растения должен быть целым числом')
        if age < 0:
            raise ValueError('Возраст растения должен быть положительным числом')
        self._age = age

    def _init_height(self, height: Union[int, float]) -> None:
        """
        Инициализация атрибута _height - высота растения (в метрах)
        Protected, так как используется только при инициализации
        :param height: высота растения
        """
        if not isinstance(height, int):
            raise TypeError('Высота растения должна быть типа int или float')
        if height < 0:
            raise ValueError('Высота растения должна быть положительным числом')
        self._height = height

    def _init_soil_volume(self, soil_volume: Union[int, float]) -> None:
        """
        Инициализация атрибута soil_volume - объем почвы (в литрах)
        Protected, так как используется только при инициализации
        :param soil_volume: объем почвы
        """
        if not isinstance(soil_volume, Union[int, float]):
            raise TypeError('Объем почвы должен быть типа int или float')
        if soil_volume < 0:
            raise ValueError('Объем почвы должен быть положительным числом')
        self._soil_volume = soil_volume

    @property
    def age(self) -> int:
        """ getter для атрибута _age
        в protected атрибуте setter не используется
        """
        return self._age

    @property
    def height(self) -> int:
        """ getter для атрибута _height
        в protected атрибуте setter не используется
        """
        return self._height

    @property
    def soil_volume(self) -> int:
        """ getter для атрибута _soil_volume
        в protected атрибуте setter не используется
        """
        return self._soil_volume

    def add_fertilizer(self, fertilizer: float) -> None:
        """
        Добавить удобрение в почву
        :param fertilizer: удобрение, литр (не больше 0.3 л, поэтому float)
        """
        if not isinstance(fertilizer, float):
            raise TypeError('Количество удобрения типа float и не должно быть больше 0.3 литра')
        if fertilizer > 0.3:
            raise ValueError('Количество удобрения не должно быть больше 0.3 литра')
        if fertilizer < 0:
            raise ValueError('Количество удобрения должно быть положительным числом')
        self._soil_volume += fertilizer


class Araucaria(Plant):
    def __init__(self, age: int, height: Union[int, float], soil_volume: float, need_watering: bool):
        """
        Создание и подготовка к работе объекта "Араукария"

        :param age: возраст растения
        :param height: высота растения
        :param soil_volume: объем почвы
        :param need_watering: флаг, определяющий, нужен ли полив
        """
        super().__init__(age, height, soil_volume)
        self.need_watering = need_watering

    def __str__(self):
        super_str = super().__str__()
        if self.need_watering is True:
            return f"{super_str} {__class__.__name__} нуждается в поливе!"
        else:
            return f"{super_str} {__class__.__name__} не нуждается в поливе :)"

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода родительского класса
        """
        return f'{self.__class__.__name__}(age={self.age}, height={self.height}, soil_volume={self.soil_volume}, ' \
               f'need_watering={self.need_watering})'

    @property
    def need_watering(self) -> bool:
        """ Возвращает True, если полив нужен, и False, если не нужен """
        return self._need_watering

    @need_watering.setter
    def need_watering(self, need_watering: bool) -> None:
        if not isinstance(need_watering, bool):
            raise TypeError('Число должно быть логического типа: либо True, либо False')
        self._need_watering = need_watering

    def watering(self, water: Union[float], need_watering: bool) -> None:
        """
        Метод совершает полив араукарии, если значение True
        :param water: количество воды, литр
        :param need_watering: нужно ли полить растение?
        """
        if need_watering is True:
            if not isinstance(water, float):
                raise TypeError('Количество воды типа float и не должно быть больше 0.5 литра')
            if water > 0.5:
                raise ValueError('Количество воды не должно быть больше 0.5 литра')
            if water < 0:
                raise ValueError('Количество воды должно быть положительным числом')
            self._soil_volume += water

    def add_fertilizer(self, fertilizer: float) -> None:
        """
        Добавить удобрение в почву.
        Является перегрузкой родительского класса, так как удобряем растение
        :param fertilizer: удобрение, в литрах (не больше 0.3 л, поэтому float)
        """
        if not isinstance(fertilizer, float):
            raise TypeError('Количество удобрения типа float и не должно быть больше 0.3 литра')
        if fertilizer > 0.3:
            raise ValueError('Количество удобрения не должно быть больше 0.3 литра')
        if fertilizer < 0:
            raise ValueError('Количество удобрения должно быть положительным числом')
        self._soil_volume += fertilizer


class Fittonia(Plant):
    def __init__(self, age: int, height: Union[int, float], soil_volume: float, need_pruning: bool):
        """
        Создание и подготовка к работе объекта "Фиттония"

        :param age: возраст растения
        :param height: высота растения
        :param soil_volume: объем почвы
        :param need_pruning: флаг, определяющий, нужна ли растению подрезка
        """
        super().__init__(age, height, soil_volume)
        self.need_pruning = need_pruning

    def __str__(self):
        super_str = super().__str__()
        if self.need_pruning is True:
            return f"{super_str} {__class__.__name__} нуждается в подрезке!"
        else:
            return f"{super_str} {__class__.__name__} не нуждается в подрезке :)"

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода родительского класса
        """
        return f'{self.__class__.__name__}(age={self.age}, height={self.height}, soil_volume={self.soil_volume}, ' \
               f'need_pruning={self.need_pruning})'

    @property
    def need_pruning(self) -> bool:
        """ Возвращает True, если подрезка нужна, и False, если не нужна """
        return self._need_pruning

    @need_pruning.setter
    def need_pruning(self, need_pruning: bool) -> None:
        if not isinstance(need_pruning, bool):
            raise TypeError('Число должно быть логического типа: либо True, либо False')
        self._need_pruning = need_pruning

    def pruning(self, need_pruning: bool) -> None:
        """
        Метод совершает подрезку фиттонии, если значение True
        :param need_pruning: нужна ли подрезка?
        """
        if need_pruning is True:
            ...

    def add_fertilizer(self, fertilizer: float) -> None:
        """
        Добавить удобрение в почву.
        Является перегрузкой родительского класса, так как удобряем растение
        :param fertilizer: удобрение, в литрах (не больше 0.3 л, поэтому float)
        """
        if not isinstance(fertilizer, float):
            raise TypeError('Количество удобрения типа float и не должно быть больше 0.3 литра')
        if fertilizer > 0.3:
            raise ValueError('Количество удобрения не должно быть больше 0.3 литра')
        if fertilizer < 0:
            raise ValueError('Количество удобрения должно быть положительным числом')
        self._soil_volume += fertilizer


if __name__ == "__main__":
    '''based_plant = Plant(1, 1, 2)
    first_plant = Araucaria(1, 2, 4, False)
    second_plant = Fittonia(2, 1, 3, True)
    print(based_plant, first_plant, second_plant, sep='\n')'''
