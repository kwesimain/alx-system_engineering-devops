#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json()
    results = data['data']['children']
    hot_list.extend([article['data']['title'] for article in articles])
    after = data['data']['after']

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list

    elif response.status_code == 302:
        print(f"The subreddit '{subreddit}' does not exist or is invalid.")
        return None

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None
