import welcome_message
import pymongo
from questions import Printer
from userscores import UserScores

if __name__ == "__main__":
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
    print "Your average:%d" %average+"%"
    userscores = UserScores()
    username = userscores.get_username()
    #score = randint(10,50)   #for the test(must remove after and take the score from questions.py)
    userscores.import_userdb(username,score)  #maybe check for same username?
    query = {}
    selector = {'username':1 , 'score':1 , "_id":0}
    all_users = userscores.find_users(query,selector)
    users = [user for user in all_users]
    user = sorted(users, reverse=True)
    for i in user:
        print i['username'],"\tscore:",i['score']
    