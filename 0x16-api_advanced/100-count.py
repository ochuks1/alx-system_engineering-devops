#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
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
                count_words(subreddit, word_list, hot_list, after)
            else:
                word_count = {}
                for title in hot_list:
                    words = title.lower().split()
                    for word in words:
                        word = word.rstrip('.,!?')
                        if word in word_list:
                            if word in word_count:
                                word_count[word] += 1
                            else:
                                word_count[word] = 1
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
        else:
            print(None)
    else:
        print(None)


