from datetime import datetime


class Book:
    def __init__(self, book_id: int, title: str, author: str, published_date: str | datetime):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.published_date = published_date

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.book_id, self.title, self.author, self.published_date) == (other.book_id, other.title, other.author, other.published_date)

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date
        }