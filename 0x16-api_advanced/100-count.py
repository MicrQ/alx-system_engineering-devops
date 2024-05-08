#!/usr/bin/python3
""" a function that queries the Reddit API """


def count_words(subreddit, word_list, count={}):
    """ counts the number of occurrences of words in a given subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Some-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code >= 300:
        return count

    data = res.json().get('data')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            if word in title:
                count[word] = count.get(word, 0) + 1
    if data.get('after'):
        return count_words(subreddit, word_list, count)
    else:
        return count
