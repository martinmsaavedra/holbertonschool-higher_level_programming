#!/usr/bin/python3
'''Takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa'''
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
    txtSQL = "SELECT name FROM cities WHERE state_id IN\
        (SELECT id FROM states WHERE name=%(state)s) ORDER BY state_id ASC"
    cur.execute(txtSQL, {'state': STATE})
    query_row = cur.fetchall()
    text = ""
    for index, row in enumerate(query_row):
        if (index < len(query_row) - 1):
            text += row[0] + ", "
        else:
            text += row[0]
    print(text)
    cur.close()
    db.close()
