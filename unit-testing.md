## Unit Testing
***
- [Overview](#overview)
- [FizzBuzz Example](#fizzbuzz-example)
- [XUnit](#xunit)

**Disclaimer:** These are my notes after attending the course [**Unit Testing and Test Driven Development in Python**](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python)

## Overview
***

Levels of Testing

a) **Unit Testing**: Testing at the function level

b) **Component Testing**: Testing is at the library and compiled binary level

c) **System Testing**: Tests the external interface of a system

d) **Performance Testing**: Testing at system level to verify timing and resource usages.

**Unit test** structure made up of three layers

  1) setup
  2) action
  3) assert

**Test Driven Development (TDD)** expect us to do the following

  1) Write unit test before any production code
  2) **DO NOT** write all unit test or production code at once.
  3) Test and production code are written for one use case at a time

**TDD** follows 3 phases:

  1) **RED**: Write a failing unit test
  2) **GREEN**: Write just `ENOUGH` production code to make test pass
  3) **REFACTOR**: clean up and remove duplicate code from unit test and production code

Repeat the cycle until you have covered all the use cases.

The **THREE** laws of **TDD**

  1) Do not write any production code until you have written a failing test
  2) Do not write more than the needed unit test to fail
  3) Do not write more than the needed production code to pass the test
     
`pytest` automatically discovers test based on standard naming conventions.

  1) test function name should start with 'test'
  2) class with test should have class name start with 'Test' and do not have __init__() method
  3) Filename should start or end with 'test'

Suppose in the current folder we have only 3 files as below

  1) test_file.py
  2) file_test.py
  3) ignore-me.py

They all have the following lines of code

    import pytest
    def test_1():
        assert True
    def test_2():
        assert True

Now if we run the command `pytest -v` inside the folder, you would get this:

    file_test.py::test_1 PASSED
    file_test.py::test_2 PASSED
    test_file.py::test_1 PASSED
    test_file.py::test_2 PASSED

As you see, `pytest` only executed test in the files `test_file.py` and `file_test.py`. It completely ignored `ignore-me.py`.

We will now create another file `test_class.py` as below in the same folder

    import pytest
    class TestOne:
        def test_1(self):
            assert True
    class IgnoreMe:
        def test_2(self):
            assert True

Try again the same command `pytest -v`. You should see something like below:

    file_test.py::test_1 PASSED
    file_test.py::test_2 PASSED
    test_class.py::TestOne::test_1 PASSED
    test_file.py::test_1 PASSED
    test_file.py::test_2 PASSED

If you noticed, `pytest` ignored the class `IgnoreMe`.

## FizzBuzz Example
***

Let us apply what we learnt so far in the `FizzBuzz` example. First we will create file named `test_fizzbuzz.py`

    # production code

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    def test_can_call_fizzBuzz():
        fizzBuzz(1)

We just entered the `RED` phase by creating the first fail unit test as shown below

    test_fizzbuzz.py::test_can_call_fizzBuzz FAILED

Now time to write enough production code to get into `GREEN` phase.

    # production code
    def fizzBuzz(value):
        return

We are now in `GREEN` phase after completing the production enough to pass the test

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED

We now have pass unit test. Time to get into `REFACTOR` phase if needed.

Do we need it? I don't think so.

So we will repeat the cycle and get into the `RED` phase again by creating another fail test.

    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert(retVal == "1")

We are in `RED` phase as shown below

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in FAILED
    
Let's update the production code to make the test pass

    # production code
    def fizzBuzz(value) -> str:
        return "1"

We are in `GREEN` phase now.

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED

To do some refactor? 

We can clearly see some code duplication now. The method `fizzBuzz()` is called twice, first in `def test_can_call_fizzBuzz()` and then again `def test_return_1_when_1_passed_in()`.  

Let's clean up the code and merged the two use cases into one as below

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert retVal == "1"

