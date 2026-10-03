class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }
        self.books.append(book)

    def get_books(self):
        return self.books

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None


if __name__ == "__main__":
    library = LibraryCatalog()

    library.add_book("1984", "George Orwell")
    library.add_book("The Hobbit", "J.R.R. Tolkien")

    print("Библиотечный каталог:")
    
    for book in library.get_books():
        print(f'{book["title"]} — {book["author"]}')

    result = library.search_book("1984")

    if result:
        print("\nКнига найдена:")
        print(f'{result["title"]} — {result["author"]}')
    else:
        print("\nКнига не найдена.")