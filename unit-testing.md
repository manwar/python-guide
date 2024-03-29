## Unit Testing
***
- [Overview](#overview)
- [FizzBuzz Example](#fizzbuzz-example)
- [XUnit](#xunit)
- [Test Fixtures](#test-fixtures)
- [Data Comparison](#data-comparison)
- [Exceptions](#exceptions)
- [PyTest CLI](#pytest-cli)
- [Test Doubles](#test-doubles)
- [Mock Example](#mock-example)

**DISCLAIMER:** These are my notes after attending the course [**Unit Testing and Test Driven Development in Python**](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python).

## Overview
***

Levels of Testing

    a) Unit Testing       : Testing at the function level
    b) Component Testing  : Testing is at the library and compiled binary level
    c) System Testing     : Tests the external interface of a system
    d) Performance Testing: Testing at system level to verify timing and resource usages.

**Test Driven Development (TDD)** expects us to do the followings:

    a) Write unit test before any production code
    b) DO NOT write all unit test or production code at once.
    c) Test and production code are written for one use case at a time

**TDD** follows 3 phases:

    1) RED     : Write a failing unit test
    2) GREEN   : Write just ENOUGH production code to make test pass
    3) REFACTOR: Clean up and remove duplicate code from unit test and production code

Repeat the cycle until you have covered all the use cases.

The **THREE** laws of **TDD**

    1) Do not write any production code until you have written a failing test
    2) Do not write more than the needed unit test to fail
    3) Do not write more than the needed production code to pass the test
     
`pytest` automatically discovers test based on standard naming conventions.

    1) Test function name should start with 'test'
    2) Class with test should have class name start with 'Test' and do not have __init__() method
    3) Filename should start or end with 'test'

Suppose in the current folder we have only 3 files as below:

    1) test_file.py
    2) file_test.py
    3) ignore-me.py

They all have the following lines of code.

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

We will now create another file `test_class.py` as below in the same folder.

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

Let us apply what we learnt so far in the `FizzBuzz` example. First we will create file named `test_fizzbuzz.py`.

    # production code

    # unit test code
    import pytest

    # case 1: can call fizzBuzz()
    def test_can_call_fizzBuzz():
        fizzBuzz(1)

We just entered the `RED` phase by creating the first failed unit test as shown below

    test_fizzbuzz.py::test_can_call_fizzBuzz FAILED

Now time to write enough production code to get into `GREEN` phase.

    # production code
    def fizzBuzz(value):
        return

We are now in `GREEN` phase after completing the production code enough to pass the test.

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED

We now have passed unit test. Time to get into `REFACTOR` phase if needed.

Do we need it? I don't think so.

So we will repeat the cycle and get into the `RED` phase again by creating another fail test.

    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert(retVal == "1")

We are in `RED` phase as shown below:

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in FAILED
    
Let's update the production code to make the test pass.

    # production code
    def fizzBuzz(value) -> str:
        return "1"

We are in `GREEN` phase now.

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED

Want to do some code refactor? 

We can clearly see some code duplication now. The method `fizzBuzz()` is called twice, first in `def test_can_call_fizzBuzz()` and then again `def test_return_1_when_1_passed_in()`.  

Let's clean up the code and merged the two use cases into one as below:

    # unit test code
    import pytest

    # case 1: can call fizzBuzz()
    # case 2: return "1" when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert retVal == "1"

The test method `test_return_1_when_1_passed_in()` covered both use cases. The test still pass after refactor as shown here:

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

First we will create function `checkFizzBuzz()` as below:

    def checkFizzBuzz(value, expectedValue) -> bool:
        retVal = fizzBuzz(value)
        return retVal == expectedValue

Then update the unit test to use it

    # case 1: can call fizzBuzz()
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

Time to update the production code to get into `GREEN` phase.

    # production code
    def fizzBuzz(value) -> str:
        if value == 3:          # Line added
            return "Fizz"       # Line added
        return str(value)

With small changes to the production code, we are back in `GREEN` phase.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED

Anything to refactor after that? Nothing for now.

