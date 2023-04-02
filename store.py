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


def data_read():
    """Reads the data in a file"""
    with open("data.txt", "r") as file:
        context = file.readlines()

    # filters the data
    context = [item.strip('\n').split(",") for item in context]

    return context


if __name__ == "__main__":
    print(data_read())
