#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(4, 6)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
    return 0
