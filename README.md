# epai-session6

This repository contains several Python functions and decorators that demonstrate the use of closures, decorators.

## closure_dockstring_check:
This is a closure that takes a function func and an integer threshold as arguments.

The closure checks whether the provided function func has a docstring with at least threshold characters.

Returns: A checker function that returns True if the docstring is present and meets the character threshold, otherwise returns False.

## fibonaci():
A decorator that provides a memoized implementation of the Fibonacci sequence calculation.

Returns: The calc_fibonaci function, which computes the Fibonacci number for a given index n.

The calc_fibonaci function first checks a cache to see if the Fibonacci number has already been computed. If so, it returns the cached value; otherwise, it computes the number, stores it in the cache, and returns it.

## counter_factory:
A decorator factory that creates a decorator to keep track of how many times a function has been called.

Parameters: counters is a dictionary used to store the call counts for various functions.

Returns: The fn_call_counter decorator, which increments the call count each time the wrapped function is executed.