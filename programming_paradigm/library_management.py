class Book:
    def __init__(self, title, author):
            self.title = title
            self.author = author
            self._is_checked_out = False

    # Take the book 
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True 
            return True 
        return False             

    # Check if book is available 
    def is_available(self):
        return not self._is_checked_out
    
    # Return the book
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # String representation of book title and author
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    # Add book to the library
    def add_book(self, book):
        self._books.append(book) 

    # List available books
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(str(book))

    # Check out book from library 
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False      
    

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
