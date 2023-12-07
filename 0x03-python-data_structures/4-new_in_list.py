#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        copied_list[idx] = element
        return copied_list
