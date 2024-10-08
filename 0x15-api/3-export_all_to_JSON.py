#!/usr/bin/python3
"""
This script retrieves TODO list data for all employees from a REST API
and exports it to a JSON file named todo_all_employees.json.
"""

import json  # Import json module to handle JSON file operations
import requests  # Import requests to make API calls

def export_all_employees_todos():
    """Export all employees' TODOs to a JSON file."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    users = response.json()
    all_employee_data = []

    # Loop through each user and fetch their TODOs
    for user in users:
        user_id = user['id']
        username = user['username']
        
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos_response = requests.get(todos_url)

        if todos_response.status_code == 200:
            todos = todos_response.json()
            for todo in todos:
                all_employee_data.append({
                    "USER_ID": user_id,
                    "USERNAME": username,
                    "TASK_COMPLETED_STATUS": todo['completed'],
                    "TASK_TITLE": todo['title'],
                })

    # Write all tasks to a JSON file
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_employee_data, jsonfile)

    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    export_all_employees_todos()
