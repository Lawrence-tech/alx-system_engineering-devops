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
        new_dict = {}
        new_dict['userId'] = user.get('id')
        new_dict['username'] = user.get('username')
        new_dict['completed'] = todo.get('completed')
        new_dict['title'] = todo.get('title')
        dict_list.append(new_dict)

    # Define the output file name
    file_name = f'{user.get("id")}.csv'

    # Write data to CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quotechar='"'
                                , quoting=csv.QUOTE_ALL)

        # Write header
        writer.writeheader()

        # Write data rows
        writer.writerows(dict_list)
