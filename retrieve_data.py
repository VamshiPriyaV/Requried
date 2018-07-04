import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection['db_sample']
record1 = db['collection_name']
cursor = record1.find()

for doc in cursor:
	#print doc
	print doc['_id']

