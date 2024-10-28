#!/usr/bin/python3
""" 5-filter_cities """

import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      pwd=password,
      db=database
    )
    query = (
        "SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC"
    )
    cursor = db.cursor()
    cursor.execute(query, (state_name))
    cities = cursor.fetchall()
    for city in cities:
        print(city[0])
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py "
              "<mysql username> "
              "<mysql password> "
              "<database name> "
              "<state name>")
    else:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
