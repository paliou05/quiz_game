import welcome_message
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
         
if __name__ == '__main__':
    printer = Printer()
    questions = printer.find_question()
    for question in questions:
        print question['question']+"\n"
        list = question['options']
        print list[0]
        print list[1]
        print list[2]
        print list[3]
        user_answer = input("Give your answer\n>")
        if user_answer == question['answer']:
            print "Correct\n"
        else:
            print "Wrong\n"
        print raw_input("For the next question press ENTER\n>")
        
            
    
    
    

    