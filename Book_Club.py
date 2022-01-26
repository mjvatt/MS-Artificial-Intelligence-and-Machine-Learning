# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:34:04 2021

@author: mjvat
"""

def points_earned(books_purchased):
    points = 0
    if books_purchased < 2:
        return points
    elif books_purchased < 4:
        points = 5
        return points
    elif books_purchased <6:
        points = 15
        return points
    elif books_purchased < 8:
        points = 30
        return points
    elif books_purchased >= 8:
        points = 60
        return points

def main():
    books_purchased = int(input('Enter the number of books you have purchased this month:\n'))
    
    user_points = points_earned(books_purchased)
    print('\nCongratulations, you have earned {} points'.format(user_points))
    
if __name__ == '__main__':
    main()
    
    
    
    