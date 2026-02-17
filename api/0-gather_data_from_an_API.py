#!/usr/bin/python3
"""
fetch and display names, number of done tasks and names
of done tasks for a given user id
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)



    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id}
    )

    user = user_response.json()
    todos = todos_response.json()

    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")
