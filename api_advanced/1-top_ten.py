#!/usr/bin/python3
"""Script that fetches the titles of the first 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a valid subreddit, or None if invalid."""
    headers = {'User-Agent': 'MyRedditAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json().get('data', {})
        posts = json_data.get('children', [])
        if posts:
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    else:
        print(None)
