#!/usr/bin/python3

"""
Module that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    '''
    Makes an API call to retrieve the top ten hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to check.

    Returns:
        None
    '''

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        allow_redirects=False)

    if data.status_code == 200:
        # Extract the list of posts from the JSON response
        post_list = data.json().get('data').get('children')
        count = 0
        for post in post_list:
            if count == 10:
                break
            # Print the title of each post
            print(post.get("data").get("title"))
            count += 1
    else:
        # Print "None" if the API call fails
        print("None")
