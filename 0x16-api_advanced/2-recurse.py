#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if children:
            for post in children:
                hot_list.append(post.get('data', {}).get('title'))
            after = data.get('after', None)
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    else:
        return None


