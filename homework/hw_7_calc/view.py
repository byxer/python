from fractions import Fraction


def get_value():
    value = input('Введите число: ')
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value

def get_operation():
    operation = input('Введите оператор: ')
    return operation

def get_result(result):
    print(f'\nОтвет: {result}')