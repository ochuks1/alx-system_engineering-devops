#!/usr/bin/python3
"""
This script retrieves employee TODO list progress from a REST API.
"""

import json  # Import the json library for handling JSON data
import requests  # Import requests to make API calls
import sys  # Import sys for command line arguments

def fetch_employee_todo_progress(employee_id):
    """Fetch TODO progress for a given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    
    # Print the output
    employee_name = "Employee Name"  # Placeholder, as we don't have employee names in the API
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    # Check if the employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
        fetch_employee_todo_progress(emp_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
