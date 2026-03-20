# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
bytes_per_symbol = 4
book_size = pages * lines * symbols * bytes_per_symbol
books_count = int(disk_size // book_size)

print("Количество книг, помещающихся на дискету:", books_count)
