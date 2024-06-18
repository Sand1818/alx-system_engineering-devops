#!/usr/bin/python3
"""parses title of all hot articles and prints sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, after=None, dicti=None):
    """Returns list containing titles of all hot articles"""
    if dicti is None:
        dicti = {word: 0 for word in word_list}

    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    respon = requests.get(url, headers={'User-Agent': 'Sand1'})

    if respon.status_code != 200:
        return

    hot = respon.json()
    for article in hot['data']['children']:
        for word in word_list:
            if f" {word.lower()} " in article['data']['title'].lower():
                dicti[word] += 1

    after = hot['data']['after']
    if not after:
        print(dicti)
        dicti_sort = dict(sorted(dicti.items()))
        for key, value in dicti_sort.items():
            if value:
                print(f"{key}: {value}")
        return
    return (count_words(subreddit, word_list, after, dicti))
