***
## Table of Contents
***

- [DataType](#datatype)
- [Function](#function)
- [Module](#module)
- [List/Tuples](#listtuples)
- [Condition](#condition)
- [Loop](#loop)
- [Recursion](#recursion)
- [Class](#class)
- [Inheritance](#inheritance)

***
## DataType
***

1) Boolean defined with keyword bool and can only have value True/False
2) Integer defined with keyword int
3) Floating defined with keyword float
4) String defined with keyword str

Built-in function type() can be used to identify the data type.

***
## Function
***

User can define function using keyword def as below

def addFive(n):
    return n + 5

Built-in functions in Python
a) print("") 
b) input("") returns string typed user data.
c) int() return integer value of the input data.

+ operator can be used to string concatenation e.g. print("Hello " + name)

***
## Module
***

Most commonly used modules in Python are calendar, math, random

  Return calendar for the month Jan 2024
  cal = calendar.month(2024, 1)

  Square root of a given number and returns result in floating number
  result = math.sqrt(49) # 7.0

  Return random number between 1 and 10 inclusive
  rand = random.randint(1, 10)

  Pick random entry from the given sequence
  alpha = [ "a", "b", "c", "d" ]
  rand = random.choice(alpha)

  Shuffle the given list
  random.shuffle(alpha)

***
## List/Tuple
***

  List: [] used to create a list

  list = [2, 4, 6, 8, 10]
  print(list[2]) # prints 6

  list[2] = 60
  print(list[2]) #  now prints 60

  NOTE: Elements in a list can be changed. Also elements do not have to be of one type. You can have elements of different data types.

  list = ["Adam", 50, True, 1.5]
  
  Tuples: () is used to create tuples. Elements in tuples CAN NOT be changed unlike List.
  child = ("Joe", "male", 2, "UK")
  print(child[0]) # prints child name

  tyoe(child) # prints tuple

***
## Condition
***

  age = 10
  if age > 5:
      print("age is more than 5.")
  elif age == 5:
      print("age is 5")
  else:
      print("age is less than 5.")

  Conditions can be comnined using keyword "and"

***
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
  
  Built-in function range(start, stop, step) can also be used in For loop.
  Default start is 0 and step is 1. The stop is NOT inclusive.

  The following would be 0-3
  for i in range(4):
      print(i)

  The following would print 1,3,5,7
  for i in range(1,8,2):
      print(i)

  Print each element in the list
  vowels = ["a", "e", "i", "o", "u"]
  for v in vowels:
      print(v)

  Same with While loop
  vowels = ["a", "e", "i", "o", "u"]
  i = 0
  while i < len(voweks):
      print(vowels[i])
      i += 1

***
## Recursion
***

  a) Factorial using the formula n! = n * (n-1)!

  def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

  b) Summing digits of number

  Sum of digits = 1st digit + 2nd digit + ... + second to last digit + last digit
  or sum of digits before last digit + last digit

  def sumDigits(n):
      if n < 10:
          return n
      else:
          all_but_last = n // 10
          last = n % 10
          return sumDigits(all_but_last) + last

  c) nth Fibonacci number

  def fib(n):
      if n == 1:
          return 0
      elif n == 2:
          return 1
      else:
          fib(n-1) + fib(n-2)

  d) Check Palindrome

  def palindrome(s):
      if len(s) <= 1:
          return True
      else:
          return s[0] == s[-1] and palindrome(s[1:-1])

***
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

***
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
