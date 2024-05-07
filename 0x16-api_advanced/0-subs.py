#!/usr/bin/python3
""" a function that queries the Reddit API """


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API
        and returns the number of subscribers
    """
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        data = r.json()
        return data['data']['subscribers']
    return 0
