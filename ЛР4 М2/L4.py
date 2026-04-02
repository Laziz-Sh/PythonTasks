class Vehicle:
    """
    Базовый класс Транспорт

    :param brand: марка
    :param speed: скорость
    """

    def __init__(self, brand: str, speed: float):
        self._brand = brand  # защищённый атрибут (инкапсуляция)
        self.speed = speed

    def move(self) -> str:
        """
        Движение транспорта

        :return: строка с описанием движения
        """
        return f"{self._brand} движется со скоростью {self.speed}"

    def __str__(self) -> str:
        return f"Транспорт {self._brand}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, speed={self.speed})"


class Car(Vehicle):
    """
    Дочерний класс Легковой автомобиль

    :param doors: количество дверей
    """

    def __init__(self, brand: str, speed: float, doors: int):
        super().__init__(brand, speed)
        self.doors = doors

    def move(self) -> str:
        """
        Переопределение метода движения.

        Причина:
        Легковой автомобиль уточняет поведение базового транспорта,
        добавляя информацию о количестве дверей.
        """
        return f"Автомобиль {self._brand} едет со скоростью {self.speed}, дверей: {self.doors}"

    def honk(self) -> str:
        """
        Уникальный метод автомобиля

        :return: сигнал
        """
        return "Бип-бип!"

    def __str__(self) -> str:
        return f"Автомобиль {self._brand}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, speed={self.speed}, doors={self.doors})"


if __name__ == "__main__":
    car = Car("Toyota", 120, 4)

    print(car)          # __str__
    print(repr(car))    # __repr__
    print(car.move())   # переопределённый метод
    print(car.honk())   # свой метод