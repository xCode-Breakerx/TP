import unittest

from library_clients.library import Library, Book


class MyTestCase(unittest.TestCase):
    def test_something(self):
        library = Library()
        book1 = Book("To Kill a Mockingbird", "Harper Lee")
        book2 = Book("Pride and Prejudice", "Jane Austen")

        library.add_book(book1)  # shouldn't fail

        try:
            # assert that duplicated are tolerated
            library.add_book(book1)
        except Exception as e:
            self.fail(e)

        # assert that there is no default behavior
        with self.assertRaises(TypeError):
            library.add_book()

        # assert that books should be valid
        with self.assertRaises(Exception):
            book3 = Book(None, None)
            library.add_book(book3)

        # assert that the function call is type safe
        with self.assertRaises(Exception):
            library.add_book(None)

        # the rest of the functions do not return any valuable data, thus they cannot be tested
        # fail by default
        self.fail("Missing test cases due to code structure. There is not enough feedback")


if __name__ == '__main__':
    unittest.main()
