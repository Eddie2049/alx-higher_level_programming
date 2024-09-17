#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """creates a new list where each element is True
    if it's divisible by 2, otherwise False
    """
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