The test method `test_return_1_when_1_passed_in()` covered both use cases. The test still pass after refactor as shown here

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED

Let's get to the third use case and get into the `RED` phase again.

    # case 3: return "2" when 2 passed in
    def test_return_2_when_2_passed_in():
        retVal = fizzBuzz(2)
        assert retVal == "2"

This is what we get when we run the command `pytest -v`.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in FAILED

Let's update the production code to get into the `GREEN` phase.

    # production code
    def fizzBuzz(value) -> str:
        return str(value)

Just one line change from `return "1"` to `return str(value)` in production code makes the test pass again.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED

We now move into `REFACTOR` phase. We can see plenty of duplicate unit test code. 

Let's refactor that.

First we will create funtion `checkFizzBuzz()` as below

    def checkFizzBuzz(value, expectedValue) -> bool:
        retVal = fizzBuzz(value)
        return retVal == expectedValue

Then update the unit test to use it

    # case 1: can call fzzBuzz()?
    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        assert checkFizzBuzz(1, "1")

    # case 3: return "2" when 2 passed in
    def test_return_2_when_2_passed_in():
        assert checkFizzBuzz(2, "2")

After code refactor, we still have all test passed.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED

Time to go for the fourth use case and get into `RED` phase.

    # case 4: return "Fizz" when 3 passed in
    def test_return_Fizz_when_3_passed_in():
        assert checkFizzBuzz(3, "Fizz")

With that we now enter into `RED` phase.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in FAILED

Time to update the production code to get into `GREEN` phase

    # production code
    def fizzBuzz(value) -> str:
        if value == 3:
            return "Fizz"
        return str(value)

With small changes to the production code, we are back in `GREEN` phase

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED

Anything to refactor after that? Nothiong for now.

Let's get to the fifth use case, similar to the fourth use case

    # case 5: return "Buzz" when 5 passed in
    def test_return_Buzz_when_5_passed_in():
        assert checkFizzBuzz(5, "Buzz")

As expected with the addition new unit test function we are back in the `RED` phase

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in FAILED

Time to update the production code to get into `GREEN` phase

    # production code
    def fizzBuzz(value) -> str:
        if value == 3:
            return "Fizz"
        if value == 5:
            return "Buzz"
        return str(value)

That was easy change, we are in `GREEN` now.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    
Anything to refactor now? Nothing for now.

Now we will add the sixth use case to the unit test code.

    # case 6: return "Fizz" when 6 passed in (a multiple of 3)
    def test_return_Fizz_when_6_passed_in():
        assert checkFizzBuzz(6, "Fizz")

We are again in `RED` phase as shown below        

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in FAILED

Time to modify production code to get in the `GREEN` phase.

Just one line change, from `if value == 3:` to `if value % 3 == 0:`

    # production code
    def fizzBuzz(value) -> str:
        if value % 3 == 0:
            return "Fizz"
        if value == 5:
            return "Buzz"
        return str(value)

One line change in the production code got us into the `GREEN` phase

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED

Let us work on the 7th use case.

    # case 7: return "Buzz" when 10 passed in (a multiple of 5)
    def test_return_Buzz_when_10_passed_in():
        assert checkFizzBuzz(10, "Buzz") 

We are back in the `RED` phase

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in FAILED

Let quickly update the production code to get the test pass.

Just one line change, from `if value == 5:` to `if value % 5 == 0:` same as before

    # production code
    def fizzBuzz(value) -> str:
        if value % 3 == 0:
            return "Fizz"
        if value % 5 == 0:
            return "Buzz"
        return str(value)

Again with one line change, we are in the `GREEN` phase now.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in PASSED

We have a duplicate production code, lets get in the `REFACTOR` phase and clean the code.

We will define new function `def isMultiple()` as below:

    def isMultiple(value, mod) -> bool:
        return (value % mod) == 0

Let's use this in the production code.
 
    def fizzBuzz(value) -> str:
        if isMultiple(value, 3):
            return "Fizz"
        if isMultiple(value, 5):
            return "Buzz"
        return str(value)

