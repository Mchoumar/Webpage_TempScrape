"""
This script store or reads the data in a text file
"""
from time import strftime


def store(extract):
    """Stores the data into a text file"""
    print("Storing data!")

    # stores the data into a dictionary and stores them into the txt file
    data = {}
    now_time = strftime("%y-%m-%d-%H-%M-%S")
    data["date"] = str(now_time)
    data["temperature"] = str(extract)
    content = f"{data['date']},{data['temperature']}\n"

    with open("data.txt", "a") as file:
        file.write(content)

    print("Data stored!")


if __name__ == "__main__":
    print(data_read())
