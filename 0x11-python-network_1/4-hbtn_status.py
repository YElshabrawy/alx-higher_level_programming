#!/usr/bin/python3
'''g'''
import requests

if __name__ == "__main__":
    res = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
