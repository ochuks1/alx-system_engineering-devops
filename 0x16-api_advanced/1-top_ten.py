#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        print(None)


