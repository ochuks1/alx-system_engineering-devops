#!/usr/bin/python3
"""
Script to display the titles of hot posts from a specified Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Output the titles of the top 10 hot posts for a given subreddit."""
    # Form the URL to fetch the hot posts in JSON format for the subreddit
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set up headers for the HTTP request, including a custom User-Agent
    headers = {
        "User-Agent": "custom-user-agent:0x16.api.advanced:v1.0.0 (by /u/example_user)"
    }

    # Parameters to limit the result to 10 hot posts
    parameters = {
        "limit": 10
    }

    # Execute the GET request to fetch the hot posts
    response = requests.get(api_url, headers=headers, params=parameters, allow_redirects=False)

    # Handle the case where the subreddit is not found (404 error)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON data and navigate to the 'data' section
    data_section = response.json().get("data")

    # Extract and print the titles of the 10 hottest posts
    [print(post.get("data").get("title")) for post in data_section.get("children")]
