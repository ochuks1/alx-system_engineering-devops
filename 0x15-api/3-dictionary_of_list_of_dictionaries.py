#!/usr/bin/env python3
# Create a new dictionary to combine user data with their to-do lists
import json
import requests

def fetch_data():
    """Fetches data from the API and returns a dictionary of tasks."""
    # Fetch users
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch todos
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create a dictionary to hold tasks by user ID
    tasks_by_user = {}

    # Populate the dictionary with tasks
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        tasks_by_user[user_id] = []

        for todo in todos:
            if todo['userId'] == user['id']:
                task_info = {
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                }
                tasks_by_user[user_id].append(task_info)

    return tasks_by_user

def save_to_json(data):
    """Saves the data to a JSON file."""
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)

def main():
    tasks_data = fetch_data()
    save_to_json(tasks_data)

if __name__ == "__main__":
    main()
