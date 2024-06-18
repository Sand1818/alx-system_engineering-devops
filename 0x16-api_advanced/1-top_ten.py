#!/usr/bin/python3
"""request top ten posts of a subreddit"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts listed for given subreddit"""
    header = {'User-Agent':  'Sand1'}
    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    respon = requests.get(url, headers=header)

    if respon.status_code == 200:
        list_of_hot = respon.json()["data"]["children"]

        posts_count = 0
        for hot in list_of_hot:
            if posts_count == 10:
                break
            print(hot["data"]["title"])
            posts_count += 1
    else:
        print("None")
