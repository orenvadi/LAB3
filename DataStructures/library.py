from prettytable import PrettyTable


class Book:
    def __init__(self, udk, author, title, year, quantity) -> None:
        self.udk: int = udk
        self.author: str = author
        self.title: str = title
        self.publishing_year: int = year
        self.book_quantity: int = quantity
        self.taken: int = 0

    def take(self) -> None:
        if self.book_quantity >= 1:
            self.book_quantity -= 1
            self.taken += 1
            print(f"You have take the book {self.title}")
        else:
            print("You can't take book, all of them already taken")

    def back(self) -> None:
        if self.taken >= 1:
            self.book_quantity += 1
            self.taken -= 1
            print(f"You have back the book {self.title}")
        else:
            print("You can't back this book, all of them already here")

    def get_udk(self) -> int:
        return self.udk

    def get_info(self) -> list[str]:
        return [
            str(i)
            for i in [
                self.udk,
                self.author,
                self.title,
                self.publishing_year,
                self.book_quantity,
            ]
        ]

    def __str__(self) -> str:
        return str(
            [
                self.udk,
                self.author,
                self.title,
                self.publishing_year,
                self.book_quantity,
            ]
        )


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def take_book(self, udk: int) -> str:
        for book in self.books:
            if book.get_udk() == udk:
                book.take()
                print("You successfully took book")
                return "success"
        return "fail"

    def back_book(self, udk: int) -> str:
        for book in self.books:
            if book.get_udk() == udk:
                book.back()
                print("You successfully back book")
                return "success"
        return "fail"

    def search_book(self, udk: int) -> str:
        for book in self.books:
            if book.get_udk() == udk:
                print(book)
                return str(book)
        print("book not found")
        return "not found"

    def show_books(self) -> None:
        table = PrettyTable()
        table.field_names = ["udk", "author", "title", "year", "quantity"]
        for book in self.books:
            table.add_row(book.get_info())

        print(table)


bishkek_state_library = Library()

# udk, author, title, year, quantity
bishkek_state_library.add_book(Book(111, "Aitamatov.Ch.T", "Jamila", 1999, 11))
bishkek_state_library.add_book(Book(112, "Aitamatov.Ch.T", "Plaha", 1979, 10))
bishkek_state_library.add_book(Book(113, "Aitamatov.Ch.T", "White ship", 1969, 18))
bishkek_state_library.add_book(
    Book(114, "Aitamatov.Ch.T", "The day longer that thecentury", 1975, 9)
)
bishkek_state_library.add_book(
    Book(115, "Aitamatov.Ch.T", "Zeitunget Juidon", 1984, 21)
)
bishkek_state_library.add_book(Book(116, "Aitamatov.Ch.T", "Face to face", 1971, 31))


bishkek_state_library.show_books()

bishkek_state_library.search_book(111)
bishkek_state_library.take_book(111)
bishkek_state_library.search_book(111)
bishkek_state_library.back_book(111)
bishkek_state_library.search_book(111)
