## Table of Contents
***
- [Variable](#variable)
- [DataType](#datatype)
- [Function](#function)
- [Module](#module)
- [Condition](#condition)
- [Loop](#loop)
- [Recursion](#recursion)
- [Class](#class)
- [Inheritance](#inheritance)

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
    
## DataType
***

1) Boolean defined with keyword `bool` and can only have value `True`/`False`
2) Integer defined with keyword `int`
3) Floating defined with keyword `float`
4) String defined with keyword `str`

List: Square bracket `[]` can be used to create a list

    list = [2, 4, 6, 8, 10]
    print(list[2]) # prints 6

    list[2] = 60
    print(list[2]) #  now prints 60

Slice a list using syntax `list[startindex: endindex: step]`
Default `startndex` is `0` and default `step` is `1`.

    print(list[1:3])   # prints [4, 6]
    print(list[0:5,2]) # prints [2, 6, 10]

Reverse a given list using the slice syntax

    print(list[::-1]) # prints [10, 8, 6, 4, 2]

#### NOTE: Elements in a list can be changed. Also elements do not have to be of one type. You can have elements of different data types.

    list = ["Adam", 50, True, 1.5]
  
  Tuples: Braces `()` can be used to create `Tuple`. Elements in tuples **CAN NOT** be changed unlike `List`.

    child = ("Joe", "male", 2, "UK")
    print(child[0]) # prints child name

    tyoe(child) # prints tuple

**Dictionary** is a key-value list, just like `hash` in **Perl**.

    users = { "name": "Joe", "age": 20 }
    print(users["name"]) # prints Joe
    print(users["age"])  # prints 20
    
Built-in function `type()` can be used to identify the data type.

## Function
***

User can define function using keyword `def` as below

    def addFive(n):
        return n + 5

    result = addFive(10)
    print(result)  # prints 15
    print(addFive) # prints object name assgined to the function addFive()

Function with default value.

    def power(n, x = 1):
        result = 1
        for i in range(x):
            result = result * n

        return result

    print(power(2))     # prints 2
    print(power(2, 3))  # prints 8

Function can be called with named parameter in any order.

    print(power(x = 3, n = 2)) # prints 8

Function with variable number of parameters.

    def addAll(*args):
        result = 0
        for i in args:
            result = result + i
        return result

    print(addAll(1,2,3))    # prints 6
    print(addAll(1,2,3,4))  # prints 10
    
Built-in functions in Python

#### a) print("") 
#### b) input("") returns string typed user data.
#### c) int() returns integer value of the input data.
#### d) str() returns string value of the input data.
#### e) + operator can be used for string concatenation e.g. print("Hello " + name)

## Module
***

Most commonly used modules in **Python** are `calendar`, `math`, `random`

Return calendar for the month `Jan 2024`

      cal = calendar.month(2024, 1)

Square root of a given number and returns result in floating number

      result = math.sqrt(49) # 7.0

Return random number between `1` and `10` both inclusive
      
      rand = random.randint(1, 10)

Pick random entry from the given sequence
      
      alpha = [ "a", "b", "c", "d" ]
      rand = random.choice(alpha)

Shuffle the given list
      
      random.shuffle(alpha)

## Condition
***

    age = 10
    if age > 5:
        print("age is more than 5.")
     elif age == 5:
        print("age is 5")
     else:
        print("age is less than 5.")

Compact `if-else` condition

    x, y = 1, 2
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than or equal to y")

The above condition can also be done in one line.

    print("x is less than y") if x < y else print("x is greater or equal to y")

  Conditions can be comnined using keyword `"and"`

## Loop
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

The following would print `0,1,2,3`

      for i in range(4):
          print(i)

The following would print `1,3,5,7`

      for i in range(1,8,2):
          print(i)

Print each element in the list

      vowels = ["a", "e", "i", "o", "u"]
      for v in vowels:
          print(v)

Same with While loop

      vowels = ["a", "e", "i", "o", "u"]
      i = 0
      while i < len(vowels):
          print(vowels[i])
          i += 1

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

## Class
***

    class Dog():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("Woof Woof")

    dog = Dog("Foo", 12)
    dog.bark()
    print(dog.name())
    print(dog.age())

    dog.age += 1
    print(dog.age())

## Inheritance
***

    class Dog():
          def __init__(self, name, age):
              self.name = name
              self.age = age

          def bark(self):
              print(self.name + " is barking.")

          def addYear(self):
              self.age += 1

          def getInfo(self):
              print(self.name + " is " + self.age + " years old.")

    class Poodle(Dog):
          def __init__(self, name, age, color, weight):
              self.name = name
              self.age = age
              self.color = color
              self.weight = weight

          def bark(self, manner = "energetically"):
              print(f"{self.name} is barking {manner}.")

          def getInfo(self):
              print(f"{self.name} is a {self.age} years old {self.color} poodle and weighs {self.weight} pounds.")

    class Corgi(Dog):
          def __init__(self, name, age, color, weight):
              self.name = name
              self.age = age
              self.color = color
              self.weight = weight

          def bark(self, manner = "briefly"):
              print(f"{self.name} is barking {manner}.")

          def getInfo(self):
              print(f"{self.name} is a {self.age} years old {self.color} corgi and weighs {self.weight} pounds.")
