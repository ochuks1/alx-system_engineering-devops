#!/usr/bin/python3

import requests
import sys

def main():
    # Check if an employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        return

    employee_id = sys.argv[1]

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get todo data
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Calculate completed tasks
    total_tasks = len(todos)
    completed_tasks = [task['title'] for task in todos if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Output the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task_title in completed_tasks:
        print(f"\t {task_title}")

if __name__ == "__main__":
    main()
