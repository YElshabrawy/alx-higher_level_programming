#!/usr/bin/python3
'''m'''
import urllib.request as ur
from sys import argv

if __name__ == "__main__":
    with ur.urlopen(argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
