from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

DB_NAME = "ScalablePath"
username = "carballofacundo70"
password = "4SOeCeyBjdqs56zX"

uri = "mongodb+srv://" + username + ":" + password + "@scalablepath.nounvbz.mongodb.net/?retryWrites=true&w=majority"

def create_client():
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
    except Exception as e:
        print("Error connecting to mongo db. " + str(e))
    
    return client

def create_local_connection():
    return MongoClient("mongodb://localhost:27017/")