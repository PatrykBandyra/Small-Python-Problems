"""
First-Class Functions:
A programming language is said to have a first-class functions if it treats functions as first-class citizens.

First-Class Citizens:
A first-class citizen (object) is an entity which supports all the operations generally available to other entities.
These operations include being passed as an argument, returned from a function, and assigned to a variable.

Higher Order Functions:
Higher order function takes function as an argument or/and returns function as a result.
"""


def example_1():
    def square(x):
        return x * x

    def my_map(func, arg_list):
        result = []
        for i in arg_list:
            result.append(func(i))
        return result

    squares = my_map(square, [1, 2, 3, 4, 5])
    print(squares)


def example_2():

    def logger(msg):

        def log_message():
            print(f'Log: {msg}')

        return log_message

    log_hi = logger('Hi!')
    log_hi()


def example_3():

    def html_tag(tag):

        def wrap_text(msg):
            print(f'<{tag}>{msg}</{tag}>')

        return wrap_text

    print_h1 = html_tag('h1')
    print_h1('Test Headline!')
    print_h1('Another headline!')

    print_p = html_tag('p')
    print_p('Test Paragraph!')


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
