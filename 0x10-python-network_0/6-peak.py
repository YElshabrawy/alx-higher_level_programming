#!/usr/bin/python3
'''finds peak of a list'''


def find_peak(list_of_integers):
    """finds max in an unsorted list of integers"""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare middle element with its neighbors (if neighbors exist)
        if (mid == 0
            or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1
                or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]

        # If the left neighbor is greater, then the peak lies on the left side
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid

        # Else the peak lies on the right side
        else:
            left = mid + 1

    return list_of_integers[left]
