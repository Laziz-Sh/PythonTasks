import doctest


class Phone:
    def __init__(self, brand: str, battery_level: float):
        """
        Класс Телефон

        :param brand: марка телефона
        :param battery_level: уровень заряда

        >>> phone = Phone("iPhone", 50)
        """
        if not isinstance(brand, str):
            raise TypeError
        if not brand:
            raise ValueError

        if not isinstance(battery_level, (int, float)):
            raise TypeError
        if not (0 <= battery_level <= 100):
            raise ValueError

        self.brand = brand
        self.battery_level = battery_level

    def make_call(self, minutes: int) -> None:
        """
        Совершить звонок

        >>> phone = Phone("iPhone", 50)
        >>> phone.make_call(10)
        """
        ...

    def charge(self, amount: float) -> None:
        """
        Зарядить телефон

        >>> phone = Phone("iPhone", 50)
        >>> phone.charge(20)
        """
        ...


class Book:
    def __init__(self, title: str, pages: int, current_page: int):
        """
        Класс Книга

        >>> book = Book("Python", 300, 0)
        """
        if not isinstance(title, str):
            raise TypeError
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError

        if not isinstance(current_page, int):
            raise TypeError
        if not (0 <= current_page <= pages):
            raise ValueError

        self.title = title
        self.pages = pages
        self.current_page = current_page

    def read(self, pages: int) -> None:
        """
        Чтение книги

        >>> book = Book("Python", 300, 0)
        >>> book.read(50)
        """
        ...

    def is_finished(self) -> bool:
        """
        Проверка дочитана ли книга

        >>> book = Book("Python", 100, 100)
        >>> book.is_finished()
        """
        ...


class BankAccount:
    def __init__(self, balance: float):
        """
        Банковский счет

        >>> acc = BankAccount(1000)
        """
        if not isinstance(balance, (int, float)):
            raise TypeError
        if balance < 0:
            raise ValueError

        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета

        >>> acc = BankAccount(1000)
        >>> acc.deposit(500)
        """
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег

        >>> acc = BankAccount(1000)
        >>> acc.withdraw(300)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()