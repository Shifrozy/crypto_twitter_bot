from twitter_handler import get_latest_tweets
from chain_detector import detect_chain
from trader import send_transaction, buy_token

def process_tweet(tweet, default_amounts):
    words = tweet.split()
    for word in words:
        chain = detect_chain(word)
        if chain:
            if word.startswith("http"):
                # Simulate token buy
                amount = default_amounts.get(chain, 0.01)
                buy_token(chain, word, amount)
            else:
                # Assume wallet
                amount = default_amounts.get(chain, 0.01)
                send_transaction(chain, word, amount)

if __name__ == "__main__":
    # Ask the user for a Twitter handle instead of hardcoding
    username = input("Enter Twitter username (without @): ").strip()
    print("Monitoring tweets from:", username)

    tweets = get_latest_tweets(username, limit=10)
    mock_defaults = {"ethereum":0.01, "bsc":0.05, "polygon":0.1}
    
    for t in tweets:
        print("Tweet:", t)
        process_tweet(t, mock_defaults)