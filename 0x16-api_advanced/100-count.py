#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests
import sys

def add_title(dictionary, hot_posts):
    if not hot_posts:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        word = word.lower()
        if word in dictionary:
            dictionary[word] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)

def recurse(subreddit, dictionary, after=None):

def count_words(subreddit, word_list):
    dictionary = {}

    for word in word_list:
        dictionary[word.lower()] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))

    for word, count in sorted_items:
        if count > 0:
            print(f"{word}: {count}")
