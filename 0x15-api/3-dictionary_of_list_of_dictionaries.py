#!/usr/bin/python3
""" a python script that exports a all data to a json file from an API """

if __name__ == "__main__":
    import json
    import requests

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    finalDict = {}

    for user in users:
        uid = user.get('id')
        username = user.get('username')
        taskList = []
        for todo in todos:
            task = {}
            if todo.get('userId') == uid:
                task['username'] = username
                task['task'] = todo.get('title')
                task['completed'] = todo.get('completed')

                taskList.append(task)
        finalDict[str(uid)] = taskList

    with open('todo_all_employees.json', 'w') as f:
        json.dump(finalDict, f)
