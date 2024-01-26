#!/usr/bin/python3
'''m'''
import urllib.request as ur

with ur.urlopen("https://alx-intranet.hbtn.io/status") as res:
    content = res.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
