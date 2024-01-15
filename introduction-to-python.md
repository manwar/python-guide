## Introduction to Python
***
- [Hello World](#hello-world)
- [Variables](#variables)
- [DataTypes](#datatypes)
- [Functions](#functions)
- [Modules](#modules)
- [Conditions](#conditions)
- [Loops](#loops)
- [Recursion](#recursion)
- [Class](#class)
- [Exception](#exception)
- [Logging](#logging)
- [Comprehensions](#comprehensions)
- [File Management](#file-management)
- [Date](#date)
- [Calendar](#calendar)
- [Data Formats](#data-formats)
- [Web Framework](#web-framework)

**Disclaimer:** These are my notes after attending the courses [[**Python Quick Start**](https://www.linkedin.com/learning/python-quick-start-22667553)], [[**Learning Python**](https://www.linkedin.com/learning/learning-python-14393370)], [[**Advanced Python**](https://www.linkedin.com/learning/advanced-python)] and [[**8 Things You Must Know in Python**](https://www.linkedin.com/learning/8-things-you-must-know-in-python)].

## Hello World
***
    print('Hello World !!')

Let's try special `f''` function.

    name = 'World'
    print(f'Hello {name} !!')  # prints Hello World !!

Or something like this:

    hello = 'Hello {} !!'
    print(hello.format(name))  # prints Hello World !!

Even you can do something like below:

    print('Hi {0} {1} !!'.format('Joe', 'Blog'))    # prints Hi Joe Blog !!

#### String Template

We can use `Template` class from the `string` module.

    from string import Template
    templ = Template("You are reading ${book} by ${author}.")
    s = templ.substitute(book="Perl Hacks", author="Damian Conway")

    print(s)    # prints You are reading Perl Hacks by Damian Conway.

There is an alternative, we can use dictionary too like below:

    data = {
        "book": "Perl Hacks",
        "author": "Damian Conway"
    }
    s1 = templ.substitute(data)

    print(s1)   # prints You are reading Perl Hacks by Damian Conway.
    
Look up environment name.

    import os
    print(os.environ.get("ENV_NAME")) # prints value of environment name "ENV_NAME".

    $ export ENV_NAME="local"    

    print(os.environ.get("ENV_NAME")) # prints local

#### Comments

For single line comment, you can use `#` same as in `Perl`.

For multilines comment, you have to use `'''` i.e. 3 single quotes in the beginning and in the end.

#### Documentations

If you ever want to find documentation of any built-in functions in `Python` then you can use `__doc__`.

    print(map.__doc__)

It also applies to module too.

    import itertools

    print(itertools.__doc__)

You can also create documentation of user defined function like below:

    def addFive(n) -> int:
        """addFive(n) --> adds 5 to the given number.

        Parameters:
        n: Any number.
        """
        return (n+5)

    print(addFive.__doc__)

#### Docstring Best Practices

    1) Enclose docstrings in tripe quotes.
    2) First line should be summary sentence of functionality.
    3) Modules: List important classes, functions, exceptions.
    4) Classes: List important methods.
    5) Functions: 
       a) List parameters and explain each, one per line. 
       b) If there is a return value then list it otherwise leave it. 
       c) If it raises exception then mention it.

## Variables
***

Variable declaration as simple as below:

    name = "Joe"
    age = 20

or you can combine both in one line as below:

    name, age = "Joe", 20

#### Global / Local variable

    # Global variable
    name = "Joe"

    def showName():
        # Local variable
        name = "Blog"
        print(name)

    showName()   # prints Blog
    print(name)  # prints Joe

Override global variable inside the function.

    # Global variable
    name = "Joe"

    def showName():
        # Override global variable
        global name
        name = "Blog"
        print(name)

    showName()   # prints Blog
    print(name)  # prints Blog

You can even undefine a variable.

    name = "Joe"
    print(name) # prints Joe
    del name
    print(name) # throw error
    
## DataTypes
***

1) `Boolean` defined with keyword `bool` and can only have value `True`/`False`
2) `Whole Numbers` defined with keyword `int`
3) `Decimal Numbers` defined with keyword `float`
4) `Imaginary Numbers` defined with suffix `j` e.g. `x = 2j`
5) `String` defined with keyword `str`

`Booleans` are straight forward but here are some fun bits.

    print(bool(1))           # prints True
    print(bool(0))           # prints False
    print(bool(-1))          # prints True
    print(bool(1j))          # prints True
    print(bool(0.0))         # prints False
    print(bool(0j))          # prints False
    print(bool('True'))      # prints True
    print(bool('False'))     # prints False
    print(bool(''))          # prints False
    print(bool([]))          # prints False
    print(bool([1,2]))       # prints True    
    print(bool({}))          # prints False
    print(bool(None))        # prints False    

Here is some use case:

    scores = [10,22,30]
    if scores:
        print("Found some scores.")

The above code is same as:

    scores = [10,22,30]
    if bool(scores):
        print("Found some scores.")

`Numbers` are defined as below:

    x = 1
    print(type(x))           # prints <class 'int'>

    y = 1.5
    print(type(y))           # prints <class 'float'>
    
    z = 1j
    print(type(z))           # prints <class 'complex'>

The `int()` is very handy to convert string to int as below:

    print(int('100'))        # prints 100

However if we pass the second argument to the `int()` then it will treat it as base when converting.

    print(int('100', 2))     # prints 4

Even this throws error:

    print(int(100, 2))       # TypeError: int() can't convert non-string with explicit base

Few other examples with different base:

    print(int('1ab', 16))    # prints 427

If doing calculation with floating numbers then you have to be extra vigilante.

    print(1.2 - 1.0)         # prints 0.19999999999999996

To deal with this, we use `decimal` module as below:

    from decimal import Decimal, getcontext

Here we import `Decimal` class and `getcontext()` function.

    print(getcontext())

You should see the default settings for `Decimal` class as below:

    Context([prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, 
    clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

We can change the precision to 4 decimal places like below:

    getcontext().prec = 4
    print(getcontext())

You should now see something like below:

    Context([prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, 
    clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

Let's play with some numbers:

    print(Decimal(1) / Decimal(3))     # prints 0.3333

Or if we change it to 2 decimal places:

    getcontext().prec = 2
    print(Decimal(1) / Decimal(3))     # prints 0.33

Here is some interesting aspects of floating point numbers:

    print(Decimal(3.14))               # prints 3.140000000000000124344978758017532527446746826171875

But this is fine.

    print(Decimal('31.4'))             # prints 3.14

`String` contains unicode whereas `Byte` is raw 8-bits values.

    s = "Hi there!"
    b = bytes([0x41, 0x42, 0x43])

    print(s)  # prints Hi there!
    print(b)  # prints b'ABC'

We can't combine `String` and `Byte` using `+` operator.

    print(s+b)     # would throw error as print() expects string and not byte

To solve the issue, we have to decode the bytes using `'utf-8'` encoding like below:

    s1 = b.decode('utf-8')
    print(s+s1)    # prints Hi there!ABC

Or we could encode the string using '`utf-8'` encoding and concatenate like this:

    b1 = s.encode('utf-8')
    print(b1+b)    # prints b'Hi there!ABC'

What if we encode the string using `'utf-32'` encoding?

    b2 = s.encode('utf-32')
    print(b2)      # prints lots of hexadecimal numbers representing the string.

**NOTE**: `String` and `Byte` are not the same.

Let's play with bytes in the following example it creates empty `Bytes` object of 4 bytes long.

    print(bytes(4))                    # prints b`\x00\x00\x00\x00'

    smiley = bytes('😊', 'utf-8')
    print(smiley)                      # prints b'\xf0\x9f\x98\x8a'

We can decode the bytes as below:

    print(smiley.decode('utf-8'))      # prints 😊

We can even create byte array using the `bytearray()` function like below:

    smiley = bytearray('😊', 'utf-8')
    print(smiley)                      # prints bytearray('\xf0\x9f\x98\x8a')

Let's change the `4th` element of the bytearray with hexadecimal of 85.

    smiley[3] = int('85', 16)

Check what it looks like now:

    print(smiley.decode('utf-8'))      # prints 😅

#### Basic Collections

    1) List: Mutable sequence of values e.g. [1,2,3]
    2) Tuple: Fixed sequence of values e.g. (1,2,3)
    3) Set: Sequence of distinct values e.g. {1,2,3}
    4) Dictionary: Collection of key-value pairs e.g. {"a":1, "b":2, "c":3}

Let's try some basic examples of collections.

    l = [1,2,3,4]
    print(type(l))         # prints list
    print(len(l))          # prints 4

`List` element can be accessed with `0-indexed` key. The elements order is important for list.

    print(l[0])            # prints 1
    print([1,2] == [1,2])  # prints True
    print([1,2] == [2,1])  # prints False

`Tuple` elements can't be changed and they can be accessed with `0-indexed` key. The elements order is important for tuple.

    t = (1,2,3)
    print(type(t))         # prints tuple
    print(len(t))          # prints 3
    print(t[0])            # prints 1

    print((1,2) == (1,2))  # prints True
    print((1,2) == (2,1))  # prints False

`Set` can only have unique elements. It can be initialised passing a list to `set()` function.

    s = {1,2,2,3}
    print(type(s))         # prints set
    print(len(s))          # prints 3
    print(s)               # prints {1,2,3}

    s = set([1,2,3,4])
    print(type(s))         # prints set
    print(len(s))          # prints 4
    print(s)               # prints {1,2,3,4}

New element can be added to a set using `add()` method.

    s.add(5)
    print(s)               # prints {1,2,3,4,5}

More than one elements can be added to a set using `update()` method.

    s.update([5,6,7])
    print(s)               # prints {1,2,3,4,5,6,7}

    s.update([4,5,8],'a')
    print(s)               # prints {1,2,3,4,5,6,7,8,'a'}

For sets, order of element is NOT important.

    print({1,2} == {1,2})  # prints True
    print({1,2} == {2,1})  # prints True

`Dictionary` can have unique keys only.

    d = {"a": 1, "b": 2}
    print(d["a"])          # prints 1
    print(d.keys())        # prints ["a","b"]

On top of the above listed, the `collections` module provides some more like below:

    1) namedtuple: Tuple with named fields
    2) OrderedDict, defaultdict: Dictionaries with special properties
    3) Counter: Counts distinct values
    4) deque: Double-ended list objects

Let's see some examples showing `namedtuple`:

    import collections

    Point = collections.namedtuple("Point", "x, y")
    p1 = Point(10,20)
    p2 = Point(30,40)
    print(p1, p2)       # prints Point(x=10, y=20) Point(x=30, y=40)
    print(p1.x, p2.y)   # prints 10 40

You can use `_replace` to create new instance.

    p1 = p1._replace(x=100)
    print(p1)           # prints Point(x=100, y=20)

Now let's see some example showing `defaultdict`.

    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana' ]

    fruitCounter = {}
    for fruit in fruits:
        fruitCounter[fruit] += 1

The above code would throw `KeyError: 'apple'` as we try to set the counter without initialising.

We can sort the issue like this:

    for fruit in fruits:
        if fruit in fruits.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

The above change is unnecessary and we can avoid it with the help of `defaultdict`.

    from collections import defaultdict
    
    fruitCounter = defaultdict(int)
    for fruit in fruits:
        fruitCounter[fruit] += 1

Now you see no more error as before.

We could even use `lambda` instead of `int` like this:

    fruitCounter = defaultdict(lambda: 100)
    for fruit in fruits:
        fruitCounter[fruit] += 1

You should see the count goes up by `100`.

Let's see some examples showing `Counter`:

    from collections import Counter

    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah",
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["James"])                                 # prints 2
    print(sum(c1.values()), " students in class 1.")   # prints 11 students in class 1.
    
    c1.update(class2)
    print(sum(c1.values()), " students in class 1.")   # prints 23 students in class 1.    

    print(c1.most_common(3))                           # prints [('James',3), ('Frank', 2), ('Bob', 1)]

    c1.subtract(class2)
    print(c1.most_common(3))                           # prints [('James',2), ('Bob', 1), ('Becky', 1)]

    print(c1 & c2)                                     # prints Counter({'Frank': 1, 'James': 1})

Let's see some examples showing `OrderedDict`:   

    from collections import OrderedDict

    sportTeams = [("Royals", (18,12)), 
                  ("Rockets", (24,6)),
                  ("Cardinals", (20,10)), 
                  ("Dragons", (22,8)),
                  ("Kings", (15,15)), 
                  ("Charger", (20,10)),
                  ("Jets", (16,14)), 
                  ("Warriors", (25,5))]

    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    teams = OrderedDict(sortedTeams)
    print(teams)

You should see something like below:

    OrderedDict([("Warriors", (25,5)), 
                 ("Rockets", (24,6)), 
                 ("Dragons", (22,8)), 
                 ("Cardinals", (20,10)), 
                 ("Charger", (20,10)), 
                 ("Royals", (18,12)), 
                 ("Jets", (16,14)), 
                 ("Kings", (15,15))])

Let's pop the top team and its win/loss numbers.

    team, winloss = teams.popitem(False)
    print("Top Team: ", team, winloss)             # prints Top Team: Warrior (25,5)

How about next `Top 4` teams?

    for i, team in enumerate(teams, start = 1):
        print(i, team)
        if i == 4:
            break

Here is result of the above code:

    1 Rockets
    2 Dragons
    3 Cardinals
    4 Chargers

How about test for equality?

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})    
    print("Equality Test: ", a == b)            # prints Equality Test: True

