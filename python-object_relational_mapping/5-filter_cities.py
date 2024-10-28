#!/usr/bin/python3
""" 5-filter_cities """

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
    query = "SELECT cities.name \
              FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE states.name = %s \
              ORDER BY cities.id ASC"
    cursor.execute(query, sys.argv[4])

    # Fetch and display results
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close database connection
    cursor.close()
    db.close()
