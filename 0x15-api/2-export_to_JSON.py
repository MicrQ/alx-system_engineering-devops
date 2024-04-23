#!/usr/bin/python3
""" a python script that exports a data to a json file """

if __name__ == "__main__":
    import json
    import requests
    import sys

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    uid = int(sys.argv[1])
    userTodos = [todo for todo in todos if todo.get('userId') == uid]
    username = ''
    for user in users:
        if user.get('id') == uid:
            username = user.get('username')
            break

    taskList = []
    for todo in userTodos:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = username

        taskList.append(task)

    with open(sys.argv[1] + '.json', 'w') as f:
        json.dump({str(uid): taskList}, f)
