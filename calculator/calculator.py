import decimal


def check_params(func: callable) -> callable:
    def wrapper(*args, **kars):
        for x in args:
            if not isinstance(x, (int, float, complex, decimal.Decimal)):
                raise TypeError
        for x in kars.values():
            if not isinstance(x, (int, float, complex, decimal.Decimal)):
                raise TypeError

        return func(*args, **kars)

    return wrapper


# def check_params_single(func: callable) -> callable:
#     def wrapper(x, y):
#         if not isinstance(x, (int, float, complex, decimal.Decimal)) or not isinstance(y, (int, float, complex, decimal.Decimal)):
#             raise TypeError
#         return func(x, y)
#
#     return wrapper

class Calculator:
    # use the static method decorator, otherwise the functions signatures below assume that the first parameter is "self".
    # these methods are meant to be called statically judging from the signature

    @staticmethod
    @check_params
    def add(x, y):
        return x + y  # the operation is ambiguous, this method has been changed to a static method

    @staticmethod
    @check_params
    def subtract(x, y):
        return x - y  # the operation is ambiguous, this method has been changed to a static method

    @staticmethod
    @check_params
    def multiply(x, y):
        return x * y  # the operation is ambiguous, this method has been changed to a static method

    @staticmethod
    @check_params
    def divide(x, y):
        return x / y  # the operation is ambiguous, this method has been changed to a static method

    @staticmethod
    @check_params
    def power(x, y):
        result = 1
        for i in range(y):
            result *= x  # the operation is ambiguous, this method has been changed to a static method
        return result

    @staticmethod
    @check_params
    def square_root(x):
        if x == 0 or x == 1:  # the operation is ambiguous, this method has been changed to a static method
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val


def calculate(operation, x, y):
    if operation == "add":
        result = Calculator.add(x, y)
    elif operation == "substract":
        result = Calculator.subtract(x, y)
    elif operation == "multiply":
        result = Calculator.multiply(x, y)
    elif operation == "divide":
        result = Calculator.divide(x, y)
    elif operation == "power":
        result = Calculator.power(x, y)
    elif operation == "square_root":
        result = Calculator.square_root(x)
    return result
