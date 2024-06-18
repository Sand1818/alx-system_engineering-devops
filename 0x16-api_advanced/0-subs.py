#!/usr/bin/python3
"""Requests number of subscribers using the reddit api"""
import requests
import re


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about/"
    respon = requests.get(url)
    html = respon.text
    pattern = r'subscribers="([^"]*)"'
    subs = re.search(pattern, html)

    if subs:
        return int(subs[0][13:-1])
    else:
        return 0
