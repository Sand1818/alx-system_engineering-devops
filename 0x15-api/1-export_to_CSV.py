#!/usr/bin/python3
"""
Export data in the CSV format
from RestAPI
"""

import requests
import csv
import sys


if __name__ == '__main__':
    arg1 = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{arg1}/"
    response = requests.get(url)

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={arg1}"
    response2 = requests.get(url2)

    employee = response.json()
    todo_ = response2.json()

    total = len(todo_)

    with open(f'{arg1}.csv', mode='w', newline='') as csv_file:
        writ = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

        for i in range(total):
            line = []
            line.append(str(arg1))
            line.append(employee.get("username"))
            line.append(str(todo_[i].get('completed')))
            line.append(todo_[i].get("title"))

            writ.writerow(line)
