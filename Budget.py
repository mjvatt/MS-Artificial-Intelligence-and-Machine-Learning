# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 02:01:07 2021

@author: mjvat
"""

def main():
    # Ask for user budget
    user_budget = int(input('What is your budget?\n'))
    
    # Ask for user expenses
    x = 1
    user_expenses = 0
    while x > 0:
        x = int(input('Please enter an expense, enter 0 when done:\n'))
        user_expenses += x

    # Calculate if user went over budget    
    over_under = user_budget 
    over_under -= user_expenses

    if over_under > 0:
        print('Congratulations, you are under budget by ${}!'.format(over_under))
    else:
        print('Unfortunately, you are over budget by ${}.'.format(over_under*-1))

if __name__ == '__main__':
    main()
    
    
    
    
    
    