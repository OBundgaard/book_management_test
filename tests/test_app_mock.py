import unittest
from unittest.mock import patch
from models import Book
from app import get_all_books_from_file, sort_books_from_author


class MockTestApp(unittest.TestCase):

    # Testing sorting books [SUCCESS EXPECTED]
    @patch('app.get_all_books_from_file')
    def test_sort_books_from_author_success(self, mock_get_all_books_from_file):
        # Arrange
        mock_get_all_books_from_file.return_value = [
            Book(2, 'Great Expectations', 'Charles Dickens', '1861'),
            Book(1, 'A Tale of Two Cities', 'Charles Dickens', '1859'),
            Book(4, 'Moby Dick', 'Herman Melville', '1851'),
            Book(3, 'Oliver Twist', 'Charles Dickens', '1837'),
        ]

        expected_books = [
            Book(1, 'A Tale of Two Cities', 'Charles Dickens', '1859'),
            Book(2, 'Great Expectations', 'Charles Dickens', '1861'),
            Book(3, 'Oliver Twist', 'Charles Dickens', '1837'),
        ]

        # Act
        result = sort_books_from_author('Charles Dickens')

        # Assert
        self.assertEqual(result, expected_books)

    # Testing sorting books [FAIL EXPECTED]
    @patch('app.get_all_books_from_file')
    def test_sort_books_from_author_fail(self, mock_get_all_books_from_file):
        # Arrange
        mock_get_all_books_from_file.return_value = [
            Book(2, 'Great Expectations', 'Charles Dickens', '1861'),
            Book(1, 'A Tale of Two Cities', 'Charles Dickens', '1859'),
            Book(4, 'Moby Dick', 'Herman Melville', '1851'),
            Book(3, 'Oliver Twist', 'Charles Dickens', '1837'),
        ]

        expected_books = [
            Book(1, 'A Tale of Two Cities', 'Charles Dickens', '1859'),
            Book(2, 'Great Expectations', 'Charles Dickens', '1861'),
            Book(4, 'Moby Dick', 'Herman Melville', '1851'),
        ]

        # Act
        result = sort_books_from_author('Charles Dickens')

        # Assert
        self.assertNotEqual(result, expected_books)


if __name__ == '__main__':
    unittest.main()
