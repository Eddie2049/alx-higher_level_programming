#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dummy_list = my_list[:]
    if (idx < 0 or idx > len(my_list) - 1):
        return dummy_list
    else:
        dummy_list[idx] = element
    return dummy_list
