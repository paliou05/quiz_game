import pymongo
import os
import json

class Printer():
    
    def __init__(self):
        self.db = self.connect_to_db('test')
        
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    
    def find_question(self):
        query = {}
        selector = {'_id':1,'question':1, 'answer':1, 'options':1}
        questions = self.db.questions.find(query,selector)
        return questions
                        
    def print_question(self,query,selector):
        ask = self.db.questions.find(query,selector)
        print ask
        
            
if __name__ == '__main__':
    printer = Printer()
    questions = printer.find_question()
    for question in questions:
            question_id = question['_id']
            query = {'_id':question_id}
            selector = {'question':1, 'options':1,'answer':0}
            printer.print_question(query,selector)
            
    
    
    

    