#!/usr/bin/python3

import sys
import MySQLdb


def list_cities_by_state(username, password, database):
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      pwd=password,
      db=database
    )
    query = (
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
    )
    cursor = db.cursor()
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]} - {city[1]} - {city[2]}")
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py "
              "<mysql username> "
              "<mysql password> "
              "<database name>")
    else:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
