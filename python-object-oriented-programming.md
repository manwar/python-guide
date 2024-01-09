## Python Object-Oriented Programming
***
- [Basic Class](#basic-class)
- [Instance Type](#instance-type)
- [Class Method Attribute](#class-method-attribute)
- [Inheritance](#inheritance)
- [Abstract Class](#abstract-class)
- [Multiple Inheritance](#multiple-inheritance)
- [Interface](#interface)
- [Composition](#composition)
- [Magic Methods](#magic-methods)
- [Data Class](#data-class)

**Disclaimer:** These are my notes after attending the course [**Python Object-Oriented Programming**](https://www.linkedin.com/learning/python-object-oriented-programming-22888296)

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

Every class in `Python` is a sub class of generic super class `object`. So this is perfectly OK.

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

## Abstract Class
***

Suppose we have the following class definition

    class GraphicalShape:
        def __init__(self):
            super().__init__()

        def calc_area(self):
            pass

    class Circle(GraphicalShape):
        def __init__(self, radius):
            self.radius = radius

     class Square(GraphicalShape):
        def __init__(self, side):
            self.side = side

Make use of the above classes

    g = GraphicalShape()
    c = Circle(10)
    print(c.calc_area()) # prints None
    s = Square(12)
    print(s.calc_area()) # prints None

Here we want to enforce two things, first stop user to create an instance of class `GraphicalShape` and make sure anyone inheriting `GraphicalShape` must implement `calc_area()`.

We can use the module `abc` and import class `ABC` and `abstractmethod`

Let's change the class `GraphicalShape` definition and make it inherit class `ABC`. Also turn the method `calc_area()` into `abstract method`.

    from abc`import ABC, abstractmethod
    class GraphicalShape(ABC):
        def __init__(self):
            super().__init__()

        @abstractmethod
        def calc_area(self):
            pass

Now run the above code would throw error as you can't instantiate abstract class

    g = GraphicalShape()

Even the following line would throw error as it expects class `Circle` to implement method `calc_area()`

    c = Circle(10)

We can resolve this very easily

    class Circle(GraphicalShape):
        def __init__(self, radius):
            self.radius = radius

        def calc_area(self):
            return 3.14 * (self.radius ** 2)

Similarly we can fix the class `Square`

     class Square(GraphicalShape):
        def __init__(self, side):
            self.side = side

        def calc_area(self):
            return self.side * self.side            

Let's run the same code, you should see the result as below

    c = Circle(10)
    print(c.calc_area()) # prints 314
    s = Square(12)
    print(s.calc_area()) # prints 144

## Multiple Inheritance
***

Assume we have class `A` and `B` defined as below

    class A:
        def __init__(self):
            super().__init__()
            self.prop1 = "prop1"

    class B:
        def __init__(self):
            super().__init__()
            self.prop2 = "prop2"            

Then we have another class `C` which inherits both class `A` and `B` in the order.

    class C(A, B):
        def __init__(self):
            super().__init__()

        def showprops(self):
            print(self.prop1)
            print(self.prop2)

Time for some action now

    c = C()
    c.showprops() # prints "prop1" and "prop2" as expected

So far so good.

What if the super classes share common attributes as below

    class A:
        def __init__(self):
            super().__init__()
            self.prop1 = "prop1"
            self.name = "Class A"

    class B:
        def __init__(self):
            super().__init__()
            self.prop2 = "prop2"
            self.name = "Class B"

Now update the method `showprops()` in the class `C`

    class C(A, B):
        def __init__(self):
            super().__init__()

        def showprops(self):
            print(self.prop1)
            print(self.prop2)
            print(self.name)

What do you expect the following code would print?

    c = C()
    c.showprops()

It would print something like

    prop1
    prop2
    Class A

Do you know why? 

Well the order of inheritance is the key, class `A` is the first in the list and hence the attribute `name` gets printed.

Here `Python` used something called `method resolution order (mro)`.

So it starts with the current class, if not find what they are looking for then jump to the first super class in the list and still can't find then go the next one in the list, so on so forth.

In the above case, the attribute `name` is not defined the current class `C`, so the next step would be look into the first super class in the list i.e. `A` and then `B`.
Since we have attribute `name` defined in the class `A`, the search stops there and we get the result as above.

Let's prove the theory now by changing the order of super class

    class C(B, A):
        def __init__(self):
            super().__init__()

        def showprops(self):
            print(self.prop1)
            print(self.prop2)
            print(self.name)

Execute the code below

    c = C()
    c.showprops()

It would now print something like

    prop1
    prop2
    Class B

If you are interesting in finding the method resolution order, you can do so using the special class attribute `__mro__`

    print(C.__mro__)

You should see something like this:

    (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    
## Interface
***

The interface feature of `OOP` can be implemented using the `Abstract Class` and `Multiple Inheritance` features of the `Python` language as there is no native implementation.

`Interface` is like making a promise to provide certain behaviour.

Let's take a look of the above class definitions

    from abc`import ABC, abstractmethod
    class GraphicalShape(ABC):
        def __init__(self):
            super().__init__()

        @abstractmethod
        def calc_area(self):
            pass

    class Circle(GraphicalShape):
        def __init__(self, radius):
            self.radius = radius

        def calc_area(self):
            return 3.14 * (self.radius ** 2)

     class Square(GraphicalShape):
        def __init__(self, side):
            self.side = side

        def calc_area(self):
            return self.side * self.side  

Suppose we want to have JSONify feature in the `Circle` and `Square` class, we could add that in the base class `GraphicalShape`. 

What if we want the same in other base class?          

We could just create another abstract class `JSONify`

    class JSONify(ABC):
        @abstractmethod
        def toJSON(self):
            pass

Now we can use the abstract class `JSONify` like below

    class Circle(GraphicalShape, JSONify):
        def __init__(self, radius):
            self.radius = radius

        def calc_area(self):
            return 3.14 * (self.radius ** 2)

We would now need to implement the abstract method `toJSON()`

        def toJSON(self):
            return f"{{'Circle': {str(self.calc_area())}}}"

Time for some action

    c = Circle(10)
    print(c.calc_area()) # prints 314
    print(c.toJSON())    # prints {'Circle': 314 }

## Composition
***

We have done `Interface` earlier something like

    Publication -> Book
                -> Periodical -> Magazine

`Composition` is slightly different as below

    Book -> Title
            Price
            Author -> First Name
                      Last Name

Let's re-create class `Book` as below

    class Book:
        def __init__(self, title, price, authorfname, authorlname):
            self.title = title
            self.price = price

            self.authorfname = authorfname
            self.authorlname = authorlname

            self.chapters = []

        def addchapter(self, name, pages):
            self.chapters.append((name, pages))

Use the class now

    b = Book("Perl Hacks", 60, "Damian", "Conway")
    b.addchapter("Chapter 1", 101)
    b.addchapter("Chapter 2", 102)
    b.addchapter("Chapter 3", 103)
    print(b.title)

It would be nice to extract out author information in its own class

    class Author:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname  = lastname

Let's override built-in `str()` function to return the string representation of the object

        def __str__(self):
            return f"{self.firstname} {self.lastname}"

We can now redefine `Book` class to use the `Author` class

    class Book:
        def __init__(self, title, price, author = None):
            self.title  = title
            self.price  = price
            self.author = author

            self.chapters = []

        def addchapter(self, name, pages):
            self.chapters.append((name, pages))

We can now do the same with `Chapter` class

    class Chapter:
        def __init__(self, name, pagecount):
            self.name = name
            self.pagecount = pagecount

Time for another attempt to use `Chapter`

    class Book:
        def __init__(self, title, price, author = None):
            self.title  = title
            self.price  = price
            self.author = author

            self.chapters = []

        def addchapter(self, chapter):
            self.chapters.append(chapter)

Let's add method `getbookpagecount()` to the `Book` class

        def getbookpagecount(self):
            count = 0
            for chapter in self.chapters:
                count += chapter.pagecount
            return count

Finally we can use the new `Book` class like below

    author = Author("Damian", "Conway")
    b = Book("Perl Hacks", 60, author)
    b.addchapter(Chapter("Chapter 1", 101))
    b.addchapter(Chapter("Chapter 2", 102))
    b.addchapter(Chapter("Chapter 3", 103))
    
    print(b.title)
    print(b.author)
    print(b.getbookpagecount())
    
## Magic Methods
***

Let's re-use the `Book` class from earlier chapter

    class Book:
        def __init__(self, title, author, price):
            self.title  = title
            self.author = author
            self.price  = price

Standard use of the class

    b1 = Book("Learning Perl", "brian d foy", 50)
    b2 = Book("Perl Hacks", "Damian Conway", 60)

    print(b1) # prints internal object representation of b1
    print(b2) # prints internal object representation of b2

#### `__str__()`

We can solve the above problem by overriding `__str__()` magic method

        def __str__(self):
            return f"{self.title} by {self.author} costs {self.price}"

Check the reselt now

    print(b1) # prints Learning Perl by brian d foy costs 50
    print(str(b1))  # sames as print(b1)

#### `__repr__()`

We will now another magic method `__repr__()`

        def __repr__(self):
            return f"title={self.title}, author={self.author}, price={self.price}"

Now check how it behaves

    print(repr(b2)) # prints title=Perl Hacks, author=Damian Conway price=60    

#### `__eq__()`

Let us compare two objects of class `Book` with exactly same data.

    b1 = Book("Learning Perl", "brian d foy", 50)
    b2 = Book("Learning Perl", "brian d foy", 50)
    b3 = Book("Perl Hacks", "Damian Conway", 60)

What do you expect this would return?

    print(b1 == b2)

Believe it or not, it would print `False` but why?

Because `Python` doesn't do attribute comparison.

We can solve this issue by overriding magic method `__eq__()` like below

        def __eq__(self, otherobject):
            if not isinstance(otherobject, Book):
                raise ValueError("Can't compare book to non-book.")
                
            return (self.title == otherobject.title and
                    self.author == otherobject.author and
                    self.price == otherobject.price)

Let's do the comparison now

    print(b1 == b2) # prints True
    print(b1 == b3) # prints False
    print(b1 == 12) # throw exception as expected

#### `__ge__()`

We can overried magic method `__ge__()` to test greater than or equal comparison

        def __ge__(self, otherobject):
            if not isinstance(otherobject, Book):
                raise ValueError("Can't compare book to non-book.")
                
            return self.price >= otherobject.price

Test the comparison

    print(b1 >= b2) # prints False
    print(b2 >= b1) # prints True

#### `__gt__()`

We can overried magic method `__gt__()` to test greater than comparison

        def __gt__(self, otherobject):
            if not isinstance(otherobject, Book):
                raise ValueError("Can't compare book to non-book.")
                
            return self.price > otherobject.price

Test the comparison

    print(b1 > b2) # prints False
    print(b2 > b1) # prints True

#### `__le__()`

We can overried magic method `__le__()` to test less than or equal comparison

        def __le__(self, otherobject):
            if not isinstance(otherobject, Book):
                raise ValueError("Can't compare book to non-book.")
                
            return self.price <= otherobject.price

Test the comparison

    print(b1 <= b2) # prints True
    print(b2 <= b1) # prints False

#### `__lt__()`

We can overried magic method `__lt__()` to test less than comparison

        def __lt__(self, otherobject):
            if not isinstance(otherobject, Book):
                raise ValueError("Can't compare book to non-book.")
                
            return self.price < otherobject.price

Test the comparison

    print(b1 < b2) # prints True
    print(b2 < b1) # prints False    

Since we have implemented `__lt__()` magic method, we can now sort the object too from low to high price.

**NOTE:** The built-in `sort()` function uses the magic method `__lt__()` for comparison.

    b1 = Book("Learning Perl", "brian d foy", 50)
    b2 = Book("Perl Hacks", "Damian Conway", 600, 60)
    books = [b2, b1]
    books.sort()
    print([ book.title for book in books ])

#### `__getattribute__()`

It gets called everytime we try to access an object attribute.

    class Book:
        def __init__(self, title, author, price):
            super().__init__()
            self.title  = title
            self.price  = price
            self.author = author
            self._discount = 0.1 # 10% discount

        def __str__(self):
            return f"{self.title} by {self.author} costs {self.price}"

        def __getattribute__(self, name):
            if name == "price":
                p = super().__getattribute__("price")
                d = super().__getattribute__("_discount")
                return p - (p * d)
            return super().__getattribute__(name)

Now test the magic method

    b1 = Book("Learning Perl", "brian d foy", 50)
    print(b1) # prints Learning Perl by brian d foy costs 45

#### `__getattr__()`  

The magic method `__getattr__()` only kicks in when `__getattribute__()` lookup fails.

        def __getattr__(self, name):
            return name + " is not here!"

So this would get caught

    print(b1.unknownprop) # print unknownprop is not here!

#### `__setattr__()`  

 Now we will try to intercept setting attribute action by overriding magic method `__setattr__()`

         def __setattr__(self, name, value):
            if name == "price":
                if type(value) is not float:
                    raise ValueError("The 'price' attribute must be a float.")
            return super().__setattr__(name, value)       

Test the change

    b1.price = 50 # throw exception as the value is not float

We can work around this by cast

    b1.price = float(50) # all good now

#### `__call__()`

The magic method `__call__()` can be used to call the object like a function.

        def __call__(self, title, author, price):
            self.title  = title
            self.author = author
            self.price  = price

Time for some action now

    b1 = Book("Learning Perl", "brian d foy", 50)
    print(b1) # prints Learning Perl by brian d foy costs 50
    b1("Learning Perl", "dummy", 40)
    print(b1) # prints Learning Perl by dummy costs 40

## Data Class
***    

In `Python 3.7`, the data class was introduced to automate the attribute settings. You also get magic method `__eq__()` and `__repr__()` for **FREE**.

    from dataclasses import dataclass

    @dataclass
    class Book:
        title: str
        author: str
        pages: int
        price: float

Test the data class now

    b1 = Book("Learning Perl", "brian d foy", 800, 50.0)
    b2 = Book("Perl Hacks", "Damian Conway", 600, 60.0)  
    b3 = Book("Learning Perl", "brian d foy", 800, 50.0)
    
    print(b1.title)
    print(b2.author)

    print(b1)       # repr() gets used here
    print(b1 == b3) # True
    print(b1 == b2) # False

You can even add regular method to data class

    from dataclasses import dataclass

    @dataclass
    class Book:
        title: str
        author: str
        pages: int
        price: float

        def bookinfo(self):
            return f"{self.title} by {self.author}"

Try the regular method in data class

    b1 = Book("Learning Perl", "brian d foy", 800, 50.0)   
    print(b1.bookinfo()) # prints Learning Perl by brian d foy

You can manage the post initialisation stage by overriding magic method `__post_init__()`

        def __post_init__(self):
            self.description = f"{self.title} by {self.author}, {self.pages} pages"

Magic works eventually

    print(b1.description) # prints Learning Perl by brian d foy, 800

How about setting default values to data class?

    from dataclasses import dataclass

    @dataclass
    class Book:
        title: str = "No Title"
        author: str = "No Author"
        pages: int = 0
        price: float = 0.0

Test the default values

    b = Book()
    print(b) # prints Book(title='No Title', author='No Author', pages=0, price=0.0)

**NOTE:** Non default attributes should come first then default value attribute

So the following definition would throw error

    from dataclasses import dataclass

    @dataclass
    class Book:
        title: str = "No Title"
        author: str = "No Author"
        pages: int = 0
        price: float

You can also use `field()` function to provide default value.

    from dataclasses import dataclass, field

    @dataclass
    class Book:
        title: str = "No Title"
        author: str = "No Author"
        pages: int = 0
        price: float = field(default = 10.0)

Let's checkout the change

    b1 = Book("Learning Perl", "brian d foy", 800)
    b2 = Book("Perl Hacks", "Damian Conway", 600)

    print(b1) # prints Book(title='Learning Perl', author='brian d foy', pages=800, price=10.0)
    print(b2) # prints Book(title='Perl Hacks', author='Damian Conway', pages=600, price=10.0)

You can use function for default value too.

    from dataclasses import dataclass, field
    import random

    def price_func():
        return float(random.randrange(20, 30))

    @dataclass
    class Book:
        title: str = "No Title"
        author: str = "No Author"
        pages: int = 0
        price: float = field(default_factory=price_func)

Test the random default using function

    b1 = Book("Learning Perl", "brian d foy", 800)
    b2 = Book("Perl Hacks", "Damian Conway", 600)

    print(b1) # prints Book(title='Learning Perl', author='brian d foy', pages=800, price=21.0)
    print(b2) # prints Book(title='Perl Hacks', author='Damian Conway', pages=600, price=28.0)    

#### Immutable Data Class

    from dataclasses import dataclass

    @dataclass(Frozen = True)
    class ImmutableClass:
        value1: str = "Value 1"
        value2: int = 0

Test the immutable data class

    c = ImmutableClass()
    print(c.value1, c.value2)
    c.value1 = "Another value" # throw error

Even function wouldn't allow change as below

    from dataclasses import dataclass

    @dataclass(Frozen = True)
    class ImmutableClass:
        value1: str = "Value 1"
        value2: int = 0

        def some_func(self, newval):
            self.value2 = newval

Try this, you should see error

    c = ImmutableClass()
    c.some_func(10)

You must note, object creation stage you can set any value you like

    c = ImmutableClass("New Val", 10)
    print(c.value1, c.value2)   # prints New Val 10
    c.some_func(10)             # this still throws error
