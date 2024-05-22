import json
import unittest
from app import app


class TestApp(unittest.TestCase):
    def set_up(self):
        # Setting up the testing itself
        self.app = app.test_client()
        self.app.testing = True

        # Sample data for later use
        self.sample_book = {
            'book_id': 1,
            'title': 'Python 101: Coding Exercises for Beginners',
            'author': 'John W. Doe',
            'published_date': '2024-03-01'
        }

    # Testing method for post_book
    def test_post_book(self):
        # Arrange
        data = json.dumps(self.sample_book)

        # Act
        response = self.app.post('/books', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], self.sample_book['title'])

    # Testing method for get_book
    def test_get_book_one(self):
        # Arrange
        book_id = 1

        # Act
        response = self.app.get(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)

    # Testing method for get_all_books
    def test_get_all_books(self):
        # Act
        response = self.app.get('/books')

        # Assert
        self.assertEqual(response.status_code, 200)

    # Testing method for put_book
    def test_put_book(self):
        # Arrange
        updated_book = self.sample_book
        updated_book['author'] = 'John W. Doe, Jane L. Doe'
        data = json.dumps(updated_book)

        # Act
        response = self.app.put('/books/1', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['author'], 'John W. Doe, Jane L. Doe')

    # Testing method for delete_book
    def test_delete_book_one(self):
        # Arrange
        book_id = 1

        # Act
        response = self.app.delete(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Book deleted')


if __name__ == '__main__':
    unittest.main()
