#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        msg = "Exception: " + str(err) + "\n"
        sys.stderr.write(msg)
        return False
