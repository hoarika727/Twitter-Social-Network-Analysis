import sys
import tweepy
import time
from keys import key

API_KEY = key['api_key']
API_SECRET = key['api_secret']
ACCESS_TOKEN = key['access_token']
ACCESS_TOKEN_SECRET = key['access_token_secret']
target_ac = "WeAreNetflix"

try:
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    follower_ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=target_ac).pages():
        follower_ids.extend(page)
    #print (follower_ids, len(follower_ids))
    with open('follower_list.txt','w') as file1:
        for id in follower_ids:
            file1.write("%s\n" % id)

    followee_ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=target_ac).pages():
        followee_ids.extend(page)
    #print(followee_ids, len(followee_ids))
    with open('followee_list.txt','w') as file2:
        for id in followee_ids:
            file2.write("%s\n" % id)

except tweepy.TweepError:
    print ("tweepy.TweepError=", tweepy.TweepError)
except:
    e = sys.exc_info()[0]
    print ("Error: %s" % e)