After code refactor, all the test still passed.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in PASSED

Last use case to deal with now.

    # case 8: return "FizzBuzz" when 15 passed in (a multiple of 3 and 5)
    def test_return_FizzBuzz_when_15_passed_in():
        assert checkFizzBuzz(15, "FizzBuzz")

With the new unit test, we are in the `RED` phase

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in PASSED
    test_fizzbuzz.py::test_return_FizzBuzz_when_15_passed_in FAILED

Time to update the production code to make the test pass.

    def fizzBuzz(value) -> str:
        if isMultiple(value, 3):
            if isMultiple(value, 5):
                return "FizzBuzz"
            return "Fizz"
        if isMultiple(value, 5):
            return "Buzz"
        return str(value)

Finally we have all test passed and nothing to refactor too.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in PASSED
    test_fizzbuzz.py::test_return_FizzBuzz_when_15_passed_in PASSED

The complete solution looks like this after the exercise.

    # production code
    def isMultiple(value, mod) -> bool:
        return (value % mod) == 0

    def fizzBuzz(value) -> str:
        if isMultiple(value, 3):
            if isMultiple(value, 5):
                return "FizzBuzz"
            return "Fizz"
        if isMultiple(value, 5):
            return "Buzz"
        return str(value)

    # unit test code
    import pytest

    def checkFizzBuzz(value, expectedValue) -> bool:
        retVal = fizzBuzz(value)
        return retVal == expectedValue

    # case 1: can call fzzBuzz()?
    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        assert checkFizzBuzz(1, "1")

    # case 3: return "2" when 2 passed in
    def test_return_2_when_2_passed_in():
        assert checkFizzBuzz(2, "2")

    # case 4: return "Fizz" when 3 passed in
    def test_return_Fizz_when_3_passed_in():
        assert checkFizzBuzz(3, "Fizz")   

    # case 5: return "Buzz" when 5 passed in
    def test_return_Buzz_when_5_passed_in():
        assert checkFizzBuzz(5, "Buzz")      

    # case 6: return "Fizz" when 6 passed in (a multiple of 3)
    def test_return_Fizz_when_6_passed_in():
        assert checkFizzBuzz(6, "Fizz")

    # case 7: return "Buzz" when 10 passed in (a multiple of 5)
    def test_return_Buzz_when_10_passed_in():
        assert checkFizzBuzz(10, "Buzz") 

    # case 8: return "FizzBuzz" when 15 passed in (a multiple of 3 and 5)
    def test_return_FizzBuzz_when_15_passed_in():
        assert checkFizzBuzz(15, "FizzBuzz")        

Having done the unit testing using the standard module `pytest`, I wanted to try something where I can create unit test in a class.

For that, I am using another module `unittest` and here is the complete `FizzBuzz` solution.

    # production code
    def isMultiple(value, mod) -> bool:
        return (value % mod) == 0

    def fizzBuzz(value) -> str:
        if isMultiple(value, 3):
            if isMultiple(value, 5):
                return "FizzBuzz"
            return "Fizz"
        if isMultiple(value, 5):
            return "Buzz"
        return str(value)

    # unit test code
    import unittest

    def checkFizzBuzz(value, expectedRetVal) -> bool:
        retVal = fizzBuzz(value)
        return retVal == expectedRetVal

    class TestFizzBuzz(unittest.TestCase):
        # case 1: can call fzzBuzz()?
        # case 2: return "1" when 1 passed in
        def test_return_1_when_1_passed_in(self):
            self.assertTrue(checkFizzBuzz(1, "1"))

        # case 3: return "2" when 2 passed in
        def test_return_2_when_2_passed_in(self):
            self.assertTrue(checkFizzBuzz(2, "2"))

        # case 4: return "Fizz" when 3 passed in
        def test_return_Fizz_when_3_passed_in(self):
            self.assertTrue(checkFizzBuzz(3, "Fizz"))

        # case 5: return "Buzz" when 5 passed in
        def test_return_Buzz_when_5_passed_in(self):
            self.assertTrue(checkFizzBuzz(5, "Buzz"))

         # case 6: return "Fizz" when 6 passed in (a multiple of 3)
        def test_return_Fizz_when_6_passed_in(self):
            self.assertTrue(checkFizzBuzz(6, "Fizz"))

        # case 7: return "Buzz" when 10 passed in (a multiple of 5)
        def test_return_Buzz_when_10_passed_in(self):
            self.assertTrue(checkFizzBuzz(10, "Buzz"))

        # case 8: return "FizzBuzz" when 15 passed in (a multiple of 3 and 5)
        def test_return_FizzBuzz_when_15_passed_in(self):
            self.assertTrue(checkFizzBuzz(15, "FizzBuzz"))

    unittest.main()

