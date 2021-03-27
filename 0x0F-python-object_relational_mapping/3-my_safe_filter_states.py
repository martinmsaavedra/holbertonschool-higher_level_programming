#!/usr/bin/python3
'''Takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections.'''
from sys import argv
import MySQLdb

if __name__ == "__main__":

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, charset="utf8")
    cur = db.cursor()
    txtSQL = "SELECT * FROM states WHERE name = %(state)s ORDER BY id ASC"
    cur.execute(txtSQL, {'state': STATE})

    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    db.close()
