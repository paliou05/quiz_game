import pymongo


class QuestionPrinter():

    
    def __init__(self):
        self.db = self.connect_to_db('test')
        
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    
    def find_question(self,number_of_questions):
        query = {}
        selector = {'_id':1,'question':1, 'answer':1, 'options':1}
        questions = self.db.questions.find(query,selector).limit(number_of_questions)
        return questions
         
"""if __name__ == '__main__':
    correct = 0
    wrong = 0
    score = 0
    average = 0
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
            correct = correct + 1
            score = score + 10
        else:
            print "Wrong\n"
            wrong = wrong + 1
        print raw_input("For the next question press ENTER\n>")
    average = (correct/float(correct+wrong))*100
    print "Your score:",score
    print "You have %d correct answers" %correct
    print "Your average:%d" %average+"%"    """
            
    
    
    

    