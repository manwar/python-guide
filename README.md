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
- [Exception](#exception)
- [File Management](#file-management)
- [Date](#date)
- [Calendar](#calendar)
- [Data Formats](#data-formats)

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

Use of `break` in loop structure

    for i in range(5, 10):
        if i == 7:
            break
        print(i)

The above code prints only `5,6` as when it reached `7` the loop terminates.

Use of `continue` in loop

    for i in range(5, 10):
        if i % 2 == 0:
            continue
        print(i)

The above code skips even number and only prints odd number between 5 and 10 i.e. `5, 7, 9`.

Enumerate a list in loop

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumarate(days):
        print(i, d)

The code would print like below

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

Exception is handle using `try` block

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

Find OS name.

    import os
    from os import path

    print(os.name)

Check if file exists

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

How long ago the file was modified    

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("test.txt"))
    print("It has been", td, "since the file was modified.")
    print("Or,", td.total_seconds(), "seconds.")

Using filesystem shell methods

    import os
    from os import path
    import shutil
    from shutil import make_archive

    if path.exists("test.txt"):
        src = path.realpath("test.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)

        os.rename("test.txt", "newtest.txt")

Archive folder

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

File info

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

Format datetime

1) `%y / %Y` Year
2) `%a / %A` Weekday
3) `%b / %B` Month
4) `%d` day of month
5) `%c` Locale's date and time
6) `%x` Locale's date
7) `%X` Locale's time
8) `%I / %H` 12/24 Hour
9) `%M` Minute
10) `%S` Second
11) `%p` Locale's AM/PM

        from datetime import datetime

        now = datetime.now()
        
        print(now.strftime("The current year: %Y"))
        print(now.strftime("%a, %d %B, %y"))

        print(now.strftime("Local's date and time: %c"))
        print(now.strftime("Local's date: %x"))
        print(now.strftime("Local's time: %X"))

        print(now.strftime("Current time is %I:%M:%S %p"))
        print(now.strftime("24-hour time is %H:%M:%S %p"))

Timedelta

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

First Friday of each month

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

sample.html

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

Create subclass myHTMLParser

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

Use myHTMLParser to parse the html data

    parser = myHTMLParser()
    f = open("sample.html")
    if f.mode == "r":
        contents = f.read()
        parser.feeds(contents)
        
    print("Paragraph tags:", paragraphs)
