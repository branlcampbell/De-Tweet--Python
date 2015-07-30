__author__ = 'Brandon Campbell'

import tweepy

''' De-Tweet will erase your account of all tweets that have been made.
    To fill in the key and token fields, go to https://dev.twitter.com/apps '''

consumer_key = "######"
consumer_secret = "######"
# Fill in these fields with the information given on Twitter's developer web site.
access_token = "######"
access_token_secret = "######"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # Checks for valid consumer credentials.
auth.secure = True
auth.set_access_token(access_token, access_token_secret)  # Checks for valid access credentials.

api = tweepy.API(auth)


def massDelete(api):
    print("Are you sure you want to delete all of your Tweets? This change cannot be undone.")
    confirm = input("Type Y if you wish to delete all tweets. ")
    if confirm.upper() == "Y":
        for status in tweepy.Cursor(api.user_timeline).items():  # Represents each individual tweet.
            try:
                api.destroy_status(status.id)
                print("Deleted ", status.id)
            except:
                print("Could not delete ", status.id)

massDelete(api)
