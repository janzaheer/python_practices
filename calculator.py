
CONDITION_LIST = ['+', '-', '*', '*']


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def multiply(val1, val2):
    return val1 * val2


def divide(val1, val2):
    return val1 / val2


def calculator(val1, val2, condition):

    try:
        val1 = float(val1)
    except ValueError:
        raise AssertionError("Val1 is string")

    try:
        val2 = float(val2)
    except ValueError:
        raise AssertionError("Val2 is string")

    if condition not in CONDITION_LIST:
        raise AssertionError("Entered Wrong Condition")

    if condition == '+':
        return add(val1, val2)
    elif condition == '-':
        return subtract(val1, val2)
    elif condition == '*':
        return multiply(val1, val2)
    else:
        return divide(val1, val2)


if __name__ == '__main__':
    VAL1 = raw_input('Enter first value: ')
    VAL12 = raw_input('Enter Second Value: ')
    CONDITION = raw_input('Enter the conditoion e.g. (+, -, / or *): ')

    print calculator(VAL1, VAL12, CONDITION)
