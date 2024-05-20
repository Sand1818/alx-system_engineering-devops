#!/usr/bin/python3
"""
Using this REST API, for given employee ID
returns information about thi TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    res = requests.get(url1)
    name = res.json().get("name")
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    res2 = requests.get(url2)
    taskname = []
    task = 0
    complete = 0
    for item in res2.json():
        if item.get("userId") == int(sys.argv[1]):
            task += 1
            if item.get("completed") is True:
                complete += 1
                taskname.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          complete,
                                                          task))
    for i in taskname:
        print("\t {}".format(i))
