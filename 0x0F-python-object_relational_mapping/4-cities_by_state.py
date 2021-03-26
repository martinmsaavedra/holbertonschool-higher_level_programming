#!/usr/bin/python3
'''Lists all cities from the database hbtn_0e_4_usa'''
from sys import argv
import MySQLdb

if __name__ == "__main__":

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, charset="utf8")
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON \
            states.id = cities.state_id ORDER BY cities.state_id ASC")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    db.close()
