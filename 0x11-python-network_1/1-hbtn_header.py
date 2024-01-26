#!/usr/bin/python3
from ast import arg
import urllib.request as ur
from sys import argv

with ur.urlopen(argv[1]) as res:
    print(res.headers.get('X-Request-Id'))
