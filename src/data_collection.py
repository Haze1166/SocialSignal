# src/data_collection.py
import tweepy
import pandas as pd
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET  # Import from config

def get_tweets(topic, count=100):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweets = []
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=topic, lang="en", tweet_mode='extended').items(count):
            tweets.append(tweet)
    except tweepy.TweepyException as e:
        print(f"Error during API call: {e}")
        return []  # Return an empty list on error
    return tweets

def tweets_to_dataframe(tweets):
    """Converts a list of tweet objects to a Pandas DataFrame."""
    if not tweets:  # Handle empty list case
        return pd.DataFrame() #return empty dataframe

    tweet_data = []
    for tweet in tweets:
        tweet_data.append({
            "tweet_id": tweet.id_str,
            "created_at": tweet.created_at,
            "text": tweet.full_text,
            "user_screen_name": tweet.user.screen_name,
            "user_location": tweet.user.location,
        })
    return pd.DataFrame(tweet_data)