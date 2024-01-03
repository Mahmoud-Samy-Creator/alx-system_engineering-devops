#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    done = 0

    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    user_data = users_response.json()
    todos_data = todos_response.json()

    for data in todos_data:
        if data['userId'] == id:
            if data['completed'] == 1:
                done += 1

    print(f"Employee {user_data[id-1]['name']} is done with tasks({done}/20):")

    for data in todos_data:
        if data['userId'] == id:
            if data['completed'] == 1:
                print("\t ", end="")
                print(data['title'])