Let's get to the fifth use case, similar to the fourth use case.

    # case 5: return "Buzz" when 5 passed in
    def test_return_Buzz_when_5_passed_in():
        assert checkFizzBuzz(5, "Buzz")

As expected with the addition new unit test function we are back in the `RED` phase.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in FAILED

Time to update the production code to get into `GREEN` phase.

    # production code
    def fizzBuzz(value) -> str:
        if value == 3:
            return "Fizz"
        if value == 5:          # Line added
            return "Buzz"       # Line added
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

We are again in `RED` phase as shown below:      

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

One line change in the production code got us into the `GREEN` phase.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED

Let us work on the 7th use case.

    # case 7: return "Buzz" when 10 passed in (a multiple of 5)
    def test_return_Buzz_when_10_passed_in():
        assert checkFizzBuzz(10, "Buzz") 

We are back in the `RED` phase.

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
    test_fizzbuzz.py::test_return_2_when_2_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_3_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_5_passed_in PASSED
    test_fizzbuzz.py::test_return_Fizz_when_6_passed_in PASSED
    test_fizzbuzz.py::test_return_Buzz_when_10_passed_in FAILED

Let quickly update the production code to get the test pass.

Just one line change, from `if value == 5:` to `if value % 5 == 0:` same as before.

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

We will define new function `isMultiple()` as below:

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

With the new unit test, we are in the `RED` phase.

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

    # case 1: can call fizzBuzz()
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
        # case 1: can call fizzBuzz()
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

`Python` provides `XUnit` styled setup/teardown functions that get executed before and after.

    module  : setup_module(), teardown_module()
    function: setup_function(), teardown_function()
    class   : setup_class(), teardown_class(), setup_method(), teardown_method()

Let us see in action and create a file named `test_xunit.py`.

    # test_xunit.py
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
            print("\nsetup test_1")
        elif function == test_2:
            print("\nsetup test_2")
        else:
            print("\nsetup unknown")

    def teardown_function(function):
        if function == test_1:
            print("\nteardown test_1")
        elif function == test_2:
            print("\nteardown test_2")
        else:
            print("\nteardown unknown")

The above `setup_function()` and `teardown_function()` gets executed for each unit test function.

Let's check the result by using the command `pytest -v -s`. 

The `-v` switch we used earlier also is for running test in `verbose` mode. 

And the `-s` switch is to allow dump print to the console.

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

What if we want similar function but for `module`.

    def setup_module():
        print("\nsetup module")

     def teardown_module():
        print("\nteardown module")      

Let's see what happens now.

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

    # test_xunit.py
    import pytest

    class TestClass():
        @classmethod
        def setup_class(cls):
            print("\nsetup TestClass")

        @classmethod
        def teardown_class(cls):
            print("\nteardown TestClass")

        def setup_method(self, method):
            if method == self.test_1:
                print("\nsetup test_1")
            elif method == self.test_2:
                print("\nsetup test_2")
            else:
                print("\nsetup unknown")

        def teardown_method(self, method):
            if method == self.test_1:
                print("\nteardown test_1")
            elif method == self.test_2:
                print("\nteardown test_2")
            else:
                print("\nteardown unknown")
                
        def test_1(self):
            print("executing test_1")
            assert True

        def test_2(self):
            print("executing test_2")
            assert True   

After running the command `pytest -v -s` we get this:

    test_xunit.py::TestClass::test_1 
    setup TestClass
    
    setup test_1
    executing test_1
    PASSED
    teardown test_1

    test_xunit.py::TestClass::test_2 
    setup test_2
    executing test_2  
    PASSED
    teardown test_2
    
    teardown TestClass

As you see `setup_class()` and `teardown_class()` only executed once. But `setup_method()` and `teardown_method()` got executed once for each method in the class.

## Test Fixtures
***

Test fixtures allow for re-use of setup and teardown code across tests.

Let's start with the basic unit test in a file named `test_fixtures.py`.

    # test_fixtures.py
    import pytest

    @pytest.fixture()
    def setup():
        print("\nsetup test")

    def test_1():
        print("\nexecuting test_1")
        assert True

    def test_2():
        print("\nexecuting test_2")
        assert True

