#!/usr/bin/python3
"""
Recursive function returns list containing titles of
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns list of titles of all hot posts on a given subreddit"""
    lin = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Sand1"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    respon = requests.get(lin, headers=headers, params=params,
                            allow_redirects=False)
    if respon.status_code == 404:
        return None

    results = respon.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for chil in results.get("children"):
        hot_list.append(chil.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
