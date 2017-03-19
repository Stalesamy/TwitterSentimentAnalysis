import tweepy, time, sys

argfile = str(sys.argv[1])

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(900)

text = input('')
blob = TextBlob(text)

for sentance in blob.sentances:
	print(sentance.sentiment.polarity)
