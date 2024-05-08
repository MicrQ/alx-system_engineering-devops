#!/usr/bin/python3
""" a function that queries the Reddit API """


def recurse(subreddit, hot_list=[]):
    """ a function that queries the Reddit API """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Some-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code < 300:
        data = res.json().get('data')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if data.get('after'):
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
