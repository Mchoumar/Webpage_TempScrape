"""
This script store or reads the data in a database file
"""
from time import strftime
import sqlite3 as sq

# Opens the database file
connection = sq.connect("data.db")


def store(extract):
    """Stores the data into a text file"""
    print("Storing data!")

    # Access database data
    cursor = connection.cursor()

    # stores the data into a dictionary and stores them into the txt file
    now_time = strftime("%y-%m-%d-%H-%M-%S")

    content = [now_time, extract]

    cursor.execute("INSERT INTO events VALUES(?, ?)", content)
    connection.commit()

    print("Data stored!")


if __name__ == "__main__":
    store(19)
