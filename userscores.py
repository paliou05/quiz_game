import pymongo
import os


class UserScores():
    
    def __init__(self):
        self.db = self.connect_to_db('test')
        
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    
    score = 0
    username = input("Give your username:\n>")
    #self.db.users.insert({'username':username},{'score':score})
    
