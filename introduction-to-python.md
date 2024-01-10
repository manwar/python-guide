## Introduction to Python
***
- [Hello World](#hello-world)
- [Variable](#variable)
- [DataTypes](#datatypes)
- [Functions](#functions)
- [Module](#module)
- [Conditions](#conditions)
- [Loops](#loops)
- [Recursion](#recursion)
- [Class](#class)
- [Exception](#exception)
- [File Management](#file-management)
- [Date](#date)
- [Calendar](#calendar)
- [Data Formats](#data-formats)
- [Web Framework](#web-framework)

**Disclaimer:** These are my notes after attending the courses [[**Python Quick Start**](https://www.linkedin.com/learning/python-quick-start-22667553)], [[**Learning Python**](https://www.linkedin.com/learning/learning-python-14393370)] and [[**8 Things You Must Know in Python**](https://www.linkedin.com/learning/8-things-you-must-know-in-python)].

## Hello World
***
    print('Hello World !!')

Let's try special `f''` function

    name = 'World'
    print(f'Hello {name} !!')  # prints Hello World !!

Or something like this

    hello = 'Hello {} !!'
    print(hello.format(name))  # prints Hello World !!

Even you can do something like below

    print('Hi {0} {1} !!'.format('Joe', 'Blog'))    # prints Hi Joe Blog !!

#### String Template

We can use `Template` class from the `string` module.

    from string import Template
    templ = Template("You are reading ${book} by ${author}.")
    s = templ.substitute(book="Perl Hacks", author="Damian Conway")

    print(s)    # prints You are reading Perl Hacks by Damian Conway.

There is an alternative, we can use dictionary too like below

    data = {
        "book": "Perl Hacks",
        "author": "Damian Conway"
    }
    s1 = templ.substitute(data)

    print(s1)   # prints You are reading Perl Hacks by Damian Conway.
    
Look up environment name

    import os
    print(os.environ.get("ENV_NAME")) # prints value of environment name "ENV_NAME".

    $ export ENV_NAME="local"    

    print(os.environ.get("ENV_NAME")) # prints local

#### Comments

For single line comment, you can use `#` same as in `Perl`

For multilines comment, you have to use `'''` i.e. 3 single quotes in the beginning and in the end.

## Variable
***

Variable declaration

    name = "Joe"
    age = 20

or you can combined both in one line as below

    name, age = "Joe", 20

Global/Local variable

    # Global variable
    name = "Joe"

    def showName():
        # Local variable
        name = "Blog"
        print(name)

    showName()   # prints Blog
    print(name)  # prints Joe

Override global variable inside the function

    # Global variable
    name = "Joe"

    def showName():
        # Override global variable
        global name
        name = "Blog"
        print(name)

    showName()   # prints Blog
    print(name)  # prints Blog

You can even undefine a variable

    name = "Joe"
    print(name) # prints Joe
    del name
    print(name) # throw error
    
## DataTypes
***

1) Boolean defined with keyword `bool` and can only have value `True`/`False`
2) Integer defined with keyword `int`
3) Floating defined with keyword `float`
4) String defined with keyword `str`

String contains unicode whereas Byte is raw 8-bits values

    s = "Hi there!"
    b = bytes([0x41, 0x42, 0x43])

    print(s)  # prints Hi there!
    print(b)  # prints b'ABC'

We can't combine string and byte using `+` operator.

    print(s+b)     # would throw error as print() expects string and not byte

To solve the issue, we have to decode the bytes using `'utf-8'` encoding like below:

    s1 = b.decode('utf-8')
    print(s+s1)    # prints Hi there!ABC

Or we could encode the string using '`utf-8'` encoding and concatenate like this:

    b1 = s.encode('utf-8')
    print(b1+b)    # prints b'Hi there!ABC'

What if encode the string using `'utf-32'` encoding?

    b2 = s.encode('utf-32')
    print(b2)      # prints lots of hexadecimal numbers representing the string.

**NOTE**: String and Byte are not the same.

List: Square bracket `[]` can be used to create a list

    list = [2, 4, 6, 8, 10]
    print(list[2]) # prints 6

    list[2] = 60
    print(list[2]) # prints 60

Slice a list using syntax `list[startindex: endindex: step]`.

Default `startindex` is `0` and default `step` is `1`.

    print(list[1:3])   # prints [4, 6]
    print(list[0:5,2]) # prints [2, 6, 10]

Reverse a given list using the slice syntax.

    print(list[::-1])  # prints [10, 8, 6, 4, 2]

#### Elements in a list can be changed. Also elements do not have to be of one type. You can have elements of different data types.

    list = ["Adam", 50, True, 1.5]
  
**Tuples**: Braces `()` can be used to create `Tuple`. Elements in tuple **CAN NOT** be changed unlike `List`.

    child = ("Joe", "male", 2, "UK")
    print(child[0]) # prints child name

    tyoe(child) # prints tuple

**Dictionary** is a key-value list, just like `hash` in **Perl**.

    users = { "name": "Joe", "age": 20 }
    print(users["name"]) # prints Joe
    print(users["age"])  # prints 20
    
Built-in function `type()` can be used to identify the data type.

## Functions
***

User can define function using the keyword `def` as below:

    def addFive(n): -> int
        return n + 5

    result = addFive(10)
    print(result)  # prints 15
    print(addFive) # prints object name assgined to the function addFive()

How about function with default value?

    def power(n, x = 1):
        result = 1
        for i in range(x):
            result = result * n

        return result

    print(power(2))     # prints 2
    print(power(2, 3))  # prints 8

Function can be called with named parameters in any order.

    print(power(x = 3, n = 2)) # prints 8

Function with variable number of parameters.

    def addAll(*args):
        result = 0
        for i in args:
            result = result + i
        return result

    print(addAll(1,2,3))    # prints 6
    print(addAll(1,2,3,4))  # prints 10
    
#### Built-in functions in Python

You can get the complete list [**here**](https://docs.python.org/3/library/functions.html).

    a) print("") 
    b) input("") returns string typed user data.
    c) int() returns integer value of the input data.
    d) str() returns string value of the input data.
    e) + operator can be used for string concatenation e.g. print("Hello " + name)

Let's try some most useful built-in functions

#### all(iterable)

An `iterable` is anything you can loop over using a `for` loop. For example, `lists`, `tuples`, `strings`, `sets` and `dictionaries`.

    def valid_rgb(rgb): -> bool
        for v in rgb:
            if not 0 <= v <= 255:
                return False
            return True

The above function can be re-written with the help of `all()` as below:

    def valid_rgb(rgb): -> bool
        return all(0 <= v <= 255
            for v in rgb)

The syntax for `all()` can take the form below, it expects every condition to be true.

    all(
        condition(item)
        for item in iterable
    )

#### any(iterable)

Similar to `all()`, but it expects atleast one condition to be true.

    def contains_digit(n):
        for c in n:
            if c.isdigit():
                return True
        return False

Now using the `any()` function, we can do something like below:

    def contains_digit(n):
        return any(c.isdigit()
            for c in n)

#### enumerate(iterable)

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    for i in range(len(countries)):
        print(f"{i+1}. {countries[i]}")

You should see something like this:

    1. Netherlands
    2. Nigeria
    3. Jordan
    4. Nepal
    5. Niger
    6. Japan
    
The above can be re-written using `enumerate()`.

    for i in enumerate(countries, start=1):
        print(i)

Similar output but not exactly.

    (1, 'Netherlands')
    (2, 'Nigeria')
    (3, 'Jordan')
    (4, 'Nepal')
    (5, 'Niger')
    (6, 'Japan')

Let's get it print the result how we wanted.

    for i, c in enumerate(countries, start=1):
        print(f"{i}. {c}")

Much cleaner and get the desired result.

    1. Netherlands
    2. Nigeria
    3. Jordan
    4. Nepal
    5. Niger
    6. Japan

For simple use case:

    for c in countries:
        print(c)

We get this:

    Netherlands
    Nigeria
    Jordan
    Nepal
    Niger
    Japan

#### zip(*iterables)

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']

    for country, capital in zip(countries, capitals):
        print(f'The capital city of {country} is {capital}.')

Here is the output of the above code.

    The capital city of Netherlands is Amsterdam.
    The capital city of Nigeria is Abuja.
    The capital city of Jordan is Amman.
    The capital city of Nepal is Kathmandu.
    The capital city of Niger is Niamey.
    The capital city of Japan is Tokyo.

If both lists has the same number of elements then you get the above result.

However what if one has less elements than the other?

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu']

    for country, capital in zip(countries, capitals):
        print(f'The capital city of {country} is {capital}.')
        
You only see the result for elements in the smaller list as below:

    The capital city of Netherlands is Amsterdam.
    The capital city of Nigeria is Abuja.
    The capital city of Jordan is Amman.
    The capital city of Nepal is Kathmandu.

What if we wanted the entire list? 

We could import `zip_longest` from `itertools` module to handle the missing entries.

    from iterutils import zip_longest
    
    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu']

    for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):
        print(f'The capital city of {country} is {capital}.')

We now have missing entries listed too.

    The capital city of Netherlands is Amsterdam.
    The capital city of Nigeria is Abuja.
    The capital city of Jordan is Amman.
    The capital city of Nepal is Kathmandu.
    The capital city of Niger is Unknown.
    The capital city of Japan is Unknown.

There is no `unzip()` function in `Python`.

Why? Because we don't need it as shown below:

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']
    pairs = list(zip(countries, capitals))

    countries, capitals = zip(*pairs)
    print(countries)  # ('Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan')
    print(capitals)   # ('Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo')
    
#### reversed(sequence)    

`Sequence` is a subset of iterables that have `a length`, `an index` and `can be sliced`. 

For example, `strings`, `lists` and `tuples` are `sequences`.

Example of iterables that are not sequences are `dictionaries`, `files`, `sets` and `generators`.

The `reverse()` function reverses a sequence in-place.

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    countries.reverse()
    print(countries) # ('Japan', 'Niger', 'Nepal', 'Jordan', 'Nigeria', 'Netherlands')

`Slicing` creates a reversed copy of a sequence as shown below

    print(counties[::-1]) # ('Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan')

You must be aware that `slicing` takes lot of memory as compare to `reverse()` function.

The `reversed()` function returns an iterator.

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    for country in reversed(countries):
        print(country)

Here is the output:

    Japan
    Niger
    Nepal
    Jordan
    Nigeria
    Netherlands

In a nutshell, there are three ways to reverse a sequence:

    a) reverse()
        - Reverse a mutable sequence in-place
        - Not avaialbe for immutable sequences
    
    b) slicing[::-1]
        - Creates a reversed copy of a sequence
        - Fastest but makes a copy of the sequence
        - Memory considerations to reverse millions of items?
        - Used for both mutable and immutable sequences

    c) reversed()
        - Returns a reverse iterator
        - Scales well to millions of items
        - Used for both mutable and immutable sequences

#### min() / max()

    countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
    populations = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

    max(population) # 190000000
    min(countries)  # Japan (alphabetically smalles)

Suppose we want to find out the country with the smallest population.

First create tuple by zipping `countries` and `populations`.

    print(list(zip(countries, populations))  

You should get something like this:

    [('Netherlands', 17500000), ('Nigeria', 190000000), ('Jordan', 10000000), ('Nepal', 30000000), ('Niger', 24000000), ('Japan', 128000000)]

Now try `min()` to the tuples as below:

    print(min(zip(countries, populations))) # ('Japan', 128000000)

We can even provide function to the `min()` function like below:

    def get_population(pair):
        country, population = pair
        return population

    print(min(zip(countries, populations), key=get_population)) # ('Jordan', 100000000)
    
We can solve the same problem with the help of `lambda` function.

    print(min(zip(countries, populations), key=lambda x: x[1])) # ('Jordan', 100000000)

Here is another cheat solution by changing the order of zip, in this case we don't need anything else.

    print(min(zip(populations, countries))) # ('Jordan', 100000000)

#### sorted(iterable, *, key=None, reverse=False)

    class Country:
        def __init__(self, name, population):
            self.name = name
            self.population = population
        def __repr__(self):
            return f'Country {self.name}, {self.population}'

    country_list = [
        Country('Taiwan', 24_000_000),
        Country('Portugal', 10_000_000),
        Country('Netherlands', 17_500_000),
        Country('Nigeria', 198_000_000),
        Country('Jordan', 10_000_000),
        Country('Nepal', 30_000_000),
        Country('Niger', 24_000_000),
        Country('Japan', 128_000_000)
    ]

Sort the country by population.

    sorted(country_list, key=lambda x: x.population)

Then you get the following:

    [Country('Portugal', 10_000_000), Country('Jordan', 10_000_000), Country('Netherlands', 17_500_000), Country('Taiwan', 24_000_000), Country('Niger', 24_000_000), Country('Nepal', 30_000_000), Country('Japan', 128_000_000), Country('Nigeria', 198_000_000)]

If you want to reverse the sort order.

    sorted(country_list, key=lambda x: x.population, reverse=True)

Sort order is reversed now as you see below:

    [Country('Nigeria', 198_000_000), Country('Japan', 128_000_000), Country('Nepal', 30_000_000), Country('Taiwan', 24_000_000), Country('Niger', 24_000_000),  Country('Netherlands', 17_500_000), Country('Portugal', 10_000_000), Country('Jordan', 10_000_000)]

We can get the same result doing this:

    sorted(country_list, key=lambda x: -x.population)

Reverse order as before.

    [Country('Nigeria', 198_000_000), Country('Japan', 128_000_000), Country('Nepal', 30_000_000), Country('Taiwan', 24_000_000), Country('Niger', 24_000_000),  Country('Netherlands', 17_500_000), Country('Portugal', 10_000_000), Country('Jordan', 10_000_000)]

If you noticed, `Taiwan` and `Niger` both have the populations `24_000_000` but `Taiwan` appears before `Niger`. 

In theory `Niger` should come first.

Let's sort in decreasing order of population and increasing name alphabetically.

    sorted(country_list, key=lambda x: (-x.population, x.name))

Here is what we get.

    [Country('Nigeria', 198_000_000), Country('Japan', 128_000_000), Country('Nepal', 30_000_000), Country('Niger', 24_000_000), Country('Taiwan', 24_000_000), Country('Netherlands', 17_500_000), Country('Jordan', 10_000_000), Country('Portugal', 10_000_000)]

What if we want to sort reverse by name too? 

Well you can't do `-x.name`, instead you would need to do like below:

    print(sorted(country_list, key=lambda x: (x.population, x.name), reverse=True))

Now if you want to sort on a field that has alphnumeric characters, something like below:

    iso = [('Taiwan', 'iso24000000'), ('Portual', 'iso10000000'), ('Netherlands', 'iso17500000'), ('Nigeria', 'iso198000000'), ('Jordan', 'iso100000    00'), ('Nepal', 'iso30000000'), ('Niger', 'iso24000000'), ('Japan', 'iso128000000')]

As you see the population has the three letters code `iso` at the start.

    def get_population(pair):
        country, population = pair
        return population[3:] # ignore the first three letters i.e. iso
 
     print(sorted(iso, key=get_population))

Below is what we get back:

    [('Portual', 'iso10000000'), ('Jordan', 'iso10000000'), ('Japan', 'iso128000000'), ('Netherlands', 'iso17500000'), ('Nigeria', 'iso198000000')    , ('Taiwan',         'iso24000000'), ('Niger', 'iso24000000'), ('Nepal', 'iso30000000')]

Did you notice it didn't do as expected? 

`Japan` comes before `Netherlands` since sorting done alphabetically `128_000_000` appears before `17_000_000`.    

We can handle this issue very easily using type cast.

    def get_population1(pair):
        country, population = pair
        return int(population[3:]) # ignore the first three letters i.e. iso
 
     print(sorted(iso, key=get_population1))

Finally we have done it correctly.

    [('Portual', 'iso10000000'), ('Jordan', 'iso10000000'), ('Netherlands', 'iso17500000'), ('Taiwan', 'iso24000000'), ('Niger', 'iso24000000'), (    'Nepal', 'iso30000000'), ('Japan', 'iso128000000'), ('Nigeria', 'iso198000000')]

#### iter()

You can use `iter()` function to generator iterator from a list.

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    i = iter(days)

Then we use the iterator `i` and print the next element until the last element in the list.

    print(next(i))  # prints Sun
    print(next(i))  # prints Mon
    print(next(i))  # prints Tue

You can use iterator to read each line in a file.

Suppose we have a text file `sample.txt` containing the following lines.

    This is line 1.
    This is line 2.
    This is line 3.
    This is line 4.
    This is line 5.

Let's use the `iter()` function to read each line of the above file.

    with open("sample.txt", "r") as fp:
        for line in iter(fp.readline(), ''):
            print(line)

The above code would dump this on the console.

    This is line 1.
    This is line 2.
    This is line 3.
    This is line 4.
    This is line 5.

The function call `iter(fp.readline(), '')` mean iterator would stop when the `fp.readline()` returns an empty string as the second paramter indicates to the `iter()` function.

#### filter()

The `filter()` can be used to filter a given sequence.

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Suppose we want to filter all odd numbers in the list.

    def is_even(n):
        if n % 2 == 0:
            return True
        return False

    print(list(filter(is_even, nums)))   # prints [2, 4, 6, 8, 10]

Similarly, if we have string as below:

    s = "abcDefGHIjk"

Let's filter out characters in lower case.

    def is_upper(c):
        if c.isupper():
            return True
        return False

    print(list(filter(is_upper, s)))     # prints ['D', 'G', 'H', 'I']


#### map()

The `map()` function creates a new list given one or more sequences.

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Let's create a new list of square numbers of each element in the given list.

    def squares(n):
        return n**2

    print(list(map(squares, nums)))    # prints [1, 4, 9, 16, 25, 36, 49, 64, 81. 100]
    
Try one more example as below:

    scores = [89, 75, 94,61, 82]

    def grades(n):
        if n >= 90:
            return "A"
        elif (n >= 80 and n < 90):
            return "B"
        elif (n >= 70 and n < 80):
            return "C"
        elif (n >= 60 and n < 70):
            return "D"
        else:
            return "E"

    print(list(map(grades, sorted(scores))))  # prints ['D', 'C', 'B', 'B', 'A']

## Module
***

Most commonly used modules in **Python** are `calendar`, `math`, `random`.

The following line returns calendar for the month `Jan 2024`.

      cal = calendar.month(2024, 1)

Square root of a given number and returns result in floating number.

      result = math.sqrt(49) # 7.0

Returns random number between `1` and `10` both inclusive.
      
      rand = random.randint(1, 10)

Picks random entry from the given sequence.
      
      alpha = [ "a", "b", "c", "d" ]
      rand = random.choice(alpha)

Shuffles the given list.
      
      random.shuffle(alpha)

## Conditions
***

    age = 10
    if age > 5:
        print("age is more than 5.")
     elif age == 5:
        print("age is 5")
     else:
        print("age is less than 5.")

Compact `if-else` condition.

    x, y = 1, 2
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than or equal to y")

The above condition can also be done in one line.

    print("x is less than y") if x < y else print("x is greater or equal to y")

For `Python 3.10` or above, we can use the following construct.

    value = "one"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1

    print(result)


Conditions can be comnined using the keyword `"and"`.

## Loops
***

Count vowels in a word

      count = 0
      word = "goodie"
      vowels = ["a", "e", "i", "o", "u"]
      for character in word:
          if character in vowels:
              count += 1

      print(count)
  
Built-in function `range(start, stop, step)` can also be used in `For` loop.

Default `start` is `0` and `step` is `1`. The `stop` is **NOT** inclusive.

The following would print `0,1,2,3`.

      for i in range(4):
          print(i)

The following would print `1,3,5,7`.

      for i in range(1,8,2):
          print(i)

Print each element in the list.

      vowels = ["a", "e", "i", "o", "u"]
      for v in vowels:
          print(v)

Same with While loop.

      vowels = ["a", "e", "i", "o", "u"]
      i = 0
      while i < len(vowels):
          print(vowels[i])
          i += 1

Use of `break` in loop structure.

    for i in range(5, 10):
        if i == 7:
            break
        print(i)

The above code prints only `5,6` as when it reached `7` the loop terminates.

Use of `continue` in loop.

    for i in range(5, 10):
        if i % 2 == 0:
            continue
        print(i)

The above code skips even number and only prints odd number between 5 and 10 i.e. `5, 7, 9`.

Enumerate a list in loop as below:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumarate(days):
        print(i, d)

The code would print like below:

    0 Mon
    1 Tue
    2 Wed
    3 Thu
    4 Fri
    5 Sat
    6 Sun

## Recursion
***

#### a) Factorial using the formula `n! = n * (n-1)!`

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

#### b) Summing digits of number

    Sum of digits = 1st digit + 2nd digit + ... + second to last digit + last digit
                    or 
                    sum of digits before last digit + last digit

Define a function `sumDigits()` as below to return the sum of digits.

    def sumDigits(n):
        if n < 10:
            return n
        else:
            all_but_last = n // 10
            last = n % 10
            return sumDigits(all_but_last) + last

#### c) nth Fibonacci number

    def fib(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            fib(n-1) + fib(n-2)

#### d) Check Palindrome

    def palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and palindrome(s[1:-1])

    def isPalindrome(s):
        temp = s.lower()
        newstr = ""
        for c in temp:
            if c.isalnum():
                newstr += c

        reversestr = ""
        strindx = len(newstr) - 1
        while (strindx > 0):
            reversestr += newstr[strindx]
            strindx -= 1

        if newstr == reversestr:
            return True
        return False

## Class
***

    class Vehicle():
          def __init__(self, bodyStyle):
              self.bodystyle = bodyStyle

          def drive(self, speed):
              self.mode = "driving"
              self.speed = speed

    class Car(Vehicle):
          def __init__(self, engineType):
              super().__init__("Car")
              self.wheels = 4
              self.doors = 4
              self.enginetype = engineType

          def drive(self, speed):
              super().drive(speed)
              print("Driving my", self.enginetype, "car at", self.speed)

    class Motorcycle(Vehicle):
          def __init__(self, engineType, hasSideCar):
              super().__init__("Motorvehicle")
              if (hasSideCar):
                  self.wheels = 3
              else:
                  self.wheels = 2
              self.doors = 0
              self.enginetype = engineType

          def drive(self, speed):
              super().drive(speed)
              print("Driving my", self.enginetype, "motorcycle at", self.speed)

    car1 = Car("gas")
    car2 = Car("electric")
    mc1 = Motorcycle("gas", True)

    print(mc1.wheels)
    print(car1.enginetype)
    print(car2.doors)

    car1.drive(30)
    car2.drive(40)
    mc1.drive(50)

## Exception
***

Exception is handle using `try` block.

    try:
        answer = prompt("What should I divide 10 by?")
        num = int(answer)
        print(10/num)
    except ZeroDivisionError as e:
        print("You can't devide by 0")
    except ValueError as e:
        print("You didn't give me a valid number!")
        print(e)
    finally:
        print("This code always runs")

## File Management
***

Open file for writing and create it if doesn't exist.

    myfile = open("test.txt", "w+")
    for i in range(10):
        myfile.write("This is demo line.\n")
    myfile.close()

Open file and append new text at the end.

    myfile = open("test.txt", "a+")
    for i in range(10):
        myfile.write("This is additional demo line.\n")
    myfile.close()

Read the file contents. You do **NOT** need to close the file.

    myfile = open("test.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read() # read the entire contents in one go
        print(contents)

Read file contents line by line.

    myfile = open("test.txt", "r")
    if myfile.mode == 'r':
        lines = myfile.readlines()
        for line in lines:
            print(line)

If you want to play with csv file then you would need to import `csv` module. 

We are also using `pprint` module for pretty print data structure.

    import csv
    from pprint import pprint

    # Suppose we have csv file sample.csv containing data like this:
    # firstname,surname,age,sex,location
    # Joe,Blogg,20,"m","Lodon"
    # Christie,Slate,18,"f","Dublin"

    with open("sample.csv", "r") as f:
        reader = csv.DictReader(f)
        lines = list(reader)
        for line in lines:
            if line["surname"] == "Blogg":
                pprint(line)
                break

You should see something like this:

    {'age': '20',
     'firstname': 'Joe',
     'location': 'London',
     'sex': 'm',
     'surname': 'Blogg'}

And if you want to play with `JSON` then there is a `json` module.

To convert a `dictionary` into `JSON` we could do something like below to the above code

    import json
    json_line = json.dumps(line)

Then back to `dictionary`

    dict_line = json.loads(json_line)

Now if we want to read `sample.csv` file and create a new `sample.json` file.

    import csv
    import json

    # Suppose we have csv file sample.csv containing data like this:
    # firstname,surname,age,sex,location
    # Joe,Blogg,20,"m","Lodon"
    # Christie,Slate,18,"f","Dublin"

    with open("sample.csv", "r") as f:
        reader = csv.DictReader(f)
        lines = list(reader)

    with open("sample.json", "w") as f:
        json.dump(lines, f, indent=2)

**NOTE**: Here we have used `json.dump()` and not `json.dumps()`.

There is also a very handy `requests` module for pulling data from web. 

You can install the module if missing using the command `pip install requests` or `python3 -m pip install requests`.

    import requests
    response = requests.get("http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?perpage=5000&format=json")

    last_twenty_years = response.json()[1][:20]
    for year in last_twenty_years:
        display_width = year["value"] // 10_000_000
        print(f'{year["date"]}: {year["value"]}', "=" * display_width)


Find OS name.

    import os

    print(os.name)

Check if file exists, we can import `path` class from the module `os`.

    import os
    from os import path

    print("Item exists:", str(path.exists("test.txt")))
    print("Item is a file:", str(path.isfile("test.txt")))
    print("Item is a directory:", str(path.isdir("test.txt")))
    print("Item's file path:", str(path.realpath("test.txt")))
    print("Item's directory and filename:", str(path.split(path.realpath("test.txt"))))

Last modification time

    import os
    from os import path
    import time
    import datetime
    from datetime import date, time, timedelta

    print(time.ctime(path.getmtime("test.txt")))
    print(datetime.datetime.fromtimestamp(path.getmtime("test.txt")))

How long ago the file was modified?

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("test.txt"))
    print("It has been", td, "since the file was modified.")
    print("Or,", td.total_seconds(), "seconds.")

Using filesystem shell methods.

    import os
    from os import path
    import shutil
    from shutil import make_archive

    if path.exists("test.txt"):
        src = path.realpath("test.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)

        os.rename("test.txt", "newtest.txt")

#### Archive folder

    import os
    from os import path
    import shutil
    from shutil import make_archive
    from zipfile import ZipFile

    if path.exists("test.txt.bak"):
        src = path.realpath("test.txt.bak")
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("test.zip", "w") as newzip:
            newzip.write("newtest.txt")
            newzip.write("test.txt.bak")

#### File info

    import os

    def file_info():
        totalbytes = 0
        folder = "deps"
        dirlist = os.listdir(folder)
        for entry in dirlist:
            if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"):
                filesize = os.path.getsize(folder + "/" + entry)
                totalbytes += filesize
        return totalbytes

## Date
***

    # Import class date, time and datetime from the module datetime
    from datetime import date
    from datetime import time
    from datetime import datetime

    today = date.today()
    print("Today's date is", today)
    print("Date components:", today.day, today.month, today.year)
    print("Today's weekday # is", today.weekday())

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Which is a", days[today.weekday()])

    now = datetime.now()
    print("The current date and time is", now)

    t = datetime.time(now)
    print("The current time is", t)

#### Format datetime

     1) %y / %Y Year
     2) %a / %A Weekday
     3) %b / %B Month
     4) %d day of month
     5) %c Locale's date and time
     6) %x Locale's date
     7) %X Locale's time
     8) %I / %H 12/24 Hour
     9) %M Minute
    10) %S Second
    11) %p Locale's AM/PM

Let's use it in the following examples:

    from datetime import datetime

    now = datetime.now()
        
    print(now.strftime("The current year: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    print(now.strftime("Local's date and time: %c"))
    print(now.strftime("Local's date: %x"))
    print(now.strftime("Local's time: %X"))

    print(now.strftime("Current time is %I:%M:%S %p"))
    print(now.strftime("24-hour time is %H:%M:%S %p"))

#### Timedelta

    from datetime import datetime
    from datetime import timedelta

    print(timedelta(days = 365, hours=5, minutes=2))

    now = datetime.now()
    print("Today is", now)
    print("One year from now it will be", str(now + timedelta(days=365)))
    print("In 2 weeks and 3 days from now it will be", str(now + timedelta(weeks=2, days=3)))

    t = now - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %y")
    print("One week ago it was", s)

    # How many days until next April Fools Day
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April Fools day already went by:", ((today-afd).days))
        afd = afd.replace(year = today.year + 1)

    time_to_afd = afd - today
    print("It is", time_to_afd.days, "days unitl the next April Fools Day")

## Calendar
***

    import calendar

    # Calendar week starts with Sunday        
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2024, 1, 0, 0)
    print(str)

    # Calendar week starts with Monday        
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(2024, 1, 0, 0)
    print(str)

    c = calendar.HTMLCalendar(calendar.SUNDAY)
    str = c.formatmonth(2024, 1, 0, 0)
    print(str)

    # Loop over days of a month
    for i in c.itermonthdays(2024,1):
        print(i)

    for name in calendar.month_name:
        print(name)

    for day in calendar.day_name:
        print(day)

First Friday of each month:

    for m in range(1, 13):
        cal = calendar.monthcalendar(2024, m)
        weekone = cal[0]
        weektwo = cal[1]
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print(calendar.month_name[m], meetday)

Count the given day in month year

    import calendar

    def count_days(year, month, whichday):
        # returns an array of weeklist
        # [
        #    [0,0,1,1,1,1,1],
        #    [1,1,1,1,1,1,1],
        #    [1,1,1,1,1,1,1],
        #    [1,1,1,1,1,0,0],            
        # ]
        m = calendar.monthcalendar(year,month)
        d = sum(1 for x in m if x[whichday] != 0)
        return d

## Data Formats
***

    import urllib.request

    weburl = urllib.request.urlopen("http://www.google.com")
    print("Result code:", weburl.getcode())

    data = weburl.read()
    print(data)

#### JSON 

    import urllib.request
    import json

    def printresults(data):
        thejson = json.loads(data)
        if "title" in thejson["metadata"]:
            print(thejson["metadata"]["title"])
        
        count = thejson["metadata"]["count"]
        print(count, "events recorded")

        for i in thejson["features"]:
            print(i["properties"]["place"])
        print("--------\n")

        for i in thejson["features"]:
            if i["properties"]["mag"] > 4.0:
                print(i["properties"]["place"])
        print("--------\n")

        print("Events that were felt:")
        for i in thejson["features"]:
            feltreports = i["properties"]["felt"]
            if feltreports != None:
                if feltreports > 0:
                    print(i["properties"]["place"], feltreports, "times")
        print("--------\n")

    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(urldata)
    print("Result code:", str(weburl.getcode())
    if weburl.getcode() == 200:
        data = weburl.read()
        printresults(data)
    else:
        print("Error received", weburl.getcode())

#### HTML

Let's we have `sample.html` like below:

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>sample HTML Document</title>
        </head>
        <body>
            <!-- This is a comment -->
            <h1>HTML Sample File</h1>
            <p>This is some text</p>
            <p><a href="/hello">Hello</a></p>
        </body>
    </html>

Create subclass `myHTMLParser` like below:

    from html.parser import HTMLParser

    paragraphs = 0
    
    class myHTMLParser(HTMLParser):
        def handle_comment(self, data):
            print("Encountered a comment:", data)
            pos = self.getpos()
            print("At line:", pos[0], " position", pos[1])

        def handle_starttag(self, tag, attrs):
            print("Encountered a start tag:", tag)
            pos = self.getpos()
            print("At line:", pos[0], " position", pos[1])

            global paragraphs
            if tag == "p":
                paragraphs += 1

            if len(attrs) > 0:
                print("Attributes:")
                for a in attrs:
                    print("\t",a[0],"=",a[1])

        def handle_data(self, data):
            if data.isspace():
                return
            print("Encountered a text data:", data)
            pos = self.getpos()
            print("At line:", pos[0], " position", pos[1])

Use `myHTMLParser` class to parse the html data.

    parser = myHTMLParser()
    f = open("sample.html")
    if f.mode == "r":
        contents = f.read()
        parser.feeds(contents)
        
    print("Paragraph tags:", paragraphs)

#### XML

Suppose we have `sample.xml` as below:

    <?xml version = "1.0" encoding="UTF-8" ?>
    <person>
        <firstname>Joe</firstname>
        <lastname>Blog</lastname>
        <home>London</home>
        <skill name="Perl"/>
        <skill name="Python"/>
        <skill name="Raku"/>
    </person>

 See how we can read/write the xml file.
 
    import xml.dom.minidom

    doc = xml.dom.minidom.parse("sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsbyTagName("skill")
    print(skills.length, " skills are listed")
    for skill in skills:
        print(skill.getAttribute("name"))

    newskill = doc.createElement("skill")
    newskill.setAttribute("name", "SQL")
    doc.firstChild.appendChild(newskill)

    skills = doc.getElementsbyTagName("skill")
    for skill in skills:
        print(skill.getAttribute("name"))

## Web Framework
***

Let's play with Python's web framework `Flask`.

You can install the framework using command `pip install Flask`.

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"
    
    app.run(debug=True)

Now we will extend the web application to dump the data from sample file used above.

    from flask import Flask, render_template, jsonify

    app = Flask(__name__)

    with open("sample.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lines = list(reader)

    @app.route("/")
    def index():
        return render_template("index.html") # template/index.html

    @app.route("/users/")
    def users():
        return jsonify(lines)

    @app.route("/users/")
    def user_list():
        results = []
        if not request.args.get("surname"):
            return jsonify(results)
        
        search_string = request.args.get("surname").lower().strip()

        for line in lines:
            if search_string in lines["surname"].lower():
                results.append(line)

        return jsonify(results)
                
    app.run(debug=True)
