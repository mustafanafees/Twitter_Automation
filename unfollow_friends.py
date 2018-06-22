#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:31:06 2018

@author: Mushi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:34:50 2018

@author: Mushi
"""

import tweepy
from keys import *
from datetime import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

from_date = date.today()-timedelta(days=60)

friends=api.friends_ids('mustafanafees')

#for friend in tweepy.Cursor(api.friends).items():
#    # Process the friend here
#    print(friend.)

for friend in friends:
    try:
        tweet = api.user_timeline(id = friend, count = 1)
        if tweet:
            tweet_date = tweet[0].created_at
            if(tweet_date.date() < from_date):
                print(tweet_date.date())
                api.destroy_friendship(friend)
                sleep(5)
    except tweepy.TweepError as error:
        print('\nError. Dont know what happened ')
        print(error.reason)
    except StopIteration:
        break