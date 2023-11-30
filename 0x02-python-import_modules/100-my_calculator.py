#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calculate
    args = len(argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, calculate.add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, calculate.sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, calculate.mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, calculate.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
