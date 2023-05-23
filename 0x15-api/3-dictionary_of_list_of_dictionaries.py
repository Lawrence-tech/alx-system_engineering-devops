#!/usr/bin/python3
"""
Module contains python script for making an api call and writing response to
csv file
"""

import json
import requests


if __name__ == '__main__':
    # Define the URLs for users and todos
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Make API calls to retrieve users and todos data
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Prepare a dictionary to store todos for each user
    todos_dict = {}
    for user in users:
        user_todo_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                new_dict = {
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': user.get('username')
                }
                user_todo_list.append(new_dict)
        todos_dict[user.get('id')] = user_todo_list

    # Define the output file name
    file_name = 'todo_all_employees.json'

    # Write the todos data to a JSON file
    with open(file_name, mode='w') as outfile:
        json.dump(todos_dict, outfile)
