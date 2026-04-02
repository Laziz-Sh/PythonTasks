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


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        # проверки
        if not isinstance(id_, int):
            raise TypeError("ID должен быть int")
        if id_ <= 0:
            raise ValueError("ID должен быть положительным")

        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not name:
            raise ValueError("Название не может быть пустым")

        if not isinstance(pages, int):
            raise TypeError("Страницы должны быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # проверка __str__

    print(list_books)  # проверка __repr__