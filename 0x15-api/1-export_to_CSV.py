#!/usr/bin/python3
"""
Extended Python script to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == '__main__':
    # Get the user ID from command-line argument
    user_id = sys.argv[1]

    # Make API calls to retrieve user and todo data
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/'
    todos_url = url + 'todos'
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    # Prepare the list of dictionaries for CSV
    dict_list = []
    for todo in todos:
        new_dict = {
            'userId': user.get('id'),
            'username': user.get('username'),
            'completed': todo.get('completed'),
            'title': todo.get('title')
        }
        dict_list.append(new_dict)

    # Define the output file name
    file_name = f'{user.get("id")}.csv'

    # Write data to CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        # Write header
        writer.writeheader()

        # Write data rows
        writer.writerows(dict_list)

    # Print the number of tasks in CSV
    tasks_msg = 'Number of tasks in CSV: {}'.format(
        'OK' if len(todos) == len(dict_list) else 'Incorrect'
    )
    print(tasks_msg)
