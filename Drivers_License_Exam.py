# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:46:52 2021

@author: mjvat
"""

# Driver's License Exam

# The local driver's license office has asked you to create an application 
# that grades the written portion of the driver's license exam. The exam has 
# 20 multiple-choice questions. Here are the correct answers:
    
#1. A
#2. C
#3. A
#4. A
#5. D
#6. B
#7. C
#8. A
#9. C
#10. B
#11. A
#12. D
#13. C
#14. A
#15. D
#16. C
#17. B
#18. B
#19. D
#20. A

# Your program should store these correct answers in a list. The program 
# should read the student's answers for each of the 20 questions from a 
# text file and store the answers in another list. (Create your own text 
# file to test the application.) After the student's answers have been read 
# from the file, the program should display a message indicating whether the 
# student passed or failed the exam. (A student must correctly answer 15 of 
# the 20 questions to pass the exam.) It should then display the total number 
# of correctly answered questions, the total number of incorrectly answered 
# questions, and a list showing the question numbers of the incorrectly 
# answered questions.

# Compile and submit your source code and screenshots of the application 
# executing the code and the results in a single document.

def getAnswers():
    
    correctAnswers = {1: 'A',
                      2: 'C',
                      3: 'A',
                      4: 'A',
                      5: 'D',
                      6: 'B',
                      7: 'C',
                      8: 'A',
                      9: 'C',
                      10: 'B',
                      11: 'A',
                      12: 'D',
                      13: 'C', 
                      14: 'A',
                      15: 'D',
                      16: 'C',
                      17: 'B',
                      18: 'B',
                      19: 'D',
                      20: 'A'}
    
    return correctAnswers

def readInput():
    
    with open("E:/Transfer/Desktop/Schools/CSU/CSC500/Week 6/test_answers.txt", 'r') as f:
        userAnswers = f.readlines()
    userAnswers = [x.strip() for x in userAnswers]
    
    return userAnswers

def readInputGoodTest():
    
    with open("E:/Transfer/Desktop/Schools/CSU/CSC500/Week 6/test_answers.txt", 'r') as f:
        userAnswers = f.readlines()
    userAnswers = [x.strip() for x in userAnswers]
    
    return userAnswers

def readInputBadTest():
    
    with open("E:/Transfer/Desktop/Schools/CSU/CSC500/Week 6/test_answers2.txt", 'r') as f:
        userAnswers = f.readlines()
    userAnswers = [x.strip() for x in userAnswers]
    
    return userAnswers

def evaluateAnswers(userAnswers, correctAnswers):
    
    correct = 0
    incorrect = 0
    index = []
    for answer in range(len(userAnswers)):
        if userAnswers[answer] == correctAnswers.get(answer+1):
            correct += 1
        else:
            incorrect += 1
            index.append(answer+1)
        answer += 1
        
    return correct, incorrect, index    
    
def passFail(correct):
    
    if correct >= 15:
        pf = 'Passed'
    else:
        pf = 'Failed'
    
    return pf

def main():
    
    correctAnswers = getAnswers()

    userAnswers = readInputGoodTest()
    correct, incorrect, index = evaluateAnswers(userAnswers, correctAnswers)
    pf = passFail(correct)
    if pf == 'Passed':
        print("\nThe student's score \"{}\" the test. They got {} correct and {} incorrect.".format(pf, correct, incorrect))
    else:
        print("\nThe student's score \"{}\" the test. They got {} correct and {} incorrect.".format(pf, correct, incorrect))
        print("The student missed problems {}".format(index))
    
    userAnswers = readInputBadTest()
    correct, incorrect, index = evaluateAnswers(userAnswers, correctAnswers)
    pf = passFail(correct)
    if pf == 'Passed':
        print("\nThe student's score \"{}\" the test. They got {} correct and {} incorrect.".format(pf, correct, incorrect))
    else:
        print("\nThe student's score \"{}\" the test. They got {} correct and {} incorrect.".format(pf, correct, incorrect))
        print("The student missed problems {}.".format(index))
        
if __name__ == '__main__':
    main()
    
    
    
