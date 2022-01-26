# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:37:59 2022

@author: mjvat
"""

from random import randint
import time

class MinimumNumber():
    
    def __init__(self, my_array=[], my_min=999999, time1=None, time2=None, difference=None):
        
        self.my_array = my_array
        self.my_min = my_min
        self.time1 = time1
        self.time2 = time2
        self.difference = difference
        
    def buildArray(self):
        
        for i in range(25000):
            
            self.my_array.append(randint(0,1000))
    
    def printArray(self):
            
            print()
            print(self.my_array)
     
    # Find Minimum in O(n)
    def findMin_v1(self):
        
        start_timer = time.time()

        for i in range(len(self.my_array)):
            
            if self.my_array[i] < self.my_min:
                
                self.my_min = self.my_array[i]
        
        self.time1 = time.time() - start_timer

        print('\nFind Minimum Version 1 Value: ', self.my_min)
        print('Find Minimum Version 1, Time elapsed: ', self.time1)
        
    # Find Minimum in O(n^2)
    def findMin_v2(self):
        
        start_timer = time.time()

        for i in range(len(self.my_array)):
            
            smallest = True
            
            for ii in range(len(self.my_array)):    
                
                if self.my_array[ii] < self.my_array[i]:
                    
                    smallest = False
                    
            if smallest:
                
                self.my_min = self.my_array[i]

        self.time2 = time.time() - start_timer

        print('\nFind Minimum Version 2 Value: ', self.my_min)
        print('Find Minimum Version 2, Time elapsed: ', self.time2)
        
    def timeDifference(self):
        
        difference = abs(self.time1-self.time2)
        print('\n', difference)

if __name__ == '__main__':
    
    my_num = MinimumNumber()
    my_num.buildArray()
    my_num.printArray()
    
    my_num.findMin_v1()
    my_num.findMin_v2()
    my_num.timeDifference()