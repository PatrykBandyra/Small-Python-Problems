import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')

file_handler = logging.FileHandler('logging_example.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


if __name__ == '__main__':

    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

    sub_result = subtract(num_1, num_2)
    logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

    mul_result = multiply(num_1, num_2)
    logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

    div_result = divide(num_1, num_2)
    logger.debug(f'Div: {num_1} / {num_2} = {div_result}')