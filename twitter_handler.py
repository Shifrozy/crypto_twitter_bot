import snscrape.modules.twitter as sntwitter

def get_latest_tweets(username, limit=5):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
        if i >= limit:
            break
        tweets.append(tweet.content)
    return tweets