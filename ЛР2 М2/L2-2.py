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


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            if not isinstance(books, list):
                raise TypeError
            self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))