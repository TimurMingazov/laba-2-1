# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Animal:
    def __init__(self, name: str, age: int):
        """
                Создание и подготовка к работе объекта "Животное"

                :param name: Вид животного (кот, собака, попугай и тд)
                :param age: возраст животного

                Примеры:
                >>> animal = Animal('Кот', 2)  # инициализация экземпляра класса
                """
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

    def fly(self) -> bool:
        """Проверяет, может ли животное летать

        :return: может ли животное летать

        >>> animal = Animal('Кот', 2)
        >>> animal.fly()
        """
    def make_sound(self) -> str:
        """Производит звук.

        :return: Выводит звук, который издает животное

        >>> animal = Animal('Кот', 2)
        >>> animal.make_sound()
        """
        ...


class Car:

    def __init__(self, color: str, model: str):
        """
                        Создание и подготовка к работе объекта "Машина"

                        :param color: Цвет машины
                        :param model: марка машины

                        Примеры:
                        >>> auto = Car('red', 'Toyota')  # инициализация экземпляра класса
                        """
        self.color = color
        self.model = model
        self.speed = 0

    def add_speed(self, speed: int) -> int:
        """Увеличивает скорость
        :param speed: увеличивает скорость

        :raise ValueError: Если скорость выше определенной, то вызываем ошибку

        :return: выдает скорость

        >>> auto = Car('red', 'Toyota')
        >>> auto.add_speed(50)
        """
        if not isinstance(speed, int):
            raise TypeError("Скорость должен быть типа int")
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.speed = speed

    def engine(self) -> bool:
        """
        Проверяет включен ли двигатель

        return: Включен ли двигатель автомобиля

        >>> auto = Car('red', 'Toyota')
        >>> auto.engine()
        """
        ...


class Book:
    def __init__(self, title: str, author: str):
        """
                        Создание и подготовка к работе объекта "Книга"

                        :param title: Название книги
                        :param author: Автор книги

                        Примеры:
                        >>> book = Book('Колобок', 'Толстой А. Н.')  # инициализация экземпляра класса
                        """
        self.title = title
        self.author = author

    def open(self, page_number: int) -> int:
        """Открывает книгу на заданной странице.

        :param page_number: номер страницы

        :raise ValueError: Номер страницы положительное число

        :return: текст страницы

        >>> book = Book('Колобок', 'Толстой А. Н.')
        >>> book.open(2)
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page_number <= 0:
            raise ValueError("Номер страницы должн быть положительным числом")
        ...

    def close(self) -> bool:
        """Закрыта ли книга

        :return: Закрыта ли книга

        >>> book = Book('Колобок', 'Толстой А. Н.')
        >>> book.close()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
