#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_ = number % -(10)
        print(-(last_), end='')
    else:
        last_ = number % 10
        print(last_, end='')
    return abs(last_)