If we change the order of items?

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})    
    print("Equality Test: ", a == b)            # prints Equality Test: False

If we change it to regular dictionary?

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = {"a": 1, "c": 3, "b": 2}
    print("Equality Test: ", a == b)            # prints Equality Test: True

Let's see some examples showing `Deque`. It is pronounced as `Double-ended Queue`.

    d = collections.deque("abcdefg")

It is like each letter in a cell of its own. 

    ["a", "b", "c", "d", "e", "f", "g"]

The `appendleft()` or `popleft()` applies to the side `"a"` i.e the start position.

The `append()` or `pop()` applies to the side `"g"` i.e. the end position.

There is also a `rotate()` function that operates in either direction. 

It takes a parameter that indicates how many items to rotate and it defaults to 1. The positive number rotate to the `right` and negative number to the `left`.

    import collections
    import string

    d = collections.deque(string.ascii_lowercase)
    print("Item count: ", str(len(d)))  # prints Item count: 26

    for elem in d:
        print(elem.upper(), end=",")    # prints A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
    
    d.pop()                             # removes 'z'
    d.popleft()                         # removes 'a'
    d.append(2)                         # adds '2' at the end
    d.appendleft(1)                     # adds '1' at the start
    
    print(d)        
    # deque(['1','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','2'])

    d.rotate(10)
    
    print(d)        
    # deque(['q','r','s','t','u','v','w','x','y','2','1','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
    
