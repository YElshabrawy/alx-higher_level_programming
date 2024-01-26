#!/usr/bin/python3
'''m'''
import urllib.request as ur
from sys import argv
import urllib.parse as up

if __name__ == "__main__":
    data = up.urlencode({'email': argv[2]}).encode('utf-8')
    req = ur.Request(argv[1], data)
    with ur.urlopen(req) as res:
        print(res.read().decode('utf-8'))
