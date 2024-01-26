#!/usr/bin/python3
'''v'''
import requests
from sys import argv

if __name__ == "__main__":
    REPO = argv[1]
    OWNER = argv[2]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    res = requests.get(url, params={"per_page": 10})
    commits = res.json()
    for c in commits:
        print(f"{c['sha']}: {c['commit']['author']['name']}")
