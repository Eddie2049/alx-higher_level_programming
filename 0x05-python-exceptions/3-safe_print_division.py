#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div_res = a / b
    except (ZeroDivisionError, TypeError):
        div_res = None
    finally:
        print("Inside result: {}".format(div_res))

    return (div_res)
