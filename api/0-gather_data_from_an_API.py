#!/usr/bin/python3
"""
Module for tasks
"""
import requests
from sys import argv


def get_user_info_and_todos(id):
    """
    Retrieves user information and todos based on the given user ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, id)).json()
    user_name = user.get("name")

    todo = requests.get("{}/todos?userId={}".format(base_url, id)).json()
    total_tasks = len(todo)
    completed_tasks_count = 0
    completed_tasks = []

    for task in todo:
        if task.get("completed"):
            completed_tasks_count += 1
            completed_tasks.append(task.get("title"))

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, completed_tasks_count, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t " + task)


if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    id = int(argv[1])
    get_user_info_and_todos(id)
