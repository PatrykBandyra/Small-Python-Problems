"""
Decorator:
Decorator is a function that takes another function as an argument, adds some functionality to it and returns
another function.

2 ways - does the same thing, but the second one is more readable:

1.
    def display():
    print('Display function ran')

    decorated_display = decorator_function(display)
    decorated_display()

2.
    @decorator_function
    def display():
        print('Display function ran')

    display()
"""


def example_1():
    """
    Wrapped function takes no arguments.
    """
    def decorator_function(original_function):
        def wrapper_function():
            print(f'Wrapper executed this before {original_function.__name__}')
            original_function()
        return wrapper_function

    @decorator_function
    def display():
        print('Display function ran')

    display()


def example_2():
    """
    Wrapped functions takes arguments - wrapper function has to take *args and **kwargs and
    pass them to the original function. If wrapper function doesn't take arguments - error.
    """
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'Wrapper executed this before {original_function.__name__}')
            original_function(*args, **kwargs)
        return wrapper_function

    @decorator_function
    def display_info(name, age):
        print(f'Display_info ran with arguments ({name}, {age})')

    display_info('Patrick', 100)


def example_3():
    """
    Class decorators.
    """
    class DecoratorClass(object):
        def __init__(self, original_function):
            self.original_function = original_function

        def __call__(self, *args, **kwargs):
            print(f'Call method executed this before {self.original_function.__name__}')
            return self.original_function(*args, **kwargs)

    @DecoratorClass
    def display_info(name, age):
        print(f'Display_info ran with arguments ({name}, {age})')

    display_info('John', 40)


"""
Practical examples .....................................................................................................
"""


def practical_example_1():
    """
    Logging function calls.
    """
    def my_logger(original_function):
        import logging
        logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

        def wrapper(*args, **kwargs):
            logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
            return original_function(*args, **kwargs)

        return wrapper

    @my_logger
    def display_info(name, age):
        print(f'Display_info ran with arguments ({name}, {age})')

    display_info('Patrick', 50)


def practical_example_2():
    """
    Timing execution time of a function.
    """
    def my_timer(original_function):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = original_function(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{original_function} ran in: {t2} sec')
            return result

        return wrapper

    def recursive_fibonacci(n):
        if n <= 1:
            return n
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

    @my_timer
    def fibonacci_sequence(num):
        return recursive_fibonacci(num)

    fibonacci_sequence(35)


def practical_example_3():
    """
    Chaining decorators.
    """
    from functools import wraps  # Decorate wrappers with this decorator

    def my_logger(original_function):
        import logging
        logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

        @wraps(original_function)
        def wrapper(*args, **kwargs):
            logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
            return original_function(*args, **kwargs)

        return wrapper

    def my_timer(original_function):
        import time

        @wraps(original_function)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = original_function(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{original_function} ran in: {t2} sec')
            return result

        return wrapper

    def recursive_fibonacci(n):
        if n <= 1:
            return n
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

    @my_logger
    @my_timer
    def fibonacci_sequence(num):
        return recursive_fibonacci(num)

    fibonacci_sequence(35)


"""
Decorators with arguments ..............................................................................................
"""


def example_decorator_with_args():

    def prefix_decorator(prefix):
        def decorator_function(original_function):
            def wrapper_function(*args, **kwargs):
                print(f'{prefix} Executed before {original_function.__name__}')
                result = original_function(*args, **kwargs)
                print(f'{prefix} Executed after {original_function.__name__}')
                return result
            return wrapper_function
        return decorator_function

    @prefix_decorator('TESTING:')
    def display_info(name, age):
        print(f'Display_info ran with arguments ({name}, {age})')

    display_info('Patrick', 30)


if __name__ == '__main__':
    # example_1()
    # example_2()
    # example_3()
    # practical_example_1()
    # practical_example_2()
    # practical_example_3()
    example_decorator_with_args()