It is exactly the same code we used before except we added function `setup()` with decorator `@pytest.fixture()`.

    test_fixtures.py::test_1 
    executing test_1
    PASSED
    test_fixtures.py::test_2 
    executing test_2
    PASSED

If you noticed `setup()` didn't get executed. Let's configure unit test `test_1()` to execute the test fixture `setup()`.

    def test_1(setup):
        print("executing test_1")
        assert True

You now see this when you run the test. The fixture `setup()` is executed before `test_1()` only.

    test_fixtures.py::test_1 
    setup test
    executing test_1
    PASSED
    test_fixtures.py::test_2 
    executing test_2
    PASSED

There is another way you can use test fixture using the decorator `@pytest.mark.usefixtures()` as we see below:

    @pytest.mark.usefixtures("setup")
    def test_2():
        print("\nexecuting test_2")
        assert True

You now see `setup()` gets execute before both unit tests.

    test_fixtures.py::test_1 
    setup test
    executing test_1
    PASSED
    test_fixtures.py::test_2 
    setup test    
    executing test_2
    PASSED

If we want test fixture to be used before each unit test then it is a big job to change each unit test.

There is shortcut to that issue like below:

    @pytest.fixture(autouse=True)
    def setup():
        print("\nsetup test")

Then you don't need to do anything to your unit test.

    def test_1():
        print("executing test_1")
        assert True

    def test_2():
        print("executing test_2")
        assert True

Here is the result:

    test_fixtures.py::test_1 
    setup test
    executing test_1
    PASSED
    test_fixtures.py::test_2 
    setup test    
    executing test_2
    PASSED

Test fixture can also have their own optional teardown code which is called after a fixture goes out of scope.

There are two methods to specify teardown code.

    1) yield keyword
    2) request-context object's addfinalizer method

The `yield` keyword is a replacement for the `return` keyword so any return values are also specified in the `yield` statement.

    @pytest.fixture()
    def setup():
        print("\nsetup test")
        yield
        print("\teardown!")

Here is outcome:

    test_fixtures.py::test_1
    setup test
    executing test_1
    PASSED
    teardown!

    test_fixtures.py::test_2
    setup test
    executing test_2
    PASSED
    teardown!

With the `addfinalizer()` method a teardown method is defined added via the `request.context`'s addfinalizer method.

Multiple finalization functions can be specified.

    @pytest.fixture()
    def setup2(request):
        print("\nsetup 2")

        def teardown_a():
            print("\nteardown A")

        def teardown_b():
            print("\nteardown B")

        request.addfinalizer(teardown_a)
        request.addfinalizer(teardown_b)

Updated the following two unit tests, one uses `setup()` and other uses `setup2()` test fixture.

    def test_1(setup):
        print("executing test_1")
        assert True

    def test_2(setup2):
        print("executing test_2")
        assert True   

Time for some result.

    test_fixtures.py::test_1 
    setup test
    executing test_1
    PASSED
    teardown!
    
    test_fixtures.py::test_2 
    setup 2  
    executing test_2
    PASSED
    teardown B!
    teardown A!

Test fixtures Scope

    1) Function - Run the fixture once for each test
    2) Class    - Run the fixture once for each class of tests
    3) Module   - Run once the module goes in scope
    4) Session  - The fixture is run whey pytest starts

Let us see in action, we would create two modules, say `test_fixture.py` and `test_fixture2.py`.

Below is the content of `test_fixture.py`:

    # test_fixture.py
    import pytest

    @pytest.fixture(scope="session", autouse=True)
    def setup_session():
        print("\nsetup session")

    @pytest.fixture(scope="module", autouse=True)
    def setup_module():
        print("\nsetup module")

    @pytest.fixture(scope="function", autouse=True)
    def setup_function():
        print("\nsetup function")

    def test_1():
        print("\nexecuting test_1")
        assert True

    def test_2():
        print("\nexecuting test_2")
        assert True

