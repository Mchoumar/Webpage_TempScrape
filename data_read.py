"""
This script reads data from the database file
"""
import sqlite3
from time import strftime

# Opens the database file
connection = sqlite3.connect("data.db")


def read():
    # Access data from the database file
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM events")
    data = cursor.fetchall()

    return data


if __name__ == "__main__":
    print(read())
