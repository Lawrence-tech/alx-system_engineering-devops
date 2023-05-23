#!/usr/bin/python3
'''
Module contains python script for making an api call and writing response to
csv file
'''

import json
import requests
import sys


if __name__ == '__main__':
    # Get the user ID from command-line argument
    user_id = sys.argv[1]

    # Define the API URLs for user and todos
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todos_url = url + 'todos'

    # Make API calls to retrieve user and todo data
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    # Prepare the todo list for the user
    todo_list = []
    for todo in todos:
        new_dict = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username')
        }
        todo_list.append(new_dict)

    # Create a dictionary with the user ID as the key
    todo_dict = {user.get('id'): todo_list}

    # Define the output file name
    file_name = '{}.json'.format(user.get('id'))

    # Write the todo data to a JSON file
    with open(file_name, mode='w') as outfile:
        json.dump(todo_dict, outfile)