Below is the content of `test_fixture2.py`.

    # test_fixture2.py
    import pytest

    @pytest.fixture(scope="module", autouse=True)
    def setup_module():
        print("\nsetup module")

    @pytest.fixture(scope="class", autouse=True)
    def setup_class():
        print("\nsetup class")

    @pytest.fixture(scope="function", autouse=True)
    def setup_function():
        print("\nsetup function")

    class TestClass:
        def test_1(self):
            print("\nexecuting test_1")
            assert True

        def test_2(self):
            print("\nexecuting test_2")
            assert True

Testing the fixtures by command `pytest -s`.

      test_fixture.py
      setup session

      setup module

      setup function
      executing test_1
      .
      setup function
      executing test_2
      .
      test_fixture2.py
      setup module

      setup class

      setup function
      executing test_1
      .
      setup function
      executing test_2
      .

Test fixtures can optionally return data which can be used in the test. 

The optional `"params"` array argument in the fixture decorator can be used to specify the data returned to the test.

When a `"params"` argument is specified then the test will be called one time with each value specified.

We will show the use in the example below:

    # test_fixture.py
    import pytest
    
    @pytest.fixture(params = [1,2,3)
    def setup(request):
        retVal = request.param
        print("\nSetup: retVal = {}".format(retVal))
        return retVal

    def test_1(setup):
        print("\nsetup = {}".format(setup))
        assert True

Checkout the result as below:

    test_fixture.py
    Setup: retVal = 1

    setup = 1
    .    
    Setup: retVal = 2

    setup = 2
    .
    Setup: retVal = 3

    setup = 3
    .

## Data Comparison
***    

`Python` assert statements can be used for data verification in unit test. All Python data can be compared using the standard operators, `>`, `<`, `==`, `>=`, `<=` and `!=`. 

**Example:**

    from pytest import approx

    def test_int_assert():
        assert 1 == 1
    def test_str_assert()
        assert "a" == "a"
    def test_float_assert()
        assert 1.0 == 1.0
    def test_array_assert()
        assert [1,2,3] == [1,2,3]
    def test_dict_assert()
        assert {"1": 1} == {"1": 1}

**NOTE**: Be careful comparing floating point values.

    def test_bad_float_values()
        assert (0.1 + 0.2) == 0.3

The above test would `FAIL`.

`pytest` provIdes `approx()` function to deal with the issue.

    def test_good_float_values()
        assert (0.1 + 0.2) == approx(0.3)
      
## Exceptions
***  

Python provides the `raises` helper to verify exception using the `with` keyword.

    # test_exceptions.py
    from pytest import raises

    def testValueException():
        raise ValueError

    def test_exception():
        with raises(ValueError):
            raiseValueException()

Test the code now by command `pytest -v`.

    test_exceptions.py::test_exception PASSED

## PyTest CLI
***

By default `pytest` automatically discovers all unit test following the standard naming convention.

But there are many command line arguments for controlling which discovered tests actually are executed.

    1) modulename     : Simply specify the module name to run only tests from the module.
    2) directoryname  : Runs any tests found in the specified directory.
    3) -k "expression": It can include module name, class name or function name.
    4) -m "expression": It matches tests that have `pytest.mark` decorator. 

Some other useful command line arguments are:

    -v       : runs the test in verbose mode
    -q       : runs the test in quiet mode
    -s       : show print statements on the console
    --ignore : specfiy the directory path to ignore when discovery tests
    --maxfail: specify the maximum fails before the test stops
    
Let's do some test run. For that we created 3 modules as below:

## test_file_1.py

    # test_file_1.py
    import pytest

    def test_1():
        print("\nTest 1")
        assert True

## test_file_2.py

    # test_file_2.py
    import pytest

    def test_2():
        print("\nTest 2")
        assert True

## testsubdirectory/test_file_3.py

    # testsubdirectory/test_file_3.py
    import pytest

    def test_3():
        print("\nTest 3")
        assert True        

Running the command `pytest -v -s` shows this:

    test_file_1.py::test_1
    Test 1
    PASSED
    test_file_2.py::test_2
    Test 2
    PASSED
    testsubdirectory/test_file_3.py::test_3
    Test 3
    PASSED

Now if we want to run the `test_file_1.py` module only then we would do something like below:

    pytest -v -s test_file_1.py

    test_file_1.py::test_1
    Test 1
    PASSED

