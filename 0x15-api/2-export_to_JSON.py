#!/usr/bin/python3
"""
Given an employee, give Records all tasks that are owned by this employee
Format:
    { "USER_ID":
    [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}
"""

from sys import argv
from requests import get
import json

if __name__ == "__main__":
    id = int(argv[1])
    user = get('https://jsonplaceholder.typicode.com/users')
    tasks = get('https://jsonplaceholder.typicode.com/todos')

    user_data = user.json()
    task_data = tasks.json()

    detail = {}
    tasks_list = []
    final_details = {}

    for task in task_data:
        if task['userId'] == id:
            detail['task'] = task['title']
            detail['completed'] = task['completed']
            detail['username'] = user_data[id - 1]['username']
            tasks_list.append(detail)
            detail = {}

    final_details[f'{id}'] = tasks_list

    with open(f'{id}'+'.json', mode="w") as file:
        json.dump(final_details, file)
