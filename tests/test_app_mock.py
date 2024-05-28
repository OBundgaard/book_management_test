import unittest
from unittest.mock import patch, MagicMock

from app import app, books


class TestFlaskApp(unittest.TestCase):

    @patch('app.books', {})
    @patch('app.Book')
    @patch('flask.request')
    def test_post_book_already_exists(self, mock_request, MockBook):
        # Setting up the mock data and behavior
        mock_request.get_json.return_value = {
            'book_id': 1,
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-01-01'
        }

        books[1] = MockBook(book_id=1, title='Sample Book', author='Sample Author', published_date='1970-1-1')

        # Creating a test client
        with app.test_client() as client:
            response = client.post('/books')

            # Asserting the response
            self.assertEqual(response.status_code, 409)
            self.assertEqual(response.get_json(), {'message': 'Book already exists'})

    @patch('app.books', {})
    @patch('app.Book')
    @patch('flask.request')
    def test_post_book_success(self, mock_request, MockBook):
        # Setting up the mock data and behavior
        mock_request.get_json.return_value = {
            'book_id': 1,
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-01-01'
        }

        mock_book_instance = MagicMock()
        mock_book_instance.to_dict.return_value = {
            'book_id': 1,
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-01-01'
        }
        MockBook.return_value = mock_book_instance

        # Creating a test client
        with app.test_client() as client:
            response = client.post('/books')

            # Asserting the response
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.get_json(), mock_book_instance.to_dict())
            MockBook.assert_called_once_with(book_id=1, title='New Book', author='New Author',
                                             published_date='2023-01-01')
            self.assertIn(1, books)
            self.assertEqual(books[1], mock_book_instance)


if __name__ == '__main__':
    unittest.main()
