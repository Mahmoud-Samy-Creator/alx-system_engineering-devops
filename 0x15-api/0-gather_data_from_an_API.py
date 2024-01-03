#!/usr/bin/python3

import requests
import json
from sys import argv

employer_id = int(argv[1])
no_of_done_tasks = 0

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

user_data = users_response.json()
todos_data = todos_response.json()


for data in todos_data:
    if data['userId'] == employer_id:
        if data['completed'] == 1:
            no_of_done_tasks += 1

print(f"Employee {user_data[employer_id - 1]['name']} is done with tasks({no_of_done_tasks}/20):")

for data in todos_data:
    if data['userId'] == employer_id:
        if data['completed'] == 1:
            print("\t ", end="")
            print(data['title'])
