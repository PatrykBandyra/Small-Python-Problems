import logging
from functools import wraps
from typing import Callable, Union, Literal


def my_logger(logger: Union[logging.Logger, None] = None, log_level: Literal[10, 20, 30, 40, 50] = logging.DEBUG,
              file_handler: Union[logging.FileHandler, None] = None,
              log_to_terminal: bool = False,
              formatter: Union[logging.Formatter, None] = None) -> Callable:
    """
    Adds logging to a wrapped function. Standard message: function name with arguments and key word arguments.
    If you provide logger and/or file_handler, then neither formatter nor level will be applied to it/them.
    Provided logger shall have all desired handlers already set.
    <<<WATCH OUT>>> for levels of provided logger and log_level for a decorator.

    :param logger: if no logger provided - the new one will be created with the name of a function
    :param log_level: 10, 20, 30, 40, 50 - logging.DEBUG, logging.INFO, etc.
    :param file_handler: if no file handler provided - the new one will be created: <function_name>.log
    :param log_to_terminal: if True, then logs will be printed in terminal
    :param formatter: if no formatter provided - default format in use (level_name: name: time: message)
    :return: function wrapped in functionality of logging
    """
    def outer_function(original_function: Callable) -> Callable:

        # Logger
        if logger is None:  # If no logger provided - creates logger with name of a function
            logger_ = logging.getLogger(original_function.__name__)
            logger_.setLevel(log_level)
        else:
            logger_ = logger

        # Formatter
        if formatter is None:  # If no formatter provided - creates default formatter
            formatter_ = logging.Formatter('%(levelname)s: %(name)s: %(asctime)s: %(message)s')
        else:
            formatter_ = formatter

        # FileHandler
        if file_handler is None:  # If no file_handler provided - creates log file for a function
            file_handler_ = logging.FileHandler(f'logs/{original_function.__name__}.log')
            file_handler_.setFormatter(formatter_)
            file_handler_.setLevel(log_level)
        else:
            file_handler_ = file_handler
            if formatter is not None:
                file_handler_.setFormatter(formatter_)

        if logger is None:
            logger_.addHandler(file_handler_)

        # StreamHandler
        if log_to_terminal:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter_)
            stream_handler.setLevel(log_level)
            logger_.addHandler(stream_handler)

        @wraps(original_function)
        def wrapper(*args, **kwargs) -> Callable:
            logger_.log(log_level, f'Ran {original_function.__name__}() with args: {args}, and kwargs: {kwargs}')
            return original_function(*args, **kwargs)
        return wrapper
    return outer_function


"""
Some examples of functionalities of above decorator.
"""


def example_1_default():
    """
    Presents default my_logger behaviour - no kwargs passed to decorator.
    New log shall be added to file 'show_welcome.log' in current directory.
    """

    @my_logger()
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Patrick', 12)


def example_2_print_to_console():
    """
    Functionality of example_1 + printing logs to console.
    """

    @my_logger(log_to_terminal=True)
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('John', 32)


def example_3_print_to_console_change_console_level():
    """
    Functionality of example 2 but level of logs changed.
    """

    @my_logger(log_to_terminal=True, log_level=logging.ERROR)
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Bob', 32)


def example_4_custom_formatter():
    """
    Functionality of example 3 + added custom formatter.
    """
    @my_logger(log_to_terminal=True, log_level=logging.ERROR,
               formatter=logging.Formatter('My custom formatter: %(asctime)s: %(name)s: %(levelname)s: %(message)s'))
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Michael', 52)


def example_5_custom_file_handler():
    """
    Changed location of logging. Formatter not provided - using formatter set in file handler.
    """
    file_handler = logging.FileHandler('logs/logging_decorator.log')
    file_handler.setFormatter(logging.Formatter('My custom formatter: %(asctime)s: %(name)s: %(levelname)s: %(message)s'))

    @my_logger(file_handler=file_handler)
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Rob', 44)


def example_6_custom_file_handler_custom_formatter():
    """
    Functionality of example 5 + custom formatter + console.
    """
    file_handler = logging.FileHandler('logs/logging_decorator.log')

    @my_logger(file_handler=file_handler, log_to_terminal=True,
               formatter=logging.Formatter('Hello There :): %(asctime)s: %(name)s: %(levelname)s: %(message)s'))
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Greg', 74)


def example_7_custom_logger():
    """
    Decorator provided with logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('logs/logging_decorator.log')
    file_handler.setFormatter(logging.Formatter('Welcome!!!: %(asctime)s: %(name)s: %(levelname)s: %(message)s'))
    logger.addHandler(file_handler)

    @my_logger(logger=logger, log_to_terminal=True)
    def show_welcome(name: str, age: int):
        print(f'Welcome ({name}, {age})')

    show_welcome('Greg', 74)


def example_8():
    """
    Wrapped function has kwargs.
    """

    @my_logger(log_to_terminal=True)
    def show_welcome(name: str, age: int = 100):
        print(f'Welcome ({name}, {age})')

    show_welcome('Greg')
    show_welcome('Andrew', age=66)


def example_9_two_functions_decorated():
    @my_logger(log_to_terminal=True)
    def show_welcome(name: str, age: int = 100):
        print(f'Welcome ({name}, {age})')

    @my_logger(log_to_terminal=True)
    def print_smile(big=True):
        print(':)))))' if big else ':)')

    show_welcome('Greg')
    print_smile(big=False)


if __name__ == '__main__':
    example_1_default()
    example_2_print_to_console()
    example_3_print_to_console_change_console_level()
    example_4_custom_formatter()
    example_5_custom_file_handler()
    example_6_custom_file_handler_custom_formatter()
    example_7_custom_logger()
    example_8()
    example_9_two_functions_decorated()
