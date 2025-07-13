# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_borrowed(self):
        self.is_borrowed = True

    def mark_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_borrowed()
            self.borrowed_books.append(book)
            print(f"{book.title} borrowed.")
        else:
            print("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book)
            print(f"{book.title} returned.")
        else:
            print("You did not borrow this book.")

    def list_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        for b in self.borrowed_books:
            print(b.title)

