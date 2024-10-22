#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py "
              "<mysql username> "
              "<mysql password> "
              "<database name>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
