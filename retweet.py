import tweepy
from time import sleep
from keys import *
from datetime import date, timedelta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!

tweet_origin = []

#Dont change this
postcount = 0

lastfewdays = date.today() - timedelta(2)


for tweet in tweepy.Cursor(api.search, q='#DataScience OR #AI OR  #IoT OR #MachineLearning OR #DeepLearning').items(100):
    try:
        if (tweet.user.screen_name not in tweet_origin) and (tweet.created_at.date()>=lastfewdays) and (tweet.lang=='en') and (tweet.retweet_count>10):
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
            tweet.retweet()
            tweet_origin.append(tweet.user.screen_name)
            #print(tweet)
            print('Retweet published successfully.')
            postcount+=1;
            sleep(10)
            if(postcount>=5):
                break
        else:
            print('Retweet condition doesnot match.')
        

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet failure. Detail: ')
        print(error.reason)

    except StopIteration:
        break
