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
    c.execute('''SELECT cities.id, cities.name, states.name
              FROM states
              JOIN cities ON cities.state_id = states.id
              ORDER BY cities.id''')
    rows = c.fetchall()
    output = ''
    for row in rows:
        if row[2] == stateName:
            output += row[1]
            output += ", "
    print(output[:-2])
    c.close()
    db.close()
