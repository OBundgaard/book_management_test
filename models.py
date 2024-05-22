

class Book:
    def __init__(self, book_id, title, author, published_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.published_date = published_date

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date
        }