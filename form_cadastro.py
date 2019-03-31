import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://victorsodre:ghZATpQEN6Zvv8W@cluster0-iqb96.mongodb.net/test?retryWrites=true")
db = client.test
dbcollectionname = "messages"


def saveCadastro(item):
	dbcollection = db[dbcollectionname]
	itemid = dbcollection.insert_one(item).inserted_id
	return str(itemid)


def listCadastro():	
	dbcollection = db[dbcollectionname]	
	cursor = dbcollection.find().sort("timestamp", -1).limit(10) 
	return dumps(cursor)