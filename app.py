from flask import Flask, request, jsonify
from models import Book

app = Flask(__name__)
books = {
    1: Book(book_id=1, title='Sample book', author='Sample author', published_date='1970-1-1'),
    2: Book(book_id=2, title='Sample book', author='Sample author', published_date='1970-1-1'),
    3: Book(book_id=3, title='Sample book', author='Sample author', published_date='1970-1-1'),
    4: Book(book_id=4, title='Sample book', author='Sample author', published_date='1970-1-1'),
    5: Book(book_id=5, title='Sample book', author='Sample author', published_date='1970-1-1'),
    6: Book(book_id=6, title='Sample book', author='Sample author', published_date='1970-1-1'),
}


@app.route('/books', methods=['POST'])
def post_book():
    # Obtain the data from the request
    data = request.get_json()

    # Find the book by ID
    book = books.get(data['book_id'])

    if book:
        # Return 409
        return jsonify({'message': 'Book already exists'}), 409

    # Create the book based on the received data
    book = Book(book_id=data['book_id'], title=data['title'], author=data['author'],
                published_date=data['published_date'])

    # Add book and return the book as a dict
    books[book.book_id] = book
    return jsonify(book.to_dict()), 201


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Find the book by ID
    book = books.get(book_id)
    if book:
        # Return book
        return jsonify(book.to_dict())
    else:
        # Return 404
        return jsonify({'message': 'Book not found'}), 404


@app.route('/books', methods=['GET'])
def get_all_books():
    # Return all the books
    return jsonify([book.to_dict() for book in books.values()])


@app.route('/books/<int:book_id>', methods=['PUT'])
def put_book(book_id):
    # Obtain the data from the request
    data = request.get_json()
    # Find the book by ID
    book = books.get(book_id)
    if book:
        # Update book
        book.title = data['title']
        book.author = data['author']
        book.published_date = data['published_date']
    else:
        # Create book
        book = Book(book_id=book_id, title=data['title'], author=data['author'], published_date=data['published_date'])

    # Add or update book, then return
    books[book_id] = book
    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        # Delete book
        del books[book_id]
        return jsonify({'message': 'Book deleted'})
    else:
        # Return 404
        return jsonify({'message': 'Book not found'}), 404


if __name__ == '__main__':
    app.run()
