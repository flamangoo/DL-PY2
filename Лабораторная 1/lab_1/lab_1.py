import doctest
from typing import Union


class Keyboard:
    def __init__(self, number_of_keys: int, switch_type: str, need_backlight: bool):
        """
        Создание и подготовка к работе объекта "Клавиатура"

        :param number_of_keys: Количество клавиш
        :param switch_type: Тип переключателей на клавиатуре
        :param need_backlight: Нужно ли включить подсветку?

        >>> keyboard = Keyboard(103, 'красный', True)
        """
        if not isinstance(number_of_keys, int) or number_of_keys < 0:
            raise ValueError('Количество клавиш должно быть целым положительным числом')
        if number_of_keys not in [61, 64, 67, 85, 103]:
            raise ValueError('Форм-фактора такой клавиатуры не существует')
        self.number_of_keys = number_of_keys

        if not isinstance(switch_type, str):
            raise TypeError('Тип переключателя должен быть типа str')
        if switch_type.lower() not in ['синий', 'красный', 'коричневый', 'черный']:
            raise ValueError('Такого типа переключателей не существует')
        self.switch_type = switch_type.lower()
        self.need_backlight = need_backlight

    def backlight_on(self) -> None:
        """
        Метод включает подсветку, если значение True

        >>> keyboard = Keyboard(64, 'Красный', False)
        >>> keyboard.backlight_on()  # меняет значение на True

        """

    def backlight_off(self) -> None:
        """
        Метод выключает подсветку

        >>> keyboard = Keyboard(64, 'Синий', True)
        >>> keyboard.backlight_off()  # меняет значение на False
        """


class Sample:
    def __init__(self, sample_volume: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Образец" - раствора с регулируемой "концентрацией"

        :param sample_volume: Объем образца, мл
        :param material: Материал образца в виде раствора в мл

        >>> sample = Sample(10, 'Тантал')
        """

        if not isinstance(sample_volume, (int, float)) or sample_volume < 0:
            raise TypeError('Объем должен быть положительным числом типа int или float')
        self.sample_volume = sample_volume

        if not isinstance(material, str):
            raise TypeError('Материал образца должен быть типа str')
        self.material = material

    def add_water_to_sample(self, water: float) -> None:
        """
        Добавление воды в образец, создание раствора

        :param water: Объем добавляемой воды, мл

        >>> sample = Sample(10, 'Спирт')
        >>> sample.add_water_to_sample(15)
        """
        if not isinstance(water, (int, float)) or water < 0:
            raise ValueError("Объем жидкости должен быть положительным числом типа int или float")
        self.sample_volume += water

    def add_material_to_sample(self, add_material: int) -> None:
        """
        Добавление в образец материала

        :param add_material: Объем добавляемого образца, мл

        >>> sample = Sample(10, 'Спирт')
        >>> sample.add_material_to_sample(40)
        """
        if not isinstance(add_material, (int, float)) or add_material < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом типа int или float")
        self.sample_volume += add_material


class Coffee:
    def __init__(self, coffee_size: Union[int, float], coffee_sort: str, need_sugar: bool, need_milk: bool):
        """
        Приготовление кофе!

        :param coffee_size: Объем кофе (фиксированные объемы), мл
        :param coffee_sort: Сорт кофе
        :param need_sugar: Нужно ли добавить сахар?
        :param need_milk: Нужно ли добавить молоко?

        >>> coffee = Coffee(300, 'Арабика', False, True)
        """
        if not isinstance(coffee_size, (int, float)):
            raise TypeError('Объем должен быть типа int или float')
        if coffee_size not in [200, 300, 400]:
            raise ValueError('Такого объема нет :(')
        self.coffee_size = coffee_size

        if not isinstance(coffee_sort, str):
            raise TypeError('Сорт кофе должен быть типа str')
        if coffee_sort.lower() not in ['арабика', 'робуста', 'либерика']:
            raise ValueError('Такого сорта нет в наличии')
        self.coffee_sort = coffee_sort
        self.need_sugar = need_sugar
        self.need_milk = need_milk

    def add_sugar(self, sugar: Union[int, float]) -> None:
        if not isinstance(sugar, (int, float)):
            raise ValueError
        print('Добавляем сахар...')
        """
        Добавляется сахар, если значение True

        :param sugar: Порция сахара, г
        
        """
        self.coffee_size += sugar

    def add_milk(self, milk: Union[int, float]) -> None:
        if not isinstance(milk, (int, float)):
            raise ValueError
        print('Добавляем молоко...')
        """
        Добавляется молоко, если значение True

        :param milk: Порция молока, мл
        """
        self.coffee_size += milk


if __name__ == "__main__":
    doctest.testmod()
    pass