`List`: Square bracket `[]` can be used to create a list.

    list = [2, 4, 6, 8, 10]
    print(list[2]) # prints 6

    list[2] = 60
    print(list[2]) # prints 60

Slice a list using the syntax `list[startindex: endindex: step]`.

Default `startindex` is `0` and default `step` is `1`.

    print(list[1:3])   # prints [4, 6]
    print(list[0:5,2]) # prints [2, 6, 10]

Reverse a given list using the slice syntax.

    print(list[::-1])  # prints [10, 8, 6, 4, 2]

Elements in a list can be changed. 

Also elements do not have to be of one type. 

Search an element in a list and return the count using the `count()` method.

    chars = ["a", "b", "a", "a", "c", "d"]
    print(chars.count("a"))  # prints 3

You can merge two lists like below:

    vowels = ["a", "e", "i", "o", "u"]
    print(chars + vowels)    # prints ['a', 'b', 'a', 'a', 'c', 'd', 'a', 'e', 'i', 'o', 'u']

Find the length of a list.

    print(len(chars))        # prints 6

Working with two dimension list.

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix[0][0])      # prints 1
    print(matrix[2][2])      # prints 9

You can update an element of a list.

     matrix[0][0] = 0
     print(matrix[0][0])     # prints 0

Remove an entry from the list using `remove()` method.

    vowels.remove("e")
    print(vowels)            # prints ['a', 'i', 'o', 'u']

You can also insert an element at a given index like below:

    chars.insert(0, "z")
    print(chars)             # prints ['z', 'a', 'b', 'a', 'a', 'c', 'd']

You can even remove an element from any index in the list using `pop()`.

If nothing passed to `pop()` it would remove the last element in the list.

    last = chars.pop()
    print(last)              # prints d
    print(chars)             # prints ['z', 'a', 'b', 'a', 'a', 'c']

Let's pop the third element from the list.

    third = chars.pop(2)
    print(third)             # prints b
    print(chars)             # prints ['z', 'a', 'a', 'a', 'c']

You can use `sort()` method and `sorted()` function with list for sorting purpose.

    nums = [1, 3, 2, 5, 4]
    nums.sort()
    print(nums)              # prints [1, 2, 3, 4, 5]

    nums_sorted = sorted(nums)
    print(nums_sorted)       # prints [1, 2, 3, 4, 5]

You can add element at the end of the list using `append()` method.

    nums.append(6)
    print(nums)              # prints [1, 2, 3, 4, 5, 6]

You can have elements of different data types.

    list = ["Adam", 50, True, 1.5]
  
Braces `()` can be used to create a `Tuple`. 

Elements in `Tuple` **CAN NOT** be changed unlike `List`.

    child = ("Joe", "male", 2, "UK")
    print(child[0]) # prints child name

    type(child) # prints tuple

`Dictionary` is a key-value list, just like `hash` in `Perl`.

    users = { "name": "Joe", "age": 20 }
    print(users["name"]) # prints Joe
    print(users["age"])  # prints 20

You can use `get()` method of dictionary to fetch value of the given key as below:

    print(users.get("name"))  # prints Joe

What if the given key doesn't exist in the dictionary?

It would return `None` as shown below:

    print(users.get("unknown"))  # prints None

