# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:38:14 2016

@author: griffinmartin
Griffin Martin
mart1444@msu.edu
A45789968
"""
import random

difficulty_int = int(input('Input Difficulty  (int>= 2): '))
problems_int = int(input('Number of problems (int>=1): '))

if (difficulty_int < 2):
    print("Enter a number >=2")
elif (problems_int <1):
    print("Enter a number >=1")

score = 0

if (difficulty_int == 2):    
    for i in range (0,problems_int):
        rand1 = random.randint(0,99)
        rand2 = random.randint(0,99)
        rand_sum = 0
        print(rand1, end = " + ")
        print(rand2)
        rand_sum = rand1 + rand2
        answer_int = int(input('Your Answer: '))
        if (answer_int == rand_sum):
            print("Correct!")
            score = score + 1
        elif (answer_int != rand_sum):
            print("Wrong, the sum was", rand_sum)
    score_percent = (score / problems_int) * 100
    score_percent = (score / float(problems_int)) * 100
    print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int ==3):
        for i in range (0,problems_int):
            rand1 = random.randint(0,999)
            rand2 = random.randint(0,999)
            rand3 = random.randint(0,999)
            rand_sum = 0
            print(rand1, end = " + ")
            print(rand2, end = " + ")
            print(rand3)
            rand_sum = rand1 + rand2
            answer_int = int(input('Your Answer: '))
            if (answer_int == rand_sum):
                print("Correct!")
                score = score + 1
            elif (answer_int != rand_sum):
                print("Wrong, the sum was", rand_sum)
        score_percent = (score / problems_int) * 100
        score_percent = (score / float(problems_int)) * 100
        print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int ==4):
        for i in range (0,problems_int):
            rand1 = random.randint(0,9999)
            rand2 = random.randint(0,9999)
            rand3 = random.randint(0,9999)
            rand4 = random.randint(0,9999)
            rand_sum = 0
            print(rand1, end = " + ")
            print(rand2, end = " + ")
            print(rand3, end = " + ")
            print(rand4)
            rand_sum = rand1 + rand2
            answer_int = int(input('Your Answer: '))
            if (answer_int == rand_sum):
                print("Correct!")
                score = score + 1
            elif (answer_int != rand_sum):
                print("Wrong, the sum was", rand_sum)
        score_percent = (score / problems_int) * 100
        score_percent = (score / float(problems_int)) * 100
        print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int ==5):
        for i in range (0,problems_int):
            rand1 = random.randint(0,99999)
            rand2 = random.randint(0,99999)
            rand3 = random.randint(0,99999)
            rand4 = random.randint(0,99999)
            rand5 = random.randint(0,99999)
            rand_sum = 0
            print(rand1, end = " + ")
            print(rand2, end = " + ")
            print(rand3, end = " + ")
            print(rand4, end = " + ")
            print(rand5)
            rand_sum = rand1 + rand2
            answer_int = int(input('Your Answer: '))
            if (answer_int == rand_sum):
                print("Correct!")
                score = score + 1
            elif (answer_int != rand_sum):
                print("Wrong, the sum was", rand_sum)
        score_percent = (score / problems_int) * 100
        score_percent = (score / float(problems_int)) * 100
        print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int ==6):
        for i in range (0,problems_int):
            rand1 = random.randint(0,999999)
            rand2 = random.randint(0,999999)
            rand3 = random.randint(0,999999)
            rand4 = random.randint(0,999999)
            rand5 = random.randint(0,999999)
            rand6 = random.randint(0,999999)
            rand_sum = 0
            print(rand1, end = " + ")
            print(rand2, end = " + ")
            print(rand3, end = " + ")
            print(rand4, end = " + ")
            print(rand5, end = " + ")
            print(rand6)
            rand_sum = rand1 + rand2
            answer_int = int(input('Your Answer: '))
            if (answer_int == rand_sum):
                print("Correct!")
                score = score + 1
            elif (answer_int != rand_sum):
                print("Wrong, the sum was", rand_sum)
        score_percent = (score / problems_int) * 100
        score_percent = (score / float(problems_int)) * 100
        print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int ==7):
        for i in range (0,problems_int):
            rand1 = random.randint(0,9999999)
            rand2 = random.randint(0,9999999)
            rand3 = random.randint(0,9999999)
            rand4 = random.randint(0,9999999)
            rand5 = random.randint(0,9999999)
            rand6 = random.randint(0,9999999)
            rand7 = random.randint(0,9999999)
            rand_sum = 0
            print(rand1, end = " + ")
            print(rand2, end = " + ")
            print(rand3, end = " + ")
            print(rand4, end = " + ")
            print(rand5, end = " + ")
            print(rand6, end = " + ")
            print(rand7)
            rand_sum = rand1 + rand2
            answer_int = int(input('Your Answer: '))
            if (answer_int == rand_sum):
                print("Correct!")
                score = score + 1
            elif (answer_int != rand_sum):
                print("Wrong, the sum was", rand_sum)
        score_percent = (score / problems_int) * 100
        score_percent = (score / float(problems_int)) * 100
        print("You solved", score, "problems out of", problems_int, "problems which is", score_percent,"percent")
elif (difficulty_int > 7):
    print ("The maximum difficulty is 7!")