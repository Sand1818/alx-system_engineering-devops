#!/usr/bin/python3
"""
Export data in the CSV format
from RestAPI
"""

import requests
import csv
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        username = req.json().get("username")
        url2 = 'https://jsonplaceholder.typicode.com/todos'
        r2 = requests.get(url2)
        filename = sys.argv[1] + '.csv'
        with open(filename, 'w') as f:
            writ = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
            for item in r2.json():
                if item.get("userId") == int(sys.argv[1]):
                    line = [item.get("userId"),
                            username,
                            str(item.get("completed")),
                            item.get('title')]
                    writ.writerow(line)