In case, you don't want `None` if key is missing key then you can provide the optional value as second parameter to the `get()` method.

    print(users.get("unknown", "Perl"))  # prints Perl

If you want to add new item to a dictionary, then you have two choices as shown below:

    users["sex"] = "male"
    users.update({ "location": "London" })

To fetch all keys in the dictionary, you can do this:

    print(users.keys())  # prints dict_keys(['name', 'age', 'sex', 'location'])

If you want to loop through each key in the dictionary, try something this:

    for k in users.keys():
        print(f'{k} = {users[k]}')

We get this result:

    name = Joe
    age = 20
    sex = male
    location = London

There is another way you can fetch each item in the dictionary by calling `items()` method as below:

    d = {"a": 1, "b": 2, "c": 3}
    print(d.items());

It returns `dict_items()` object like below:

    dict_items([{"a": 1, "b": 2, "c": 3}])

Or we can fetch key, value individually like this:

    for k,v in users.items():
        print(f'{k} = {v}')

You get the same result as above:

    name = Joe
    age = 20
    sex = male
    location = London

How about fetching all values in the dictionary?

    print(users.values())  # prints dict_values(['Joe', 20, 'male', 'London'])

To delete an item from the dictionary, you can use `pop()` method as below:

    value = users.pop("sex")
    print(value)  # print male

    for k,v in users.items():
        print(f'{k} = {v}')

You see the key `sex` missing from the dictionary.    

    name = Joe
    age = 20
    location = London

If you have two dictionaries and wants to merge into one then do this:

    dict1 = { "name": "Joe" }
    dict2 = { "age": 20 }
    dict1.update(dict2)
    print(dict1)         # {'name': 'Joe', 'age': 20}

Built-in function `type()` can be used to identify the data type.

## Functions
***

User can define function using the keyword `def` as below:

    def addFive(n: int) -> int:
        return n + 5

    result = addFive(10)
    print(result)  # prints 15
    print(addFive) # prints <function addFive at 0x7fe8fcae2280>

How about function with default value?

    def power(n: int, x: int = 1) -> int:
        result = 1
        for i in range(x):
            result = result * n

        return result

    print(power(2))     # prints 2
    print(power(2, 3))  # prints 8

Function can be called with named parameters in any order.

    print(power(x = 3, n = 2)) # prints 8

If we want to force user to always call the function with named parameters?

Let's redefine the above function `power()` to enforce named parameters calling.

    def power(n, x = 1, *, suppressExceptions=False):
        result = 1
        for i in range(x):
            result = result * n

With the change, you can still call the function as below without any issues.

    print(power(2, 3))  # prints 8

However if we call like below then you would see error.

    print(power(2, 3, True))  # TypeError: power() takes from 1 to 2 positional arguments but 3 were given

Let's call with `suppressExceptions=True` like below:

    print(power(2, 3, suppressExceptions=True))  # prints 8

or like this:

    print(power(2, 3, suppressExceptions=False))  # prints 8

or with named parameters like below:

    print(power(x=2, n=3))  # prints 8
    print(power(n=3, x=2))  # prints 8

Function with variable number of parameters.

    def addAll(*args):
        result = 0
        for i in args:
            result = result + i
        return result

    print(addAll(1,2,3))    # prints 6
    print(addAll(1,2,3,4))  # prints 10

What if we already have a list and wants to pass it as variable arguments.

    nums = [1,2,3]
    print(addAll(*nums))    # prints 6

Function with variable keyword arguments too.

    def func(*args, **kwargs):
        print(args)
        print(kwargs)

Let's call the function like this:

    func(10, 20)

You should see something like below, `*args` is a tuple and `**kwargs` is a dictionary.

    (10, 20)
    {}

How about calling with keyword arguments as well.
    
    func(10, 20, message="hello")

This time you should see this:

    (10, 20)
    {'message': 'hello'}
    
THe parameters passed to a function can be fetched using `locals()` function as below:

    def func(x, y, op="sum"):
        print(locals())

    func(10, 20, op="multiply")
    
You should see something like this:

    {"x": 10, "y": 20, "op": "multiply"}

Similar to `locals()`, we have a `globals()` function as well.

    print(globals())

This is what we get back:

    {'__name__': '__main__', 
     '__doc__': None, 
     '__package__': None, 
     '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
     '__spec__': None, 
     '__annotations__': {}, 
     '__builtins__': <module 'builtins' (built-in)>}        

#### Built-in functions in Python

You can get the complete list [**here**](https://docs.python.org/3/library/functions.html).

    a) print("") 
    b) input("") returns string typed user data.
    c) int() returns integer value of the input data.
    d) str() returns string value of the input data.
    e) + operator can be used for string concatenation e.g. print("Hello " + name)

#### Lambda Functions

The `Lambda` function is like anonymous function in `Perl`.

    def CelciusToFahrenheit(temp):
        return (temp * 9/5) + 32
    def FahrenheitToCelcius(temp):
        return (temp - 32) * 5/9

    celcius = [0, 12, 34, 100]
    fahrenheit = [32, 65, 100, 212]

    print(list(map(FahrenheitToCelcius, fahrenheit)))
    print(list(map(CelciusToFahrenheit, celcius)))

Let's use the `lambda` function instead of regular function.

    print(list(map(lambda t: (t - 32) * 5/9, fahrenheit)))
    print(list(map(lambda t: (t * 9/5) + 32, celcius)))

Let's try some most useful built-in functions.

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

    [('Netherlands', 17500000), 
     ('Nigeria', 190000000), 
     ('Jordan', 10000000), 
     ('Nepal', 30000000), 
     ('Niger', 24000000), 
     ('Japan', 128000000)]

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

    [Country('Portugal', 10_000_000), 
     Country('Jordan', 10_000_000), 
     Country('Netherlands', 17_500_000), 
     Country('Taiwan', 24_000_000), 
     Country('Niger', 24_000_000), 
     Country('Nepal', 30_000_000), 
     Country('Japan', 128_000_000), 
     Country('Nigeria', 198_000_000)]

If you want to reverse the sort order.

    sorted(country_list, key=lambda x: x.population, reverse=True)

