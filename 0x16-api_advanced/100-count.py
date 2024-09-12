#!/usr/bin/python3
"""
Function to count specific words in the titles of hot posts from a subreddit.
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, fetches the titles of
        hot articles, and counts occurrences of specified keywords.
    """
    if not subreddit or not word_list:
        return

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyUserAgent"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(api_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        articles = json_data.get("data", {}).get("children", [])

        for article in articles:
            title = article.get("data", {}).get("title", "").lower()
            for keyword in word_list:
                lower_keyword = keyword.lower()
                counts[lower_keyword] = counts.get(lower_keyword, 0) + title.split().count(lower_keyword)

        next_page = json_data.get("data", {}).get("after", None)
        if next_page:
            count_words(subreddit, word_list, after=next_page, counts=counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return
