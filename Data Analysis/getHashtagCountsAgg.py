#gets count of all hashtags used

from pymongo import MongoClient
import cPickle as pickle

client = MongoClient()
db = client.twitter

tweets = db.tweets

pipeline = [
	{"$unwind": "$entities.hashtags"},
	{"$group": {"_id": "$entities.hashtags.text", "count": {"$sum": 1}}}

]

x = tweets.aggregate(pipeline, allowDiskUse=True)
htags = {}
for dic in x:
	htags[dic['_id']] = dic['count']

pickle.dump(htags, open('htags3.p', 'wb'))

'''
pipeline = [
	{ "$sample": { "size": 5 } },
	{"$unwind": "$entities.hashtags"},
	{"$group": {"_id": "$entities.hashtags.text", "count": {"$sum": 1}}}

]

'''