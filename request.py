import praw

reddit = praw.Reddit(client_id='id',
                     client_secret='secret',
                     password='password',
                     user_agent='/all/top grabber script by /u/cbkatx',
                     username='cbkatx')

top_posts = []

for submission in reddit.subreddit('all').top('hour', limit = 5):
    top_posts.append(submission.author)
    top_posts.append(submission.comments)
    top_posts.append(submission.subreddit)
    top_posts.append(submission.title)
    

print(top_posts)