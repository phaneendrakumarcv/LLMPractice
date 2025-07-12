import tweepy
import requests
from dotenv import load_dotenv
load_dotenv()
import os

def scrape_user_tweets(username, num_tweets=5):
    """
    scrapes tweets from the user's tweets from twitter and returns them as list of dictonaries,
    Each dictionary has three keys "time_posted(relative to now)", "text", "url"
    :param username: 
    :param num_tweets: 
    :return: 
    """
    bearer_token = os.environ["TWITTER_BEARER_TOKEN"]
    consumer_key = os.environ["TWITTER_API_KEY"]
    consumer_secret = os.environ["TWITTER_API_KEY_SECRET"]
    access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    access_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    twitter_client = tweepy.Client(bearer_token,consumer_key,consumer_secret,access_token,access_secret)
    tweet_list = []

    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(id=user_id,max_results=num_tweets,exclude=["retweets","replies"])
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)
    return tweet_list




if __name__ == "__main__":
    tweets = scrape_user_tweets(username="elonmusk")
    print(tweets)