from pymongo import MongoClient

MONGO_DB_NAME = "safemaxdb"
MONGO_URI ="mongodb+srv://kskkoushik135:LQCFjoGmTHFyIdRi@cluster0.zzxbiby.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
