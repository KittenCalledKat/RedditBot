import praw
import pdb
import re
import os
import json
from redditpuller import RedditPuller

def main():
    rp = RedditPuller('joke_bot','Jokes')
    top_new_joke = rp.get_unique_top()

    print(top_new_joke)

    rp.write_files()


class Post(object):
    def __init__(self, title, text):
        self.title = submission.title
        self.text = submission.selftext
        raise NotImplementedException()

main()