Sort order is reversed now as you see below:

    [Country('Nigeria', 198_000_000), 
     Country('Japan', 128_000_000), 
     Country('Nepal', 30_000_000), 
     Country('Taiwan', 24_000_000), 
     Country('Niger', 24_000_000),  
     Country('Netherlands', 17_500_000), 
     Country('Portugal', 10_000_000), 
     Country('Jordan', 10_000_000)]

We can get the same result doing this:

    sorted(country_list, key=lambda x: -x.population)

Reverse order as before.

    [Country('Nigeria', 198_000_000), 
     Country('Japan', 128_000_000), 
     Country('Nepal', 30_000_000), 
     Country('Taiwan', 24_000_000), 
     Country('Niger', 24_000_000), 
     Country('Netherlands', 17_500_000), 
     Country('Portugal', 10_000_000), 
     Country('Jordan', 10_000_000)]

If you noticed, `Taiwan` and `Niger` both have the populations `24_000_000` but `Taiwan` appears before `Niger`. 

In theory `Niger` should come first.

Let's sort in decreasing order of population and increasing name alphabetically.

    sorted(country_list, key=lambda x: (-x.population, x.name))

Here is what we get.

    [Country('Nigeria', 198_000_000), 
     Country('Japan', 128_000_000), 
     Country('Nepal', 30_000_000), 
     Country('Niger', 24_000_000), 
     Country('Taiwan', 24_000_000), 
     Country('Netherlands', 17_500_000), 
     Country('Jordan', 10_000_000), 
     Country('Portugal', 10_000_000)]

What if we want to sort reverse by name too? 

Well you can't do `-x.name`, instead you would need to do like below:

    print(sorted(country_list, key=lambda x: (x.population, x.name), reverse=True))

Now if you want to sort on a field that has alphnumeric characters, something like below:

    iso = [('Taiwan', 'iso24000000'), 
           ('Portual', 'iso10000000'), 
           ('Netherlands', 'iso17500000'), 
           ('Nigeria', 'iso198000000'), 
           ('Jordan', 'iso10000000'), 
           ('Nepal', 'iso30000000'), 
           ('Niger', 'iso24000000'), 
           ('Japan', 'iso128000000')]

As you see the population has the three letters code `iso` at the start.

    def get_population(pair):
        country, population = pair
        return population[3:] # ignore the first three letters i.e. iso
 
     print(sorted(iso, key=get_population))

Below is what we get back:

    [('Portual', 'iso10000000'),
     ('Jordan', 'iso10000000'), 
     ('Japan', 'iso128000000'), 
     ('Netherlands', 'iso17500000'), 
     ('Nigeria', 'iso198000000'), 
     ('Taiwan', 'iso24000000'), 
     ('Niger', 'iso24000000'), 
     ('Nepal', 'iso30000000')]

Did you notice it didn't do as expected? 

`Japan` comes before `Netherlands` since sorting done alphabetically `128_000_000` appears before `17_000_000`.    

We can handle this issue very easily using type cast.

    def get_population1(pair):
        country, population = pair
        return int(population[3:]) # ignore the first three letters i.e. iso
 
     print(sorted(iso, key=get_population1))

Finally we have done it correctly.

    [('Portual', 'iso10000000'), 
     ('Jordan', 'iso10000000'), 
     ('Netherlands', 'iso17500000'), 
     ('Taiwan', 'iso24000000'), 
     ('Niger', 'iso24000000'), 
     ('Nepal', 'iso30000000'), 
     ('Japan', 'iso128000000'), 
     ('Nigeria', 'iso198000000')]

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

## Modules
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

#### itertools

The `itertools` is a very powerful module of `Python` and it is shipped with the source, so you don't need to install it separately.

It is used to create iterators.

The different types of iterator that you can create are as follow:

    1) Cycle Iterator
    2) Count Iterator
    3) Accumulate Iterator
    4) Chain Iterator
    5) dropwhile
    6) takewhile

The `Cycle` iterator is used to create infinite iterator as shown below:

    import itertools
    
    names = ["Joe", "Blog", "Bill", "Gates"]
    iter = itertools.cycle(names)
    print(next(iter))     # prints Joe
    print(next(iter))     # prints Blog
    print(next(iter))     # prints Bill
    print(next(iter))     # prints Gates
    print(next(iter))     # prints Joe

The `Count` iterator is used to create counter as shown below. 

It takes starting value which defaults to `0` and step value which defaults to `1`.

    counter = itertools.count(100, 10)
    print(next(counter))  # prints 100
    print(next(counter))  # prints 110
    print(next(counter))  # prints 120

The `Accumulate` iterator accumulates values.

    scores = [10,20,50,20,40,30]
    accum = itertools.accumulate(scores)
    print(list(accum))    # prints 10, 30, 80, 100, 140, 170
    
We can change the default behaviour of `Accumulate` iterator which is `addition` to something else.

    accum = itertools.accumulate(scores, max)
    print(list(accum))    # prints 10, 20, 50, 50, 50, 50

It you noticed, when it reached the max value, it keeps repeating until the list ends.

The `Chain` iterator connects all the sequences together.

    chain = itertools.chain("ABCD", "1234")
    print(list(chain))    # prints ['A','B','C','D','1','2','3','4']

The `dropwhile` and `takewhile` will return values until a certain condition is met that stops them.

    def testFunction(s):
        return s < 40

    scores = [10,20,50,20,40,30]
    print(list(itertools.dropwhile(testFunction, scores)))  # prints [50,20,40,30]
    print(list(itertools.takewhile(testFunction, scores)))  # prints [10,20]

The `dropwhile` will drop score from the list where the `testFunction` returns true.

The `takewhile` will take score from the list where the `testFunction` returns true.

#### enum

The `enum` module provides `Enum` class to define enumerations.

    from enum import Enum
    
    class Fruit(Enum):
        APPLE = 1
        BANANA = 2
        ORANGE = 3
        TOMATO = 4

    print(Fruit.APPLE)           # prints Fruit.APPLE
    print(type(Fruit.APPLE))     # prints <enum 'Fruit'>
    print(repr(Fruit.APPLE))     # prints <Fruit.APPLE: 1>

