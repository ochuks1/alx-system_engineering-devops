#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, counts={}, after=None):
    # Set up the custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Convert word_list to lowercase for case-insensitive matching
    word_list = [word.lower() for word in word_list]
    
    # Send the GET request to the Reddit API with pagination support using `after`
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and contains the needed data
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                counts[word] = counts.get(word, 0) + title.split().count(word)
        
        # Handle pagination
        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            # Sort and print the counts
            sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return None
