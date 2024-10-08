#!/usr/bin/python3

import csv
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py EMPLOYEE_ID")
        return

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Prepare CSV file
    with open(f"{employee_id}.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task['completed'], task['title']])

if __name__ == "__main__":
    main()
