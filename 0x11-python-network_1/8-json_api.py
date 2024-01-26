#!/usr/bin/python3
'''g'''
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://63f92135de34.92814df4.alx-cod.online:5000/search_user"
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    try:
        res = requests.post(url, {"q": q}).json()
        if res:
            print(f"[{res['id']}] {res['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
