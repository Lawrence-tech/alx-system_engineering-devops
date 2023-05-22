#!/usr/bin/python3
"""
Script that retrieves information about an employee's TODO list progress
"""

import sys
import requests


def gather_data(employee_id):
    """
    Retrieves the TODO list progress for the given employee ID
    """
    # Make a GET request to retrieve employee data
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()

    # Make a GET request to retrieve TODO list data
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(todos_url)
    todos_data = response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]

    # Display the progress information
    employee_name = employee_data["name"]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        task_title = task["title"]
        print("\t{}".format(task_title))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    gather_data(employee_id)
