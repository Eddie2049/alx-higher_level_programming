#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ''' function checks if the index is valid
    (not negative and within the range of the list)
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list

    # remove the element at the specified index by slicing the list
    del my_list[idx]

    return my_list
