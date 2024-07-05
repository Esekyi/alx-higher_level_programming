#!/usr/bin/python3
"""a python script that finds the peak of a list of unsorted integers"""
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted
    integers without going through
    all the number in the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
