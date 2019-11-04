import praw
import json

class RedditPuller(object):

    def __init__(self,secret_filename,subreddit_name):
        self.reddit = praw.Reddit(secret_filename)
        self.subreddit = self.reddit.subreddit(subreddit_name)
        self.pulled = []
        self.posted = []
        self.read_files()

    def read_files(self):
        #Read the file into a list and remove any empty values
        try:
            with open("submissions_pulled.json", "r") as f:
                self.pulled = json.loads(f.read())
        except FileNotFoundError:
            self.pulled = []

        #with open("submissions_posted.json", "r") as f:
        #    self.pulled = json.loads(f.read())

    def write_files(self):
        self.pulled = list(filter(None, self.pulled))
        with open("submissions_pulled.json", "w") as f:
            f.write(json.dumps(self.pulled))

    # Pulls the top x posts from the top list in the sub from the current day
    def pull_top_submissions(self, limit=10):
        return self.subreddit.top(time_filter='day', limit=limit)

    def filter_new_submission(self):
        for candidate in self.pull_top_submissions(10):
            if candidate.id not in self.pulled:
                return candidate
        return None

    def get_unique_top(self):
        item = self.filter_new_submission()
        self.pulled.append(item.id)

