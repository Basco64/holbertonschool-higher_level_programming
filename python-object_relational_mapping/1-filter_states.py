#!/usr/bin/python3
""" 1-filter_states """

import sys
import MySQLdb


def filter_states(username, password, database):
    """ Filter states by 'N' """
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      pwd=password,
      db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """ Checking arguments and execution"""
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py "
              "<mysql username> "
              "<mysql password> "
              "<database name>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
