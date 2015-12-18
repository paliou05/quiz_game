import welcome_message
import pymongo
from questions import QuestionPrinter
from userscores import UserScores
from count_seconds import TimeCounter


if __name__ == "__main__":
    correct = 0
    wrong = 0
    score = 0
    average = 0
    timer = TimeCounter()
    question_printer = QuestionPrinter()
    questions = question_printer.find_question()
    for question in questions:
        timer.start()
        print question['question']+"\n"
        options_list = question['options']
        for option in options_list:
            print option
        user_answer = input("Give your answer\n>")
        seconds = timer.finish()
        print("You took {} seconds to answer the question".format(seconds))
        if user_answer == question['answer']:
            print "Correct\n"
            correct = correct + 1
            score = (score + 50)-(seconds*2)
        else:
            print "Wrong\n"
            print "The correct answer is:", question['answer']
            wrong = wrong + 1
            score = score - (seconds*2)
        print raw_input("To continue press ENTER\n>")
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
    