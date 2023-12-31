## Python Object-Oriented Programming
***
- [Basic Class](#basic-class)
- [Instance Type](#instance-type)
- [Class Method Attribute](#class-method-attribute)
- [Inheritance](#inheritance)

## Basic Class
***

#### Define a class

    class Book:
        def __init__(self, title, author, pages, price) -> None:
            self.title = title
            self.author = author
            self.pages = pages
            self.price = price
            self.__secret = "top secret"

        def getPrice(self):
            if hasattr(self, '_discount'):
                return self.price - (self.price * self._discount)
            else:
                return self.price

        def setDiscount(self, amount):
            self._discount = amount

Attribute name starts with `_` consider to be private attribute.
But there is a better way to try to hide attribute from outside world by prefixing with `__` double underscore.
Since `_discount` was not declared in the `__init__()` so we have to be check before using it anywhere in the method

#### Create instance

    book1 = Book("Learning Perl", "brian d foy", 800, 50)
    book2 = Book("Perl Hacks", "Damian Conway", 600, 60)

    print(book1.getPrice()) # 50
    print(book2.getPrice()) # 60

    book2.setDiscount(0.25)
    print(book2.getPrice()) # 45

    print(book2.__secret)       # would throw error
    print(book2._Book__secret)  # this can let secret out

## Instance Type
***    

    class Book:
        def __init__(self, title) -> None:
            self.title = title

    class Author:
        def __init__(self, name) -> None:
            self.name = name

    book = Book("Learning Perl")
    author = Author("Damian Conway")

The `type()` function can be used to find out the instance type.

    print(type(book))     # <class '__main__.Book'>
    print(type(author))   # <class '__main__.Author'>

You can compare the instance type like below but not recommended.

    book1 = Book("Learning Perl")
    book2 = Book("Perl Hacks")
    author = Author("Damian Conway")

    print(type(book1) == type(book2))  # True
    print(type(book1) == type(author)) # False

A better comparison would be to use function `isinstance()`.

    print(isinstance(book1, Book)     # True
    print(isinstance(author, Author)) # True
    print(isinstance(author, Book))   # False

Every class in `Python` is a sub class of generic class `object`. So this is perfectly OK.

    print(isinstance(book1, object)   # True

## Class Method Attribute
***

    class Book:
        BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")  # class attribute

        @classmethod
        def get_book_types(cls):
            return cls.BOOK_TYPES

        # static method
        __booklist = None
        def get_book_list():
            if Book.__booklist == None:
                Book.__booklist = []
            return Book.__booklist
            
        def __init__(self, title, booktype) -> None:
            self.title = title

            if not booktype in Book.BOOK_TYPES:
                raise ValueError(f"{booktype} is not a valid booktype.")
            else:
                self.booktype = booktype

Call class method

      print(Book.get_book_types())

      book1 = Book("Learning Perl", "HARDCOVER")  # OK
      book2 = Book("Perl Hacks", "COMIC")         # Throw error

Call static method

      thebooks = Book.get_book_list()
      thebooks.append(Book("Learning Perl", "HARDCOVER"))
      thebooks.append(Book("Perl Hacks", "PAPERBACK"))
      print(thebooks)

## Inheritance
***

Consider the following three class definitions:

    class Book:
        def __init__(self, title, author, pages, price):
            self.title = title
            self.author = author
            self.pages = pages
            self.price = price

    class Magazine:
        def __init__(self, title, publisher, price, period):
            self.title = title
            self.publisher = publisher
            self.price = price
            self.period = period

    class Newspaper:
        def __init__(self, title, publisher, price, period):
            self.title = title
            self.publisher = publisher
            self.price = price
            self.period = period

Do you see lots of duplication in the above class definition?

We can solve this using `inheritance`. First extract, `title` and `price` in a separate class `Publication`.

    class Publication:
        def __init__(self, title, price):
            self.title = title
            self.price = price

With this new class `Publication`, we can now redefine the class `Book` as below

    class Book(Publication):
        def __init__(self, title, author, pages, price):
            super().__init__(title, price)
            self.author = author
            self.pages = pages

Looking back at the definition of class `Magazine` and `Newspaper`, we see another duplication i.e. `publisher` and `period`.

Let's extract that out in a separate class `Periodical` with the help of `Publication` class.

    class Periodical(Publication):
        def __init__(self, title, price, period, publisher):
            super().__init__(title, price)
            self.period = period
            self.publisher = publisher

Now with the help `Periodical` class, we can cleanup the `Magazine` and `Newspaper` class.

    class Magazine(Periodical):
        def __init__(self, title, publisher, price, period):
            super().__init__(title, publisher, price, period)

    class Newspaper(Periodical):
        def __init__(self, title, publisher, price, period):
            super().__init__(title, publisher, price, period)

Use the new refined class definitions like below

    b1 = Book("Learning Perl", "brian d foy", 800, 40)
    n1 = Newspaper("Evening Standard", "Evening Standard Ltd.", 4, "Daily")
    m1 = Magazine("Perl Journal", "TPF", 5, "Monthly")

    print(b1.author)
    print(n1.publisher)
    print(b1.price, m1.price, n1.price)
