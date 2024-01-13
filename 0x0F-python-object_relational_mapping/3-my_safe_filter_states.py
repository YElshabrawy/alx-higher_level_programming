#!/usr/bin/python3
'''Lists all states'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]
    stateName = argv[4]
    db = MySQLdb.connect(password=dbPass, database=dbName,
                         user=dbUser, host='localhost', port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id"
              .format(stateName))
    rows = c.fetchall()
    for row in rows:
        if row[1] == stateName:
            print(row)
    c.close()
    db.close()
