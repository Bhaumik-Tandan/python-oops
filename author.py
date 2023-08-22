"""
Question 5: Composition
Design a class Author with attributes name and books_written. 
Create a class Book with attributes title, published_year, and author (an instance of Author). 
Implement methods to add books to an author's list and to display all books written by an author.
"""

class Author:
    def __init__(self, name):
        self.name = name
        self.books_written = []

    def add_book(self, book:"Book"):
        self.books_written.append(book)

    def display_books(self):
        print(f"Books written by {self.name}:")
        for book in self.books_written:
            print(f"Title: {book.title}, Published Year: {book.published_year}")

class Book:
    def __init__(self, title, published_year):
        self.title = title
        self.published_year = published_year
        self.author = None

    def assign_author(self, author:"Author"):
        self.author = author
        author.add_book(self)

# Creating authors
author1 = Author("J.K. Rowling")
author2 = Author("George Orwell")

# Creating books
book1 = Book("Harry Potter and the Sorcerer's Stone", 1997)
book2 = Book("1984", 1949)

# Assigning authors to books
book1.assign_author(author1)
book2.assign_author(author2)

# Displaying books by authors
author1.display_books()
author2.display_books()
