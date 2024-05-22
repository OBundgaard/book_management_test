import unittest
from models import Book


class TestBookCreation(unittest.TestCase):
    def test_book_creation(self):
        test_cases = [
            (1, 'Test Book 1', 'Author 1', '2022-01-01'),
            (2, 'Test Book 2', 'Author 2', '2023-01-01'),
            (3, 'Test Book 3', 'Author 3', '2024-01-01'),
            (4, 'Test Book 34', 'Author 3', '2024-01-01'),
            (5, 'Test Book 36', 'Author 3', '2024-01-01'),
            (6, 'Test Book 312', 'Author 3', '2024-01-01'),
        ]
        for book_id, title, author, published_date in test_cases:
            with self.subTest(book_id=book_id, title=title, author=author, published_date=published_date):
                book = Book(book_id=book_id, title=title, author=author, published_date=published_date)
                self.assertEqual(book.book_id, book_id)
                self.assertEqual(book.title, title)
                self.assertEqual(book.author, author)
                self.assertEqual(book.published_date, published_date)


if __name__ == '__main__':
    unittest.main()
