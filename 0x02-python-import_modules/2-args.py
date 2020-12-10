#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        print("0 arguments.")
    else:
        print("{:d} {}:".format(ac, "argument" if ac == 1 else "arguments"))
        for i in range(1, ac + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
