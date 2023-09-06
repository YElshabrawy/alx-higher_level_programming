#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    c = i
    if i % 2 != 0:
        c = i - (ord('a') - ord('A'))
    print("{}".format(chr(c)), end="")
