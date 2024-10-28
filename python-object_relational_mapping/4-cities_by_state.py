#!/usr/bin/python3
""" 4-cities_by_state """

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
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities \
                   JOIN states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
