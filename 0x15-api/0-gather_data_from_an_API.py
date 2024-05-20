#!/usr/bin/python3
"""
Using this REST API, for given employee ID
returns information about thi TODO list progress
"""
import requests
import sys


if __name__ == "__main__":

    user_id = sys.argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id)
        )
    name = r.json()['name']
    r = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                user_id)
            )
    total = len(r.json())
    done = 0
    for task in r.json():
        if task['completed'] is True:
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in r.json():
        if task['completed'] is True:
            print("\t {}".format(task['title']))
