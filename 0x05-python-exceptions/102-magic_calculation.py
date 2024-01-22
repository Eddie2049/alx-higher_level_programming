#!/usr/bin/python3

def magic_calculation(a, b):
    """
    does exactly the same as the following Python bytecode:
    """
    res_ = 0
    for i in range(1, 3):
        try:
            if a < i:
                raise Exception('Too far')
            res_ += a ** b / i
        except Exception:
            res_ = a + b
            break
    return res_
