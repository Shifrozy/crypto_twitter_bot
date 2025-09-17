# twitter_handler.py
import tweepy

def get_latest_tweets(username, limit=5):
    client = tweepy.Client(bearer_token="YOUR_TWITTER_BEARER_TOKEN")
    user = client.get_user(username=username)
    tweets = client.get_users_tweets(user.data.id, max_results=limit)
    return [t.text for t in tweets.data]