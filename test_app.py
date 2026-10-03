import unittest
from app import LibraryCatalog


class TestLibraryCatalog(unittest.TestCase):

    def test_add_book(self):
        library = LibraryCatalog()

        library.add_book("1984", "George Orwell")

        self.assertEqual(len(library.get_books()), 1)

    def test_search_book(self):
        library = LibraryCatalog()

        library.add_book("1984", "George Orwell")

        result = library.search_book("1984")

        self.assertIsNotNone(result)
        self.assertEqual(result["author"], "George Orwell")


if __name__ == "__main__":
    unittest.main()