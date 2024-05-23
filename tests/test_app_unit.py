import json
import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        # Setting up the testing itself
        self.app = app.test_client()
        self.app.testing = True

    # Testing method for post_book ID 7 [SUCCESS EXPECTED]
    def test_post_book_seven_success(self):
        # Arrange
        sample_book = {
            'book_id': 7,
            'title': 'Sample book',
            'author': 'Sample author',
            'published_date': '1970-01-01'
        }

        data = json.dumps(sample_book)

        # Act
        response = self.app.post('/books', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 201)

    # Testing method for post_book ID 1 [FAIL EXPECTED]
    def test_post_book_one_fail(self):
        # Arrange
        sample_book = {
            'book_id': 1,
            'title': 'Sample book',
            'author': 'Sample author',
            'published_date': '1970-01-01'
        }
        data = json.dumps(sample_book)

        # Act
        response = self.app.post('/books', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 409)

    # Testing method for get_book with ID 1 [SUCCESS EXPECTED]
    def test_get_book_one_success(self):
        # Arrange
        book_id = 1

        # Act
        response = self.app.get(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)

    # Testing method for get_book with ID 8 [FAIL EXPECTED]
    def test_get_book_eight_fail(self):
        # Arrange
        book_id = 8

        # Act
        response = self.app.get(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 404)

    # Testing method for get_all_books
    def test_get_all_books(self):
        # Act
        response = self.app.get('/books')

        # Assert
        self.assertEqual(response.status_code, 200)

    # Testing method for put_book with ID 3 [SUCCESS EXPECTED]
    def test_put_book_three_success(self):
        # Arrange
        updated_book = {
            'book_id': 3,
            'title': 'Sample book',
            'author': 'A python developer',
            'published_date': '1970-01-01'
        }
        data = json.dumps(updated_book)

        # Act
        response = self.app.put(f'/books/{updated_book['book_id']}', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['author'], 'A python developer')

    # Testing method for delete_book with ID 2 [SUCCESS EXPECTED]
    def test_delete_book_two_success(self):
        # Arrange
        book_id = 2

        # Act
        response = self.app.delete(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)

    # Testing method for delete_book with ID 9 [FAIL EXPECTED]
    def test_delete_book_nine_fail(self):
        # Arrange
        book_id = 9

        # Act
        response = self.app.delete(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
