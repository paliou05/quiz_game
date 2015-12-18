import pymongo
import os
from random import randint

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
        self.db.users.insert({'username':username ,'score':score})
    
    def find_users(self,query,selector):
        all_users = self.db.users.find(query,selector)
        return all_users
    
    def print2txt(self,all_users): #didnt used it yet
        """SORT DESCEDING"""
        
    def print_userscores():  #could use it if i wanted to print them to a txt
        """print on screen from txt"""
    #def read_list(list_name):      maybe use it for iteration in my list
       #for i in list_name:         to fix my print output
          #print i

"""1)add main.py
   2)add choice of game(5,10,15,20?)
   3)add the questions
   4)check if they work all together"""
"""if __name__ == "__main__":
    userscores = UserScores()
    username = userscores.get_username()
    score = randint(10,50)   #for the test(must remove after and take the score from questions.py)
    #userscores.import_userdb(username,score)  #maybe check for same username?
    query = {}
    selector = {'username':1 , 'score':1 , "_id":0}
    all_users = userscores.find_users()
    users = [user for user in all_users]
    user = sorted(users, reverse=True)
    for i in user:
        print i['username'],"\tscore:",i['score']"""
    
    