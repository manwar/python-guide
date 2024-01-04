## Unit Testing
***
- [Overview](#overview)
- [FizzBuzz Example](#fizzbuzz-example)

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

`TDD` follows 3 phases:

  1) **RED**: Write a failing unit test
  2) **GREEN**: Write just `ENOUGH` production code to make test pass
  3) **REFACTOR**: clean up and remove duplicate code from unit test and production code

Repeat the cycle until you have covered all the use cases.

The `THREE` laws of `TDD`

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
    def test_cancallFizzBuzz():
        fizzBuzz(1)

We just entered the `RED` phase by creating the first fail unit test as shown below

    test_fizzbuzz.py::test_canCallFizzBuzz FAILED

Now time to write enough production code to get into `GREEN` phase.

    # production code
    def fizzBuzz(value):
        return

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    def test_can_call_fizzBuzz():
        fizzBuzz(1)

We are now in `GREEN` phase after completing the production enough to pass the test

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED

We now have pass unit test. Time to get into `REFACTOR` phase if needed.

Do we need it? I don't think so.

So we will repeat the cycle and get into the `RED` phase again by creating another fail test.

    # production code
    def fizzBuzz(value):
        return

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    def test_can_call_fizzBuzz():
        fizzBuzz(1)

    # case 2: return 1 when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert(retVal == 1)

We are in `RED` phase as shown below

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in FAILED
    
Let's update the production code to make the test pass

    # production code
    def fizzBuzz(value) -> str:
        return "1"

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    def test_can_call_fizzBuzz():
        fizzBuzz(1)

    # case 2: return 1 when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert retVal == "1"

We are in `GREEN` phase now.

    test_fizzbuzz.py::test_can_call_fizzBuzz PASSED
    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED

To do some refactor? 

We can clearly see some code duplication now. The method `fizzBuzz()` is called twice. Let's clean up the code.

    # production code
    def fizzBuzz(value) -> str:
        return "1"

    # unit test code
    import pytest

    # case 1: can call fzzBuzz()?
    # case 2: return 1 when 1 passed in
    def test_return_1_when_1_passed_in():
        retVal = fizzBuzz(1)
        assert retVal == "1"

The test method `test_return_1_when_1_passed_in()` covered both use cases. The test still pass after refactor as shown here

    test_fizzbuzz.py::test_return_1_when_1_passed_in PASSED
