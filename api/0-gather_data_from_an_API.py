#!/usr/bin/python3
"""
fetch and display names, number of done tasks and names
of done tasks for a given user id
"""
import requests
import sys


def fetch_employee_progress(employee_id):

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        return

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        number_of_done_tasks,
        total_tasks
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_progress(employee_id)
        except ValueError:
            pass
