#!/usr/bin/python3
"""
fetch and display names, number of done tasks and names
of done tasks for a given user id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    api_url = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]
    response = requests.get(f"{api_url}/users/{EMPLOYEE_ID}/todos",
                            params={"_expand": "user"})
    data = response.json()

    if response.status_code != 200:
        print("request not successfull")
        sys.exit()

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task.get("completed")]
    total_done_tasks = len(done_tasks)
    print(f"Employee {employee_name} is"
          f" done with tasks({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f'\t {task.get("title")}')
