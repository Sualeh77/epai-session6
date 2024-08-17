import re
import inspect
import os

import session6 as s6

def test_closure_dockstring_check1():
    # Test1
    assert s6.closure_dockstring_check(s6.dock_string_check, 50), "The dockstring is either not set or it has less than 50 characters in it"

def test_closure_dockstring_check2():
    # Test2
    s6.dock_string_check.__doc__ = s6.dock_string_check.__doc__[0:49] # Cahnging dockstring of the function to have less than 50 chars
    assert s6.closure_dockstring_check(s6.dock_string_check, 50), "The dockstring is either not set or it has less than 50 characters in it"

def test_closure_dockstring_check3():    
    # Test3
    s6.dock_string_check.__doc__ = "" # Cahnging dockstring of the function to blank string (0 chars)
    assert s6.closure_dockstring_check(s6.dock_string_check, 50), "The dockstring is either not set or it has less than 50 characters in it"

def test_closure_dockstring_check4():    
    # Test4
    s6.dock_string_check.__doc__ = None # Cahnging dockstring of the function to None
    assert s6.closure_dockstring_check(s6.dock_string_check, 50), "The dockstring is either not set or it has less than 50 characters in it"

# fibonaci series: 1,1,2,3,5,8,13,21,34,55......
def test_fibonaci_check1():
    # Test5
    fib = s6.fibonaci()
    assert fib(7) == 21, "Fibonaci number is incorrect"

def test_fibonaci_check2():
    # Test6
    fib = s6.fibonaci()
    assert fib(0) == 1, "Fibonaci number is incorrect"

# Test function call counter
counters = dict()
def test_fn_call_counter_check1():
    #Test7
    @s6.counter_factory(counters)
    def add(a, b):
        return a + b
    assert add(1,3) == 4, "Addition is not working properly"
    assert counters[add.__name__] == 1

def test_fn_call_counter_check2():
    # Test8
    @s6.counter_factory(counters)
    def add(a, b):
        return a + b
    assert add(11,35) == 46, "Addition is not working properly"
    assert counters[add.__name__] == 2

def test_fn_call_counter_check3():
    # Test9
    @s6.counter_factory(counters)
    def mult(a, b, c):
        return a * b * c
    assert mult(1, 2, 3) == 6, "Mulitplication is not working properly"
    assert counters[mult.__name__] == 1

def test_fn_call_counter_check4():
    # Test10
    @s6.counter_factory(counters)
    def mult(a, b, c):
        return a * b * c
    assert mult(4, 2, 8) == 64, "Mulitplication is not working properly"
    assert counters[mult.__name__] == 2

def test_fn_call_counter_check5():
    # Test11
    @s6.counter_factory(counters)
    def div(a ,b):
        if b==0:
            return "Hey, are you trying to divide by 0"
        return a/b
    assert div(5, 0) == "Hey, are you trying to divide by 0", "Division is not working properly"
    assert counters[div.__name__] == 1

def test_fn_call_counter_check6():
    # Test12
    @s6.counter_factory(counters)
    def div(a ,b):
        if b==0:
            return "Hey, are you trying to divide by 0"
        return a/b
    assert div(10, 2) == 5, "division is not working properly"
    assert counters[div.__name__] == 2


# Test modified counter function that takes dictionary and update it's values
counters_instance1 = dict()
counters_instance2 = dict()
def test_counter_factory_dict1_check1():
    # Test13
    @s6.counter_factory(counters_instance1)
    def add(a, b):
        return a + b
    assert add(1,2) == 3, "Addition is not working properly"
    assert counters_instance1[add.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"

def test_counter_factory_dict1_check2():
    # Test14
    @s6.counter_factory(counters_instance1)
    def mult(a, b, c):
        return a * b * c
    assert mult(1,2,3) == 6, "Multiplication is not working properly"
    assert counters_instance1[mult.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"

def test_counter_factory_dict1_check3():  
    # Test15  
    @s6.counter_factory(counters_instance1)
    def div(a ,b):
        if b==0:
            return "Hey, are you trying to divide by 0"
        return a/b
    assert div(8, 4) == 2, "Division is not working properly"
    assert counters_instance1[div.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"
    
def test_counter_factory_dict2_check1():
    # Test16
    @s6.counter_factory(counters_instance2)
    def add(a, b):
        return a + b
    assert add(0,0) == 0, "Addition is not working properly"
    assert counters_instance2[add.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"

def test_counter_factory_dict2_check2():
    # Test17
    @s6.counter_factory(counters_instance2)
    def mult(a, b, c):
        return a * b * c
    assert mult(0,2,3) == 0, "Multiplication is not working properly"
    assert counters_instance2[mult.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"

def test_counter_factory_dict1_check3():  
    # Test18  
    @s6.counter_factory(counters_instance2)
    def div(a ,b):
        if b==0:
            return "Hey, are you trying to divide by 0"
        return a/b
    assert div(5, 0) == "Hey, are you trying to divide by 0", "Division is not working properly"
    assert counters_instance2[div.__name__] == 1, "Correct instance of dictionary did not updated with the count of function call"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(s6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_wrapping():
    @s6.counter_factory(counters)
    def add(a, b):
        return a + b
    assert add.__name__ == "add", "Function did not wrapped"
    
def test_dockstring_of_fibonaci():
    assert s6.fibonaci.__doc__, "The dockstring is not their in the fibonaci function"
    
def test_dockstring_of_counter_factory():
    assert s6.counter_factory.__doc__, "The dockstring is not their in the fibonaci function"
