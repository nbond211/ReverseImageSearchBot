import tweepy
import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

class TwitterAPI:
    def __init__(self):
        consumer_key = "SkMIlX4xHTiETAPf25o3PpTfj"
        consumer_secret = "OjokAnVUVlVBgJ4Umm71ALKHDJjTKHZXmXfkH26kpFFAnxdatH"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3709897817-4aWMMfWBA6nuzPvTT220lsQgJxkeTlM5g9dbGMN"
        access_token_secret = "tOhekE0owzUv4yFoBrLHNLxA3WQKsXLXnYKiSM6uLDy13"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(random.choice(WORDS).decode("utf-8"))