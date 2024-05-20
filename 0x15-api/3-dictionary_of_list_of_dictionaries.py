#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    data = {}
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    resp2 = requests.get(url2)
    for item in resp2.json():
        if str(item.get('userId')) not in data:
            data[str(item.get('userId'))] = []
        url = 'https://jsonplaceholder.typicode.com/users?id='\
              + str(item.get('userId'))
        resp = requests.get(url)
        resp = resp.json()
        username = resp[0]['username']
        dictio = {}
        dictio['task'] = item.get('title')
        dictio['completed'] = item.get('completed')
        dictio['username'] = username
        data[str(item.get('userId'))].append(dictio)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as j:
        json.dump(data, j)
