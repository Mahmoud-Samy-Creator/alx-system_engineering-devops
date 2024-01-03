#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

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
