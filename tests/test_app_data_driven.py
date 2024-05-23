import json
import unittest
from models import Book
from app import app
import ddt


@ddt.ddt
class DataTestApp(unittest.TestCase):
    def setUp(self):
        # Setting up the testing itself
        self.app = app.test_client()
        self.app.testing = True

    @ddt.data(
        Book(book_id=7, title='Sample book', author='Sample author', published_date='1970-1-1').to_dict(),
        Book(book_id=8, title='Sample book', author='Sample author', published_date='1970-1-1').to_dict(),
        Book(book_id=9, title='Sample book', author='Sample author', published_date='1970-1-1').to_dict(),
    )
    def test_post_books(self, case):
        # Arrange
        data = json.dumps(case)

        # Act
        response = self.app.post('/books', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], case['title'])

    @ddt.data(4, 5, 6)
    def test_get_books(self, case):
        # Arrange
        book_id = case

        # Act
        response = self.app.get(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)

    @ddt.data(
        Book(book_id=1, title='Sample book', author='A python developer', published_date='1970-1-1'),
        Book(book_id=4, title='Sample book', author='A python developer', published_date='1970-1-1'),
        Book(book_id=5, title='Sample book', author='A python developer', published_date='1970-1-1'),
    )
    def test_put_books(self, case):
        # Arrange
        updated_book = case.to_dict()
        data = json.dumps(updated_book)
        book_id = case.book_id

        # Act
        response = self.app.put(f'/books/{book_id}', data=data, content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['author'], 'A python developer')

    @ddt.data(1, 2, 3)
    def test_delete_books(self, case):
        # Arrange
        book_id = case

        # Act
        response = self.app.delete(f'/books/{book_id}')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Book deleted')


if __name__ == '__main__':
    unittest.main()
