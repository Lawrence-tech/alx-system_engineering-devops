#!/usr/bin/python3
"""
Module that queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    '''
    Recursive function that queries the Reddit API and returns a list of titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list): List to store the titles of hot articles.
        Default is None.
        after (str): Parameter used for pagination. Default is None.

    Returns:
        list or None: List of titles if hot articles are found, otherwise None.
    '''

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'my-bot'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')

        if posts:
            for post in posts:
                hot_list.append(post.get('data').get('title'))

            after = data.get('data').get('after')

            if after is not None:
                return recurse(subreddit, hot_list, after)

        return hot_list

    return None