Every `enum` has a `name` and a `value`.

    print(Fruit.APPLE.name, Fruit.APPLE.value)     # Apple 1

`enum` names are always `UNIQUE` but can have same values.

You can enforce checking values to be unique as well by importing `unique` class.

    from enum import Enum,unique

    @unique
    class Fruit(Enum):
        APPLE = 1
        BANANA = 2
        ORANGE = 3
        TOMATO = 4

You can autogenerate unique value for names using the `auto` class.

    from enum import Enum,unique,auto

    @unique
    class Fruit(Enum):
        APPLE = 1
        BANANA = 2
        ORANGE = 3
        TOMATO = 4
        PEAR = auto()

    print(Fruit.PEAR.value)           # prints 5

`enums` are hashable and can be used as keys.

    fruits = {}
    fruits[Fruit.BANANA] = "Healthy Fruit"
    print(fruits[Fruit.BANANA])       # prints Healthy Fruit

#### Class String Functions

The `object.__str__(self)` function is called for `str(object)`, `print(object)` and `"{0}".format(object)`.

The `object.__repr__(self)` funciton is called for `repr(object`.

The `object.__format__(self, format_spec)` is called for `format(object, format_spec)`.

The `object.__bytes__(self)` is called for `bytes(object)`.

Let's us see some examples:

    class Author():
        def __init__(self):
            self.fname = "Damian"
            self.lname = "Conway"
            self.book  = "Perl Hacks"

    author = Author()
    print(author)                              # prints <__main__.Author object at 0x7f26446c6640>
    print(str(author))                         # prints <__main__.Author object at 0x7f26446c6640>
    print(repr(author))                        # prints <__main__.Author object at 0x7f26446c6640>
    print("Formatted: {0}".format(author))     # prints Formatted: <__main__.Author object at 0x7f26446c6640>

Let's override string function `__repr__()`

    class Author():
        def __init__(self):
            self.fname = "Damian"
            self.lname = "Conway"
            self.book  = "Perl Hacks"

        def __repr__(self):
            return "<Author Class - {0} {1} {2}>".format(self.fname, self.lname, self.book)

    author = Author()
    print(author)                              # prints <Author Class - Damian Conway Perl Hacks>
    print(str(author))                         # prints <Author Class - Damian Conway Perl Hacks>
    print(repr(author))                        # prints <Author Class - Damian Conway Perl Hacks>
    print("Formatted: {0}".format(author))     # prints Formatted: <Author Class - Damian Conway Perl Hacks>

Let's override string function `__str__()` now.

    class Author():
        def __init__(self):
            self.fname = "Damian"
            self.lname = "Conway"
            self.book  = "Perl Hacks"

        def __repr__(self):
            return "<Author Class - {0} {1} {2}>".format(self.fname, self.lname, self.book)

        def __str__(self):
            return "Author ({0, {1}, {2})".format(self.fname, self.lname, self.book)

    author = Author()
    print(author)                              # prints Author(Damian, Conway, Perl Hacks)
    print(str(author))                         # prints Author(Damian, Conway, Perl Hacks)
    print(repr(author))                        # prints <Author Class - Damian Conway Perl Hacks>
    print("Formatted: {0}".format(author))     # prints Formatted: Author(Damian, Conway, Perl Hacks)

Finally let's override string function `__bytes__()` like here:

    class Author():
        def __init__(self):
            self.fname = "Damian"
            self.lname = "Conway"
            self.book  = "Perl Hacks"

        def __repr__(self):
            return "<Author Class - {0} {1} {2}>".format(self.fname, self.lname, self.book)

        def __str__(self):
            return "Author ({0}, {1}, {2})".format(self.fname, self.lname, self.book)

        def __bytes__(self):
            val = "Author:{0}:{1}:{2}".format(self.fname, self.lname, self.book)
            return bytes(val.encode('utf-8'))

    author = Author()
    print(author)                              # prints Author(Damian, Conway, Perl Hacks)
    print(str(author))                         # prints Author(Damian, Conway, Perl Hacks)
    print(repr(author))                        # prints <Author Class - Damian Conway Perl Hacks>
    print("Formatted: {0}".format(author))     # prints Formatted: Author(Damian, Conway, Perl Hacks)
    print(bytes(author))                       # prints b'Author:Damian:Conway:Perl Hacks'

#### Class Attribute Functions

The `object.__getattribute__(self, attr)` is called for `object.attr`.

The `object.__getattr__(self, attr)` is called for `object.attr`.

The `object.__setattr__(self, attr, val)` is called for `object.attr = val`.

The `object.__delattr__(self)` is called for `del object.attr`.

The `object.__dir__(self)` is called for `dir(object)` to list class attributes.

Let's look at some examples below:

    class Color():
        def __init__(self):
            self.red = 50
            self.green = 75
            self.blue = 100

        def __getattribute(self, attr):
            if attr == "rgbcolor":
                return (self.ref, self.green, self.blue)
            elif attr == "hexcolor":
                return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
            else:
                attributeError

    mycolor = Color()
    print(mycolor.rgbcolor)              # prints (50, 75, 100)
    print(mycolor.hexcolor)              # prints #324b64

Let's override `__setattr__()` function as below:

    class Color():
        def __init__(self):
            self.red = 50
            self.green = 75
            self.blue = 100

        def __getattribute(self, attr):
            if attr == "rgbcolor":
                return (self.ref, self.green, self.blue)
            elif attr == "hexcolor":
                return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
            else:
                attributeError

        def __setattr__(self, attr, val):
            if attr == "rgbcolor":
                self.red = val[0]
                self.green = val[1]
                self.blue = val[2]
            else:
                super().__setattr__(attr, val)

    mycolor = Color()
    print(mycolor.rgbcolor)              # prints (50, 75, 100)
    print(mycolor.hexcolor)              # prints #324b64

    mycolor.rgbolor = (125, 200, 86)
    print(mycolor.rgbcolor)              # prints (125, 200, 86)
    print(mycolor.hexcolor)              # prints #7dc856

