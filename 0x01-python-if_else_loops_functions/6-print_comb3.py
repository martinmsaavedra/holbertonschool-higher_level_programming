#!/usr/bin/python3

for i in range (10):
    for j in range (10):
        if i < j:
            print("{:d}".format(i), end="")
            print("{:d}".format(j), end="")
            if i != 8 or j != 9:
                print(", ", end="")
print()
