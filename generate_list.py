import tweepy
from time import sleep
from keys import *
from datetime import date, timedelta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

lastfewdays = date.today() - timedelta(3)


for tweet in tweepy.Cursor(api.search, q='#DataScience OR #AI OR  #IoT OR #MachineLearning OR #DeepLearning').items(100):
    try:
        if (tweet.created_at.date()>=lastfewdays) and (tweet.lang=='en') and (tweet.retweet_count>10):
            print(tweet.user.id)
            
            try:
                api.add_list_member(slug='datascience', id=tweet.user.id, owner_screen_name = 'mustafanafees')
            except tweepy.TweepError as error:
                print ("cannot add: " + error.reason)
            
            sleep(10)
        else:
            print('Mismatch criteria to add to the list.')
        

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Detail: ')
        print(error.reason)

    except StopIteration:
        break
