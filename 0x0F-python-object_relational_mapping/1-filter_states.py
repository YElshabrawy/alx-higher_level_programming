#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2], database=argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states WHERE name LIKE "N%"')
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
