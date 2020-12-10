#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    res = 0
    for i in range(1, ac + 1):
        res += int(sys.argv[i])
    print("{}".format(res))
