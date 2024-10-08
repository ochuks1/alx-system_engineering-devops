#!/usr/bin/python3

import json
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py EMPLOYEE_ID")
        return

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Prepare JSON data
    user_tasks = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            } for task in todos
        ]
    }

    # Write to JSON file
    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(user_tasks, json_file)

if __name__ == "__main__":
    main()
