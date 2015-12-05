import random
import pymongo
import datetime
import re
import uuid
import settings

mongo_client = pymongo.MongoClient(settings.mongo_host, settings.mongo_port)
mongo_db = mongo_client.restate

def get_next_sequence(name):
    ret = mongo_db.counters.find_and_modify(query={'_id': name}, update={'$inc': {'seq': 1}}, new=True)
    if not ret:
        doc = {'_id':name,'seq':1}
        mongo_db.counters.insert(doc)
        return doc['seq']
    return ret['seq']

def get_user_by_email(email):
    return mongo_db.users.find_one({'email':email})

def get_agents():
    return list(mongo_db.users.find({'is_agent':1}))