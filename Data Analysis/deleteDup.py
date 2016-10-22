#Delete duplicate tweets

from pymongo import MongoClient

client = MongoClient()
db = client.twitter8

cursor = db.tweets.aggregate(
    [
        {"$group": {"_id": "$id_str", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
        {"$match": {"count": { "$gte": 2 }}}
    ], allowDiskUse = True

)

response = []
for doc in cursor:
    del doc["unique_ids"][0]
    for id in doc["unique_ids"]:
        response.append(id)

db.tweets.remove({"_id": {"$in": response}})