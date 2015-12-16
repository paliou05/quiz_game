import pymongo
import os


class UserScores():
    
    def __init__(self):
        self.db = self.connect_to_db('test')
        
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    
    def get_username(self):
        username = input("Give your username:\n>")
        return username
    
    def import_userdb(self,username,score):    
        self.db.users.insert({'username':username},{'score':score})
    
    def find_users(self):
        all_users = self.db.users.find(query,selector)
        return all_users
    
    def print_userscores():
        """SORT DESCEDING"""


"""1)add main.py
   2)add choice of game(5,10,15,20?)
   3)print users and scores to txt?
   4)add the questions"""
    
        