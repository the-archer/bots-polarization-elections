import tweepy
from pymongo import MongoClient
import logging

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        insertIntoDB(status)

    def on_error(self, status_code):
        """This is called when an error occurs"""
        logging.error(repr(status_code))
        print('Error: ' + repr(status_code))
        return False

def loadKeys(fileName):
	keys = []
	with open(fileName, "r") as f1:
		for line in f1:
			keys.append(line.rstrip('\n'))
	return keys


def loadKeywords(fileName):
	kwords = []
	with open(fileName, "r") as f1:
		for line in f1:
			kwords.append(line.rstrip('\n'))
	return kwords


def insertIntoDB(tweet):
	print tweet.text
	db.tweets.insert(tweet._json)

logging.basicConfig(filename='datacollection.log',level=logging.DEBUG)


consumer_key, consumer_secret, access_token, access_token_secret = loadKeys("keys.txt")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

kwords = loadKeywords("keywordslist.txt")

client = MongoClient()
db = client.twitter


myStream.filter(track=kwords)
