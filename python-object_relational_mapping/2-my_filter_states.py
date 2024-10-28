#!/usr/bin/python3
""" 2-my_filter_states """

import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cursor = db.cursor()

    # Create and execute query
    query = "SELECT * FROM states WHERE BINARY name = '{}' \
            ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
