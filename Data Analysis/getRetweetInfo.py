#creates retweet graph from mongodb collection

from pymongo import MongoClient
import cPickle as pickle

client = MongoClient()
db = client.twitter

tweets = db.tweets

x = tweets.find({'retweeted_status' : {'$exists': True}}, {'user.screen_name': 1, 'retweeted_status.user.screen_name': 1})
y = list(x)

pickle.dump(y, open('retweet_graph.p', 'wb'))	