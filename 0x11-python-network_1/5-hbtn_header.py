#!/usr/bin/python3
'''g'''
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    id = res.headers.get("X-Request-Id")
    print(id)
