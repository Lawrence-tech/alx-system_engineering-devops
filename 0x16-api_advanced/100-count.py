#!/usr/bin/python3
"""
Module that queries the Reddit API, parses the title of all hot articles, and
prints a sorted count of given keywords (case-insensitive, delimited by spaces
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    '''
    Recursive function that queries the Reddit API, parses the titles of all,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): List of keywords to count occurrences of.
        after (str): Parameter used for pagination. Default is None.
        count_dict (dict): Dictionary to store keyword counts. Default is None

    Returns:
        None
    '''

    if count_dict is None:
        count_dict = {}

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
                title = post.get('data').get('title')
                words = title.split()

                for word in words:
                    word = word.lower()
                    if word in word_list:
                        if word in count_dict:
                            count_dict[word] += 1
                        else:
                            count_dict[word] = 1

            after = data.get('data').get('after')

            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)

    sorted_counts = sorted(count_dict.items(), key=lambda x:
                           (-x[1], x[0].lower()))

    for keyword, count in sorted_counts:
        print(f"{keyword.lower()}: {count}")
