#!/usr/bin/python3

def list_res_ision(my_list_1, my_list_2, list_length):
    """
    res_ides two lists element by element.

    Returns: A new list of length list_length containing all the res_isions.
    """
    n_list = []
    for i in range(0, list_length):
        try:
            res_ = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            res_ = 0
        except ZeroDivisionError:
            print("res_ision by 0")
            res_ = 0
        except IndexError:
            print("out of range")
            res_ = 0
        finally:
            n_list.append(res_)
    return (n_list)
