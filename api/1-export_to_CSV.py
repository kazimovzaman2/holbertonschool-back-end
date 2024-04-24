#!/usr/bin/python3
"""
Module for tasks
"""
import requests
import csv
from sys import argv


def main(id):
    """
    Retrieves user information and todos based on the given user ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, id)
    todo_url = "{}/todos?userId={}".format(base_url, id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    for task in todos:
        with open(f"{user["id"]}.csv", "a") as f:
            file = csv.writer(f, quoting=csv.QUOTE_ALL)
            file.writerow(
                [user["id"], user["name"], task["completed"], task["title"]]
            )


if __name__ == "__main__":
    if len(argv) == 2:
        id = int(argv[1])
        main(id)