You can still access regular attributes like below:

    print(mycolor.red)                   # prints 125

Let's override `__dir__()` function as below:

    class Color():
        def __init__(self):
            self.red = 50
            self.green = 75
            self.blue = 100

        def __getattribute(self, attr):
            if attr == "rgbcolor":
                return (self.ref, self.green, self.blue)
            elif attr == "hexcolor":
                return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
            else:
                attributeError

        def __setattr__(self, attr, val):
            if attr == "rgbcolor":
                self.red = val[0]
                self.green = val[1]
                self.blue = val[2]
            else:
                super().__setattr__(attr, val)

        def __dir__(self):
            return ("red", "green", "blue", "rgbcolor", "hexcolor")

    mycolor = Color()
    print(mycolor.rgbcolor)              # prints (50, 75, 100)
    print(mycolor.hexcolor)              # prints #324b64

    mycolor.rgbolor = (125, 200, 86)
    print(mycolor.rgbcolor)              # prints (125, 200, 86)
    print(mycolor.hexcolor)              # prints #7dc856

    print(dir(mycolor))                  # prints ("red", "green", "blue", "rgbcolor", "hexcolor")

#### Class Numerical Operators

The `object.__add__(self, other)` is same as `self + other`.

The `object.__sub__(self, other)` is same as `self - other`.

The `object.__mul__(self, other)` is same as `self * other`.

The `object.__div__(self, other)` is same as `self / other`.

The `object.__floordiv__(self, other)` is same as `self // other`.

The `object.__pow__(self, other)` is same as `self ** other`.

The `object.__and__(self, other)` is same as `self & other`.

The `object.__or__(self, other)` is same as `self or other`.

You can also use `in-place` operations like below:

The `object.__iadd__(self, other)` is same as `self += other`.

The `object.__isub__(self, other)` is same as `self -= other`.

The `object.__imul__(self, other)` is same as `self *= other`.

The `object.__itruediv__(self, other)` is same as `self /= other`.

The `object.__ifloordiv__(self, other)` is same as `self //= other`.

The `object.__ipow__(self, other)` is same as `self **= other`.

The `object.__iand__(self, other)` is same as `self &= other`.

The `object.__ior__(self, other)` is same as `self or= other`.

Let's show some of the above functions in the following example:

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return "<Point x:{0}, y:{1}>".format(self.x, self.y)

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point(self.x - other.x, self.y - other.y)
    
        def __iadd__(self, other):
            self.x += other.x
            self.y += other.y
            return self

    p1 = Point(10, 20)
    p2 = Point(30, 30)

    print(p1, p2)          # prints <Point x:10,y:20> <Point x:30,y:30>

    p3 = p1 + p2
    print(p3)              # prints <Point x:40,y:50>

    p4 = p2 - p1
    print(p4)              # prints <Point x:20,y:10>

    p1 += p2
    print(p1)              # prints <Point x:40,y:50>

#### Class Comparison Operators

The `object.__gt__(self, other)` is same as `self > other`.

The `object.__ge__(self, other)` is same as `self >= other`.

The `object.__lt__(self, other)` is same as `self < other`.

The `object.__le__(self, other)` is same as `self <= other`.

The `object.__eq__(self, other)` is same as `self == other`.

The `object.__ne__(self, other)` is same as `self != other`.

    class Employee():
        def __init__(self, fname, lname, level, years):
            self.fname = fname
            self.lname = lname
            self.level = level
            self.years = years

        def __ge__(self, other):
            if self.level == other.level:
                return self.years >= other.years
            return self.level >= other.level

        def __gt__(self, other):
            if self.level == other.level:
                return self.years > other.years        
            return self.level > other.level

        def __le__(self, other):
            if self.level == other.level:
                return self.years <= other.years        
            return self.level <= other.level

        def __lt__(self, other):
            if self.level == other.level:
                return self.years < other.years        
            return self.level < other.level

        def __eq__(self, other):
            pass

    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Rpbinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))    

    print(dept[0] > dept[2])          # prints False
    print(dept[4] < dept[3])          # prints True

Now if we want to sort employee then you can do something like below:

    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)

You should see the result like this:

    Doe
    Sims
    Durden
    Robinson
    Smith
        
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

The ternary operator in `Python` is a one-line shorthand for an if-else statement.

    value_if_true if condition else value_if_false

For example:

    x = 2
    message = 'Even' if x % 2 == 0 else 'Odd'
    print(message)                                  # prints Even

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

In `Python` we can use `for-else` loop as below:

    for number in range(2, 100):
        for factor in range(2, int(number ** 0.5)+1):
            if number % factor == 0:
                break
        else:
            print(f'{number} is prime')
    
Same with While loop.

      vowels = ["a", "e", "i", "o", "u"]
      i = 0
      while i < len(vowels):
          print(vowels[i])
          i += 1

Let's create code to pause for `2 seconds`.

    import datetime
    
    two_seconds = datetime.now().second + 2
    while datetime.now().second != two_seconds:
        pass

Or use `break` to do the same as below:

    import datetime
    
    two_seconds = datetime.now().second + 2
    while True:
        if datetime.now().second == two_seconds:
            break

or use `continue` to do the same.

    import datetime
    
    two_seconds = datetime.now().second + 2
    while True:
        if datetime.now().second < two_seconds:
            continue
           
Use of `break` in for loop structure.

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

## Logging
***

The `logging` module can be used for adding log for different levels as below:

    1) logging.debug("debug level")
    2) logging.info("info level")
    3) logging.warning("warning level")
    4) logging.error("error level")
    5) logging.critical("critical level")

Let's us show some examples:

    import logging

    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

You should only see the following debug messages:

    WARNING:root:This is warning message
    ERROR:root:This is error message
    CRITICAL:root:This is critical message

So by default, `Python` only logs message level `WARNING` or above.

We can change the default behaviour by calling `basicConfig()` method as below:

    import logging

    logging.basicConfig(level = logging.DEBUG)

    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

Now you should see these logging messages:

    DEBUG:root:This is debug message
    INFO:root:This is info message
    WARNING:root:This is warning message
    ERROR:root:This is error message
    CRITICAL:root:This is critical message

