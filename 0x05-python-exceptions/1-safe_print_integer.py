#!/usr/bin/python3

"""this function prints an integer with "{:d}".format()."""


def safe_print_integer(value):
 try:
    print("{:d}".format(value))
 except Exception:
    return False
 return True
