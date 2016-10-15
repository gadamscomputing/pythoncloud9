#-------------------------------------------------------------------------------
# Name:        CodePractice
# Purpose:
#
# Author:      gadamslr
#
# Created:     30/01/2016
# Copyright:   (c) gadams 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import modules'
import random
import time
import csv
import os

# set variable counters to 0
questionCounter = 0
userScore = 0


#import the csv files
if os.path.isfile("quizResults.csv"):
    print("True")
    file = open("quizResults.csv", "a")
else:
    print("Create a file")
    file = open("quizResults.csv", "wb")

# Quiz function
def quiz():
    number01 = random.randint(0,10)
    number02 = random.randint(0,10)
    mathSymbols = ["+","-","*"]
    randOperator = random.choice(mathSymbols)
    userScoreL = 0

    print(number01)
    print(number02)
    print(randOperator)

    userAnswer = input("What is the answer to: %s %s %s?" % (number01, randOperator, number02))
    quizQuestion = eval(str(number01) + randOperator + str(number02))

    if int(quizQuestion) == int(userAnswer):
        print("correct")
        userScoreL = userScoreL + 1
    else:
        print("Oncorrect")
    return(userScoreL)

while questionCounter < 3 :
    print(("Your score is: %s" % userScore))
    userScore = userScore + quiz()

    print(("Your score is: %s" % userScore))
    questionCounter = questionCounter + 1
    print(("Question number %s") % questionCounter)



userName = input("What is your name?")
print("%s, your score was %s out of %s questions on the %s" % (userName, userScore, questionCounter, time.strftime('%d-%m-%Y')))

file.write("%s, %s, %s, %s\n" % (userName, userScore, questionCounter, time.strftime('%d-%m-%Y')))
file.close()


data = csv.reader(open('quizResults.csv'),delimiter=',')

import operator
print("Alphabetical order.")
sortedlist = sorted(data, key=operator.itemgetter(0), reverse=False)
for x in sortedlist:
    print(sortedlist)
    print(x)

data = csv.reader(open('quizResults.csv'),delimiter=',')

print("Alphabetical order in reverse.")
sortedAlphRev = sorted(data, key=operator.itemgetter(0), reverse=True)
print(sortedAlphRev)

data = csv.reader(open('quizResults.csv'),delimiter=',')

print("Scores highest to lowest.")
sortedScores = sorted(data, key=operator.itemgetter(1), reverse=False)
print(sortedScores)

returnedScore = operator.itemgetter(1)
print(returnedScore)

#csv.reader(close())