By default logging message dump on the console but we can direct it to a log file like below:

    import logging

    logging.basicConfig(level = logging.DEBUG,
                        filename = "output.log")

    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

With the above changes all the log messages are now getting saved in the log file `output.log`.

Be default log message would be appended to the log file.

We can change this default behaviour by passing `filemode` parameter to the `basicConfig()` function like below:

    import logging

    logging.basicConfig(level = logging.DEBUG,
                        filename = "output.log",
                        filemode = "w")

    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

    logging.info("Here is a {} variable and an int:".format("string", 10))

#### Customized Logging

The `basicConfig()` function can be called with parameters `format` and `datefmt` to control how we want to log the message.

Some examples that can be passed as format string to the function `basicConfig()`.

    1. %(asctime)s   - Human readable date format when the log was created
    2. %(filename)s  - File name when the log message originated
    3. %(funcName)s  - Function name where the log message was originated
    4. %(levelname)s - String representation of the message level
    5. %(levelno)d   - Numeric representation of the message level
    6. %(lineno)d    - Source line number where the logging call was issued
    7. %(message)s   - The logged message string
    8. %(module)s    - Module name portion of the filename where the message was logged

Let's show some example:

    import logging

    logging.basicConfig(filename = "output.log", 
                        level = logging.DEBUG, 
                        filemode = "w")

    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level log message")

When we run the code as is we should see the following 2 lines in the log file `output.log`.

    INFO:root:This is an info-level log message
    WARNING:root:This is a warning-level log message

Let's add format str now.

    import logging

    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    logging.basicConfig(filename = "output.log", 
                        level = logging.DEBUG, 
                        filemode = "w", 
                        format = fmtstr)

    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level log message")

Now check the log file.

    2024-01-13 12:22:33,450: INFO: main Line:18 This is an info-level log message
    2024-01-13 12:23:39,634: WARNING: main Line:19 This is a warning-level log message    

Let's add another function to log from and also date format string.

    import logging

    def anotherFunction():
        logging.debug("This is a debug-level message")

    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename = "output.log", 
                        level = logging.DEBUG, 
                        filemode = "w", 
                        format = fmtstr,
                        datefmt = datestr)

    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level log message")
    anotherFunction()

With this you should see this the log file:

    2024-01-13 12:25:33 PM: INFO: main Line:18 This is an info-level log message
    2024-01-13 12:25:33 PM: WARNING: main Line:19 This is a warning-level log message    
    2024-01-13 12:25:33 PM: DEBUG: anotherFunction Line:7 This is a debug-level log message

Now if we want some additional information as well in the log file.

We could do something like this:

    import logging

    extData = {
        "user": "bill@gate.com"
    }
    
    def anotherFunction():
        logging.debug("This is a debug-level message", extra=extData)

    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename = "output.log", 
                        level = logging.DEBUG, 
                        filemode = "w", 
                        format = fmtstr,
                        datefmt = datestr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level log message", extra=extData)
    anotherFunction()

Running the above code would generate the following logs:

    User:bill@gate.com 2024-01-13 12:30:25 PM: INFO: main Line:18 This is an info-level log message
    User:bill@gate.com 2024-01-13 12:30:25 PM: WARNING: main Line:19 This is a warning-level log message    
    User:bill@gate.com 2024-01-13 12:30:25 PM: DEBUG: anotherFunction Line:7 This is a debug-level log message

## Comprehensions
***

Do you remember this code we did earlier?

    def FahrenheitToCelcius(temp):
        return (temp - 32) * 5/9
        
    fahrenheit = [32, 65, 100, 212]
    print(list(map(FahrenheitToCelcius, fahrenheit)))

The above functionality is very common in `Python` language so they came up with `Comprehensions` to deal with.

The same code can be re-written using the comprehension as below:

    print([ (t*9/5) + 32  for t in [32, 65, 100, 212] ])

#### List Comprehension

Let's perform a mapping function on a list.

    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    evenSquared = list(map(lambda e: e**2, evens))
    print(evenSquared)                               # prints [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

Now we will perform a mapping and filter function on a list.

    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    evenSquared = list(
        map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
    print(evenSquared)                               # prints [36, 64, 100, 144, 196]

Let's do the same using `List Comprehension` like below:

    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)                               # prints [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

Let's apply filter to the `List Comprehension` like below:

    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    print(oddSquared)                                # prints [25, 49, 81, 121, 169, 225]

#### Dictionary Comprehension

    temps = [0, 12, 24, 100]

Given the celcius temperature in the list, we want to build a dictionary mapping celcius temperature to it's corresponding fahrenheit temperature.

    dict = {t: (t * 9/5) + 32 for t in temps if t < 100}
    print(dict)                                      # prints {0: 32.0, 12: 53.6, 34: 93.2}
    print(dict[12])                                  # prints 53.6

Let's merge two dictionaries with comprehension.

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    newteam = {k:v for team in (team1, team2) for k,v in team.items()}
    print(newteam)         # prints {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'White': 12, 'Macke': 88, 'Perce': 4}

#### Set Comprehension

    temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

Suppose we want to build a set of unique fahrenheit temperatures of the given celcius temperatures.

    ftemps1 =  [(t*9/5) + 32 for t in temps]
    ftemps2 =  {(t*9/5) + 32 for t in temps}

    print(ftemps1) # prints [41.0,50.0,53.6,57.2,50.0,73.4,105.8,86.0,53.6,64.4,84.2]
    print(ftemps2) # prints {64.4,73.4,41.0,105.8,75.2,50.0,84.2,53.6,86.0,57.2}

Let's build a set from input source.

    text = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in text}
    print(chars)
    # {'B','N','H','V','Z','E','W','M','C','P','Q','L','Y','G','J','T','A','U','R','I',' ','O','D','K','F','X'}

Let's get rid of space from the set.

    chars = {c.upper() for c in text if not c.isspace()}
    print(chars)
    # {'B','N','H','V','Z','E','W','M','C','P','Q','L','Y','G','J','T','A','U','R','I','O','D','K','F','X'}

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
