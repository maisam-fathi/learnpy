# Python Exercise: Library Book Management with OOP and Methods

from datetime import datetime


# Description:
# Create a program that manages books in a library using a Book class.

# Tasks:

# 1. Define a class called Book with the following:
#    - Class variable: total_books (to count how many books have been created)
#    - Instance variables: title (string), author (string), year (int), is_checked_out (bool, default False)
class Book:
    total_books = 0

    # 2. Implement the following methods inside the Book class:
    #    - __init__(self, title, author, year): constructor that sets the attributes and increments total_books
    #    - check_out(self): sets is_checked_out to True and prints "<title> has been checked out."
    #    - return_book(self): sets is_checked_out to False and prints "<title> has been returned."
    #    - get_info(self): prints the book info in the format: "Title: <title>, Author: <author>, Year: <year>, Checked out: <True/False>"
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out
        Book.total_books += 1

    def check_out(self):
        if self.is_checked_out:
            print('%s has already checked out!' % self.title)
        else:
            self.is_checked_out = True
            print('%s has been checked out.' % self.title)

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print('%s has been returned.' % self.title)
        else:
            print('%s has already returned!' % self.title)

    def get_info(self):
        status = "Yes" if self.is_checked_out else "No"
        print('Title: %s, Author: %s, Year: %i, Checked out: %s' % (self.title, self.author, self.year,
                                                                    status))

    def age_of_book(self, current_year):
        age_info = '%s is %i years old.' % (self.title, current_year - self.year)
        return age_info


# 3. Outside the class:
#    - Create at least 3 Book objects with different data.
#    - Call their methods to simulate checking out and returning books.
#    - Print total number of books using Book.total_books.
_1984 = Book('1984', 'Orwell', 1949, True)
dune = Book('Dune', 'Herbert', 1965)
fahrenheit = Book('Fahrenheit', 'Bradbury', 1953, True)
sapiens = Book('Sapiens', 'Harari', 2011)
it = Book('It', 'King', 1986, True)

_1984.get_info()
dune.get_info()
fahrenheit.get_info()
sapiens.get_info()
it.get_info()
print('******')
_1984.return_book()
dune.check_out()
fahrenheit.return_book()
sapiens.check_out()
it.return_book()
it.return_book()
print('******')
_1984.get_info()
dune.get_info()
fahrenheit.get_info()
sapiens.get_info()
it.get_info()
print('******')
print('Total number of books: %i' % Book.total_books)
print('******')

# Bonus (optional):
# - Add a method called age_of_book(self, current_year) that calculates how old the book is and returns the age.
# - Use that method to print how old each book is.
current_year = datetime.now().year
print(_1984.age_of_book(current_year))
print(dune.age_of_book(current_year))
print(fahrenheit.age_of_book(current_year))
print(sapiens.age_of_book(current_year))
print(it.age_of_book(current_year))

# This exercise will help practice:
# - Class and instance variables
# - Instance methods
# - Creating objects and calling their methods
# - Using print formatting and basic logic inside methods