As you see, it only executed tests in the specified module `test_file_1.py`.

What if I want to run only tests found in a specified directory?

    pytest -v -s testsubdirectory/

    testsubdirectory/test_file_3.py::test_3
    Test 3
    PASSED

Let's try `-k` parameter. Here we want to run only test named `test_2`.

    pytest -v -s -k "test_2"

    test_file_2.py::test_2
    Test 2
    PASSED

If we want to run test named  `"test_2"` or `"test_3"`.

    pytest -v -s -k "test_2 or test_3"

    test_file_2.py::test_2
    Test 2
    PASSED
    testsubdirectory/test_file_3.py::test_3
    Test 3
    PASSED    

Now we wlll try `-m` command line argument. For this we need to add the decorator `@pytest.mark`.

For demo purpose, we would only mark `test_1` and `test_3` as below:

    # test_file_1.py
    import pytest

    @pytest.mark.test_1
    def test_1():
        print("\nTest 1")
        assert True

    # testsubdirectory/test_file_3.py
    import pytest

    @pytest.mark.test_3
    def test_3():
        print("\nTest 3")
        assert True

We are ready to try the `-m` switch as below:

    pytest -v -s -m "test_2 or test_3"

    test_file_1.py::test_1
    Test 1
    PASSED
    testsubdirectory/test_file_3.py::test_3
    Test 3
    PASSED    

## Test Doubles
***

Test doubles are objects that are used in unit tests as replacements to the real production systems.

Types of Test Doubles:

    1) Dummy - Objects that can be passed around as necessary but do not have any type of test implementation
    2) Fake  - These object generally have a simplified functional implementation for testing only
    3) Stub  - These object provide implementations with canned answers that are suitable for the test
    4) Spies - These object provide implementations that record the value that were passed in so they can be used in the test
    5) Mock  - These objects are pre-programmed to expect specific calls and parameters

`Python` provides mocking framework called `unittest.mock`.

Mock provides many initialization parameters that can be used to control the mock behaviour.

    1) The `spec` parameter specifies the interface that Mock object is implementing
    2) The `side_effect` parameter specifies a function that should be called when the mock is called
    3) The `return_value` parameter specifies the return value when the mock is called

Mock verification:

    1) assert_called           - Assert the mock was called
    2) assert_called_once      - Assert the mock was called once
    3) assert_called_with      - Assert the last call to the mock was with the specified parameters
    4) assert_called_once_with - Assert the mock was called once with the specified parameters
    5) assert_any_call         - Assert the mock was ever called with the specified parameters
    6) assert_not_called       - Assert the mock was not called

Mock provides additional attributes for verification:

    1) assert_has_calls - Assert the mock was called with the list of calls
    2) called           - A boolean value indicating if the mock was ever called
    3) call_count       - An integer value representing the number of times the mock object was called
    4) call_args        - The arguments the mock was last called with
    5) call_args_list   - A list containing the arguments that were used for each call to the mock

The `unittest.mock` also provides `MagicMock` class and it is derived from `Mock` class and provides a default implementation of many of the default magic methods. For example `__str__`. However there are some not implemented by default, like `__getattr__`, `__setattr__`, `__init__`, `__new__`, `__prepare__`, `__instancecheck__`, `__subclascheck__` and `__del__`.

`pytest` provides the `monekypatch` test fixture to allow a test to dynamically replace the followings:

    1) module and class attributes
    2) dictionary entries
    3) environment variables

## Mock Example
***

Let's try to show how `MagicMock` works. For this we would create a module `LineReader.py` and unit test `test_mock.py`.

Following the **TDD** rules, we will create a test and get into `RED` phase.

    # test_mock.py
    import pytest

    # case 1: can call readFromFile()
    def test_can_call_readFromFile():
        readFromFile("blah")

We get failed test as expected.

    test_mock.py::test_can_call_readFromFile FAILED
    
Now we will write enough production to pass the unit test.

    # LineReader.py
    def readFromFile(filename):
        pass

