#!/usr/bin/python3
import sys
ac = len(sys.argv) - 1
if ac == 0:
    print("{} arguments.".format(0))
else:
    print("{} {}:".format(ac, "argument" if ac == 1 else "arguments"))
    for i in range(1, ac + 1):
        print("{}: {}".format(i, sys.argv[i]))
