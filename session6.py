def closure_dockstring_check(func, threshold:int):
    char_threshold = threshold
    def checker(*args, **kwargs):
        dock_string = func.__doc__
        # print(dock_string)
        return True if dock_string and len(dock_string)>=char_threshold else False
    return checker

def dock_string_check():
    """A Python function docstring is a string literal that is used to document a function's purpose, behavior, and usage.
      It provides an easy way to understand what the function does, the parameters it takes, the return value it produces,
     and any exceptions it might raise. Docstrings are placed immediately after the function's definition line
    and are enclosed in triple quotes, allowing for multiline text."""
    pass


def fibonaci():
    """
        it's a fibonaci decorator.
        returns: calc_fibonaci function
    """
    cache = {0:1, 1: 1, 2: 2}
    
    def calc_fibonaci(n:int):
        """
        calc_fibonaci : 
                parameter : n (int), position of the fibonaci number in fibonaci deries
                returns: Fibonaci number at nth index

                it first check in cache dictionary, whether the function is already called for nth index, if yes then it fetches the value from cahced dict and returns it,
                otherwise it computes the fibonaci number and then cache it in dict
        """
        if n not in cache:
            print(f'Calculating fib({n})')
            cache[n] = calc_fibonaci(n-1) + calc_fibonaci(n-2)
        return cache[n]
    
    return calc_fibonaci


def counter_factory(counters:dict):
    """
        Decorator factory:
            parameters: counters (dictionary to maintain per function calls count)
            returns: Decorator (fn_call_counter)
    """
    def fn_call_counter(fn):
        """
            Decorator:
                parameters: fn (function)
                returns: inner function that calls the fn with all the passed key word and positional arguments
        """
        from functools import wraps
        cnt = counters.get(fn.__name__, 0)  # initially fn has been run zero times
        @wraps(fn)
        def inner(*args, **kwargs):
            """
                inner function : that maintains the function call count in a global dictionary and returns function output that has been called in it.
            """
            nonlocal cnt
            cnt = cnt + 1
            counters[fn.__name__] = cnt  # counters is global
            return fn(*args, **kwargs)
        return inner
    return fn_call_counter