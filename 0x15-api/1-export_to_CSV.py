#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    file_name = f'{id}.csv'
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_data = users_response.json()
    todos_data = todos_response.json()

with open(file_name, mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL, lineterminator='\n')

    for task in todos_data:
        if task.get('userId') == int(id):
            writer.writerow([id, user_data[int(id)]['name'],
                             str(task.get('completed')),
                             task.get('title')])
