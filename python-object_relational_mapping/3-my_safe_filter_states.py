#!/usr/bin/python3

import sys
import MySQLdb


def filter_states(username, password, database):
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      pwd=password,
      db=database
    )
    query = (
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC"
    )
    cursor = db.cursor()
    cursor.execute(query, (state_name))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./3-my_safe_filter_states.py "
              "<mysql username> "
              "<mysql password> "
              "<database name> "
              "<state name>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
