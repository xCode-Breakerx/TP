from calculator.calculator import calculate


def main():
    operation = input("Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): ")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(calculate(operation, num1, num2))


if __name__ == '__main__':
    main()
