#!/usr/bin/python3
""" 3-my_safe_filter_states """

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
