#!/usr/bin/python3
""" a function that queries the Reddit API """


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API
        and returns the number of subscribers
    """
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                       allow_redirects=False)
    if res.status_code < 300:
        data = res.json().get('data')
        return data.get('subscribers')
    return 0
