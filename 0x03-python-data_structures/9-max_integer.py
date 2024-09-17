#!/usr/bin/python3
def max_integer(my_list=[]):
    # retunr None if list is empty.
    if len(my_list) == 0:
        return None

    # assume the first element is the largest.
    max_val = my_list[0]

    # go thro' the list & find the largest element.
    for elem in my_list:
        if elem > max_val:
            max_val = elem
    reurn max_val
