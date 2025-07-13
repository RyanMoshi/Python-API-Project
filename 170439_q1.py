# 170439_q1.py
# This Is A Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            return f"The book has been checked out."
        else:
            return f"This book is already checked out."
        
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            return f"The book has been returned."
        else:
            return f"This book wasn't checked out."
        
class LibraryMember:
    def __init__(self, name, memberID):
        self.name = name
        self.memberID = memberID
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.is_borrowed == False:
            book.borrow()
            self.borrowed_books.append(book)
            return f"{book.title} has been borrowed by {self.name}."
        else:
            return f"{book.title} is not available right now."
            
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{book.title} has been returned by {self.name}."
        else:
            return f"{self.name} didn't borrow {book.title}."
                
    def ListBorrowedBooks(self):
        if self.borrowed_books:
            return [book.title for book in self.borrowed_books]
        else:
            return "No books currently borrowed."

if __name__ == "__main__":
    book1 = Book("Python Fundamentals", "Kuol Abraham")
    book2 = Book("Deep Learning with Python", "Joy Mbinya")
    book3 = Book("AI for Beginners", "Samuel Githongori")
    book4 = Book("Data Structures in Practice", "Eurel Owatte")
    
    member1 = LibraryMember("Ryan Moshi", 101)
    member2 = LibraryMember("Brian Kikuvi", 102)
    member3 = LibraryMember("Caleb Katumo", 103)
    member4 = LibraryMember("Mumo Mwangagi", 104)
    
    print(member3.borrow_book(book2))
    print(member4.borrow_book(book1))
    print(member4.borrow_book(book1))
    
    print(member3.ListBorrowedBooks())
    print(member4.ListBorrowedBooks())
    
    print("Books borrowed by Mumo:", member4.ListBorrowedBooks())
    
    print(member3.return_book(book2))
    
    print("Mumo's borrowed books after returning:", member4.ListBorrowedBooks())
