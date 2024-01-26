#!/usr/bin/python3
'''v'''
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    code = res.status_code
    if code >= 400:
        print("Error code:", code)
        exit(1)
    print(res.text)
