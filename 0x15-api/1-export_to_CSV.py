#!/usr/bin/python3
""" a python script that exports a data in csv format """
if __name__ == "__main__":
    import csv
    import requests
    import sys

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    userTodos = []
    username = ''
    for user in users:
        if user.get('id') == int(sys.argv[1]):
            username = user.get('username')
            break

    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            userTodos.append(todo)

    with open(sys.argv[1] + '.csv', 'w') as csvFile:
        csvWrite = csv.writer(csvFile)

        for todo in userTodos:
            row = [sys.argv[1], username]
            row.append(str(todo.get('completed')))
            row.append(str(todo.get('title')))

            csvWrite.writerow(row)
