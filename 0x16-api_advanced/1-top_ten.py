#!/usr/bin/python3
""" a function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit
"""


def top_ten(subreddit):
    """ prints top 10 hot posts """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Some-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code < 300:
        data = res.json().get('data')
        children = data.get('children')
        for child in children:
            print(child.get('data').get('title'))
    else:
        print(None)
