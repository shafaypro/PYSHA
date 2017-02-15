import tweepy
import time


# Twitting functions are in the below class regarding to the twitter
# TODO: add other things of the twitter api's like messages and others
class Twitter_PYSHA:
    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''
    api = None

    def __init__ (self, consumer_key='', consumer_secret="", access_token_key="", access_token_secret=""):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

    # Authorizes using all keys and secrets
    def _get_auth (self):
        try:  # multiple if used for accurate missing value stating
            if self.consumer_key != "":
                if self.consumer_secret != "":
                    if self.access_token_key != "":
                        if self.access_token_secret != "":
                            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
                            auth.set_access_token(self.access_token_key, self.access_token_secret)
                            return auth  # Auth handler returned
                        else:
                            print("access token secret not found")
                            return None
                    else:
                        print("access token key not found")
                        return None
                else:
                    print("consumer secret key not found")
                    return None
            else:
                print("consumer key not found")
                return None
        except Exception as e:
            print("Authentication problem error : ", e)
            return None

    def _api_auth (self):
        api = tweepy.API(self._get_auth())
        self.api = api
        return api

    def _check_public_tweets_home (self, api):  # returns the current profile tweets
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def _follow_all (self):  # Follows every follower of the authenticated user
        for follower in tweepy.Curson(self.api.followers).items():
            print("Followed ..")
            follower.follow()

    def limit_handled (self, cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                time.sleep(15 * 60)

    def __update_tweet (self, tweet_string):
        try:
            self.api.update_status(tweet_string)
            print("tweet Successfully tweeted...")
        except:
            print('Tweet Error ')
            # .###.....
