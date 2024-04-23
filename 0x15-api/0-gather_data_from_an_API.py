#!/usr/bin/python3
"""  a Python script that, using this
    'https://jsonplaceholder.typicode.com/todos' API,
    for a given employee ID, returns information about
    his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    todoOfEmployee = []
    nameOfEmployee = ''
    completed = 0

    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            todoOfEmployee.append(todo)

    for user in users:
        if user.get('id') == int(sys.argv[1]):
            nameOfEmployee = user.get('name')
            break

    for todo in todoOfEmployee:
        if todo.get('completed'):
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        nameOfEmployee, completed, len(todoOfEmployee)))

    for todo in todoOfEmployee:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
