#!/usr/bin/python3
""" 2-my_filter_states """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )


    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(
        sys.argv[4])

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
