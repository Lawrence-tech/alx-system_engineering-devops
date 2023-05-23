#!/usr/bin/python3
"""
Module contains python script for making an api call
"""

import requests
import sys


def retrieve_todo_data(user_id):
    """
    Retrieves the TODO list progress for the given user ID
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todos_url = url + 'todos'

    user_response = requests.get(url).json()
    todos_response = requests.get(todos_url).json()

    completed_todos = [
        todo for todo in todos_response if todo.get('completed')
    ]

    return user_response, todos_response, completed_todos


def print_todo_progress(user, todos, completed_todos):
    """
    Prints the TODO list progress for the user
    """
    user_name = user.get('name')
    total_tasks = len(todos)
    completed_tasks = len(completed_todos)

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, completed_tasks, total_tasks))

    for todo in completed_todos:
        print('\t {}'.format(todo.get('title')))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 retrieve_todo_data.py <user_id>')
        sys.exit(1)

    user_id = sys.argv[1]
    user_data, todos_data, completed_tasks_data = retrieve_todo_data(user_id)
    print_todo_progress(user_data, todos_data, completed_tasks_data)