With this, we now import the function `readFromFile()` from the module `LineReader` in unit test.

    # test_mock.py
    import pytest
    from LineReader import readFromFile

    # case 1: can call readFromFile()
    def test_can_call_readFromFile():
        readFromFile("blah")

The test now **PASSED** with the above changes.

    test_mock.py::test_can_call_readFromFile PASSED

Now we will add another test case as below and also import `MagicMock` at the top i.e. `from unittest.mock import MagicMock`.

    # case 2 readFromFile returns correct string
    def test_return_correct_string(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

Now we have failed test again as expected.

    test_mock.py::test_can_call_readFromFile PASSED
    test_mock.py::test_return_correct_string FAILED
   
To get into `GREEN` phase, lets update production code

    # LineReader.py
    def readFromFile(filename):
        infile = open(filename, "r")
        line = infile.readline()
        return line

This now passed the newly added test `test_return_correct_string()` but made the first test `test_can_call_readFromFile()` failed.

    test_mock.py::test_can_call_readFromFile FAILED
    test_mock.py::test_return_correct_string PASSED
    
If you noticed the first unit test `test_can_call_readFromFile()` no longer needed as we already cover that case in the second unit test.

Let's clean up the unit test.

    # test_mock.py
    import pytest
    from unittest.mock import MagicMock
    from LineReader import readFromFile

    # case 1: can call readFromFile()
    # case 2: readFromFile returns correct string
    def test_return_correct_string(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

Now we are good to go as test passed.

    test_mock.py::test_return_correct_string PASSED

Finally let us get the last use case defined and import function `raises()`.

    # test_mock.py
    import pytest
    from pytest import raises
    from unittest.mock import MagicMock
    from LineReader import readFromFile

    # case 1: can call readFromFile()
    # case 2: readFromFile returns correct string
    def test_return_correct_string(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    # case 3: readFromFile throws exception when file doesn't exist
    def test_throwsException(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exists = MagicMock(return_value = False)
        monkeypatch.setattr("os.path.exists", mock_exists)
        with raises(Exception):
            result = readFromFile("blah")

As expected. we have a failed test.

    test_mock.py::test_return_correct_string PASSED
    test_mock.py::test_throws_exception_with_bad_file FAILED

Get the production code raise exception when file doesn't exist.

    # LineReader.py
    import os
    def readFromFile(filename):
        if not os.path.exists(filename):
            raise Exception("Bad File")
        infile = open(filename, "r")
        line = infile.readline()
        return line

This now made the first test **FAILED** now as below:

    test_mock.py::test_return_correct_string FAILED
    test_mock.py::test_throws_exception_with_bad_file PASSED

We would need to update `test_return_correct_string()` to handle the file exists case as production code now checks that.

    # case 1: can call readFromFile()
    # case 2: readFromFile returns correct string
    def test_return_correct_string(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exists = MagicMock(return_value = True)             # Line added
        monkeypatch.setattr("os.path.exists", mock_exists)       # Line added
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

Finally we have both tests passed.

    test_mock.py::test_return_correct_string PASSED
    test_mock.py::test_throws_exception_with_bad_file PASSED

Anything to refactor now?

Yes. plenty of scope. We see lots of code repetition. We will use `fixture` to clean up the unit test.

    @pytest.fixture()
    def mock_open(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "test line")
        mock_open = MagicMock(return_value = mock_file)#
        monkeypatch.setattr("builtins.open", mock_open)
        return mock_open

With the test fixture `mock_open()` we will now update both the unit tests to use it.

    # case 1: can call readFromFile()
    # case 2: readFromFile returns correct string
    def test_return_correct_string(mock_open, monkeypatch):
        mock_exists = MagicMock(return_value = True)
        monkeypatch.setattr("os.path.exists", mock_exists)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    # case 3: readFromFile throws exception when file doesn't exist
    def test_throwsException(mock_open, monkeypatch):
        mock_exists = MagicMock(return_value = False)
        monkeypatch.setattr("os.path.exists", mock_exists)
        with raises(Exception):
            result = readFromFile("blah")

After code refactor, we still have both tests passed.

    test_mock.py::test_return_correct_string PASSED
    test_mock.py::test_throws_exception_with_bad_file PASSED