## XUnit
***

`Python` provides `XUnit` styled setup/teardonw functions that get executed before and after.

    module: setup_module() / teardown_module()
    function: setup_function() / teardown_function()
    class: setup_class() / teardown_class() / setup_method() / teardown_method()

Let us see in action and create a file named `test_xunit.py`

    import pytest

    def test_1():
        print("executing test_1")
        assert True

    def test_2():
        print("executing test_2")
        assert True   

We will first try `setup_function()` and `teardown_function()` as below:

    def setup_function(function):
        if function == test_1:
            print("setup test_1")
        elif function == test_2:
            print("setup test_2")
        else:
            print("setup unknown")

    def teardown_function(function):
        if function == test_1:
            print("teardown test_1")
        elif function == test_2:
            print("teardown test_2")
        else:
            print("teardown unknown")

The above `setup_function()` and `teardown_function()` gets executed for each unit test function.

Let's check the result by using the command `pytest -v -s`. The `-v` switch we used earlier also is for running test in `verbose` mode. And the `-s` swith is to allow dump print to the console.

      test_xunit.py::test_1 
      setup test_1
      executing test_1
      PASSED
      teardown test_1

      test_xunit.py::test_2
      setup test_2
      executing test_2
      PASSED
      teardown test_2

What if we want similar function but one for `module`      

    def setup_module():
        print("setup module")

     def teardown_module():
        print("teardown module")      

Let see what happens now

      test_xunit.py::test_1
      setup module
      setup test_1
      executing test_1
      PASSED
      teardown test_1

      test_xunit.py::test_2
      setup test_2
      executing test_2
      PASSED
      teardown test_2
      teardown module

Did you notice, `setup_module()` executed only once before the first test and `teardown_module()` gets executed only once at the end of last test?

Now the fun starts with class level setup and teardown.

We will re-use the above code and change it to class.

    import pytest

    class TestClass():
        @classmethod
        def setup_class(cls):
            print("setup TestClass")

        @classmethod
        def teardown_class(cls):
            print("teardown TestClass")

        def setup_method(self, method):
            if method == self.test_1:
                print("setup test_1")
            elif method == self.test_2:
                print("setup test_2")
            else:
                print("setup unknown")

        def teardown_method(self, method):
            if method == self.test_1:
                print("teardown test_1")
            elif method == self.test_2:
                print("teardown test_2")
            else:
                print("teardown unknown")
                
        def test_1(self):
            print("executing test_1")
            assert True

        def test_2(self):
            print("executing test_2")
            assert True   

After running the command `pytest -v -s` we get this

    test_xunit.py::TestClass::test_1 
    setup TestClass
    setup test_1
    executing test 1
    PASSED
    teardown test_1

    test_xunit.py::TestClass::test_2 
    setup test_2
    executing test 2
    PASSED
    teardown test_2
    teardown TestClass

As you see `setup_class()` and `teardown_class()` only executed once. But `setup_method()` and `teardown_method()` got executed once for each method in the class.

