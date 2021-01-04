#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        tot = a / b
    except (ValueError, ZeroDivisionError):
        tot = None
    finally:
        print("Inside result: {}".format(tot if tot is not None else "None"))
    return tot
