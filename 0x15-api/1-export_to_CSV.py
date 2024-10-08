#!/usr/bin/python3
"""
This script retrieves employee TODO list data from a REST API
and exports it to a CSV file. It accepts an employee ID as a
command-line argument and saves the employee's tasks to a CSV file
named USER_ID.csv.
"""

import csv  # Import csv module to handle CSV file operations
import requests  # Import requests to make API calls
import sys  # Import sys for command line arguments

def export_employee_tasks_to_csv(employee_id):
    """Export employee tasks to a CSV file."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    todos = response.json()
    user_id = employee_id
    username = "User Name"  # Placeholder for username, API does not provide it

    # Create CSV filename
    filename = f"{user_id}.csv"

    # Write tasks to CSV file
    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for todo in todos:
            csv_writer.writerow([user_id, username, todo['completed'], todo['title']])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    # Check if the employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
        export_employee_tasks_to_csv(emp_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
