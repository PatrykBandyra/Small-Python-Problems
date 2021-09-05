import logging
logging.basicConfig(filename='example.log', level=logging.INFO)
"""
Closure:
A closure is a record storing a function together with an environment: a mapping associating each free variable
of the function with the value or storage location to which the name was bound when the closure was created.
A closure, unlike plain function, allows the function to access those captured variables through the closure's
reference to them, even when function is invoked outside their scope.
"""


def example_1():

    def outer_func(msg):
        message = msg

        def inner_func():   # This function is a closure - it has access to variables created in local scope
            print(message)  # message - free variable

        return inner_func

    hi_func = outer_func('Hi!')
    hello_func = outer_func('Hello!')

    hi_func()
    hello_func()


def example_2():

    def logger(func):

        def log_func(*args):
            logging.info(f'Running "{func.__name__}" with arguments {args}')
            print(func(*args))

        return log_func

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(3, 3)
    sub_logger(5, 2)


if __name__ == '__main__':
    example_1()
    example_2()
