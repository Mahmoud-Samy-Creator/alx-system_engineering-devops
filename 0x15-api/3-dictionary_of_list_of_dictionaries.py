#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    user_data = users_response.json()
    todos_data = todos_response.json()

    task_dict = {}
    task_list = []

    for user in user_data:
        for task in todos_data:
            if user['id'] == task['userId']:
                data = {"username": user["username"],
                        "task": task["title"],
                        "completed": task["completed"]}
                task_list.append(data)
        task_dict[f"{user['id']}"] = task_list
        task_list = []

    with open('USER_ID.json', mode='w') as file:
        json.dump(task_dict, file)
