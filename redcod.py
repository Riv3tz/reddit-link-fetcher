import praw

reddit = praw.Reddit(client_id="Your client id here",
                     client_secret="Your reddit client here",
                     user_agent="my user agent")

for submission in reddit.subreddit("CODWarzone").hot(limit=20):
    print("\n" + submission.url)