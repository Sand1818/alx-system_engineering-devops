#!/usr/bin/python3
"""Requests number of subscribers using the reddit api"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for given subreddit"""
    header = {'User-Agent': 'Sand1'}
    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    respon = requests.get(url, headers=header)
    if respon.status_code == 200:
        subs = respon.json()["data"]["subscribers"]
    else:
        subs = 0
    return subs
