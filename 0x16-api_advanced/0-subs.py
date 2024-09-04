#!/usr/bin/python3
"""
Script that retrieves the subscriber count of a specified Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Fetch and return the total number of subscribers for a subreddit."""
    api_endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyCustomAgent"}
    response = requests.get(api_endpoint, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        response_data = response.json()
        subscriber_count = response_data.get('data', {}).get('subscribers', 0)
        return subscriber_count
    else:
        return 0
