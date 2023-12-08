#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if not (0 <= idx < len(my_list)):
        return (my_list)

    copied_list = [integer for integer in my_list]
    copied_list[idx] = element
    return (copied_list)
