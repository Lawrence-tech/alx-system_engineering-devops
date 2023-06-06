#!/usr/bin/python3
"""
Module that queries the Reddit API and returns the number of subscribers
"""

import requests
import sys


def number_of_subscribers(subreddit):
    '''
    Makes an API call to retrieve the number of subscribers in a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit to check the number of
        subscribers.

    Returns:
        int: The number of subscribers in the subreddit. Returns 0 if the
        API call fails.
    '''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers={'User-agent': 'my-bot'})

    if data.status_code == 200:
        # Extract the number of subscribers from the JSON response
        return data.json().get('data').get('subscribers')
    else:
        # Return 0 if the API call fails
        return 0
