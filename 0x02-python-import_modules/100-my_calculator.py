#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    ac = len(sys.argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        total = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{:d} + {:d} = {:d}".format(int(sys.argv[1]),
              int(sys.argv[3]), total))
    elif sys.argv[2] == "-":
        total = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{:d} - {:d} = {:d}".format(int(sys.argv[1]),
              int(sys.argv[3]), total))
    elif sys.argv[2] == "*":
        total = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{:d} * {:d} = {:d}".format(int(sys.argv[1]),
              int(sys.argv[3]), total))
    elif sys.argv[2] == "/":
        total = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{:d} / {:d} = {:d}".format(int(sys.argv[1]),
              int(sys.argv[3]), total))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
