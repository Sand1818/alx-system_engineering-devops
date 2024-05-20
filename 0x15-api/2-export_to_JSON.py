#!/usr/bin/python3
"""
Exports data in the JSON format.
"""
import requests
import sys
import json

if __name__ == "__main__":
    arg1 = int(sys.argv[1])
    url1 = f"https://jsonplaceholder.typicode.com/users/{arg1}/"
    res = requests.get(url1)

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={arg1}"
    res2 = requests.get(url2)

    employee = res.json()
    todo_ = res2.json()

    total = len(todo_)
    dictionary = {}
    li = []

    for i in range(total):
        dic = {}
        dic['task'] = todo_[i].get("title")
        dic['completed'] = todo_[i].get('completed')
        dic['username'] = employee.get("username")
        li.append(dic)

    dictionary[str(arg1)] = li
    with open(f"{arg1}.json", "w") as file:
        json.dump(dictionary, file)
