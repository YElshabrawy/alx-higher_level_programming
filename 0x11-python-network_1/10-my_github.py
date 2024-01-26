#!/usr/bin/python3
'''g'''
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/user"
    res = requests.get(url, auth=(argv[1], argv[2]))
    if res.status_code == 200:
        print(res.json()['id'])
    else:
        print(None)
