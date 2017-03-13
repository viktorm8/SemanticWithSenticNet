#Sentiment Analysis with Python

#First Step: Access to tweet

#Second Step: get the polarity of sentiment analysis

#Third Step: Analysis of a case of a public interest.
            #Example: OSINT on Trump Victory. Then verify the Trump Victory
            #through OSINT of tweets.

#Coded By Daniele Cannarsa
#Copyright 2017 - Tutti i diritti riservati

import tweepy
from textblob import TextBlob

consumer_key = 'uAzSRIhykkh38dbD9f3rftHvJ'
consumer_secret = 'xQbzXVy5cjz5P6feg6b3sIhMtYcbcnhSXzFsI8I4v2rTERpjlk'

access_token = '3162981567-EKolFYFDlTpBgjSDfog8EEot91fXnb2UgdLNtAQ'
access_token_secret = 'JWJTT5IvKOxae8X2zXglGBZcIQcKbzpqYaVfhmpBq9QFB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Cyber Security')
#public_tweets = api.home_timeline()


for tweet in public_tweets:
    print(tweet.text,"\n")
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment,"\n\n\n")
