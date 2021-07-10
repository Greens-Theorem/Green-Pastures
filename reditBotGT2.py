#July 2021 | Reddit Bot
import praw
import re
import pathlib

reddit = praw.Reddit('GreenTheoremsBot')
f = pathlib.Path("comments_replied_to.txt")

if not f.exists():
	comments_replied_to = []

else:
	with open("comments_replied_to.txt", "r") as f:
		comments_replied_to = f.read()
		comments_replied_to = list(filter(None, comments_replied_to.split("\n")))
subreddit = reddit.subreddit('walmart')
for comment in subreddit.comments(limit=5):
    if comment.id not in comments_replied_to:
        if "?PPTO" in comment.body:
            comment.reply("You do not need to use 16 hours of PPTO to cover a key event date. You only need to use enough to cover your shift total hours, just like any other day.")
            print ("Replied to comment " + comment.id)
            comments_replied_to.append(comment.id)

with open ("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment.id + "\n")	
