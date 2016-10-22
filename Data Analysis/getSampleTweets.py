#gets 5 sample tweets from the collection

from pymongo import MongoClient
from pprint import pprint


client = MongoClient()
db = client.twitter

tweets = db.tweets

pipeline = [
	{ "$sample": { "size": 5 } }
]

samp = tweets.aggregate(pipeline, allowDiskUse=True)
i = 1
for x in samp:
	with open('tweet_example{0}.txt'.format(i), 'wt') as out:
		pprint(x, stream=out)
	i+=1