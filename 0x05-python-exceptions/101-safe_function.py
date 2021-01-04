#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        msg = "Exception: " + str(err) + "\n"
        sys.stderr.write(msg)
    return None
