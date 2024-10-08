#!/usr/bin/python3
"""
This script retrieves employee TODO list data from a REST API
and exports it to a JSON file. It accepts an employee ID as a
command-line argument and saves the employee's tasks to a JSON file
named USER_ID.json.
"""

import json  # Import json module to handle JSON file operations
import requests  # Import requests to make API calls
import sys  # Import sys for command line arguments

def export_employee_tasks_to_json(employee_id):
    """Export employee tasks to a JSON file."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    todos = response.json()
    username = "User Name"  # Placeholder for username, API does not provide it

    # Prepare data to be written to JSON
    employee_data = []
    for todo in todos:
        employee_data.append({
            "USER_ID": employee_id,
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": todo['completed'],
            "TASK_TITLE": todo['title'],
        })

    # Create JSON filename
    filename = f"{employee_id}.json"

    # Write tasks to JSON file
    with open(filename, 'w') as jsonfile:
        json.dump(employee_data, jsonfile)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    # Check if the employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
        export_employee_tasks_to_json(emp_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
