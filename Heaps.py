# -*- coding: utf-8 -*-

"""
Created on Fri Jan 14 18:16:06 2022

@author: mjvat
"""

'''
What are the properties of a heap? What is the running time of heap sort on an 
array A of length n that is already sorted in increasing order? What about the 
same in decreasing order? Lastly, trace out the heap sort algorithm for the 
following list: {25, 44, 55, 99, 30, 37, 15, 10, 2, 4}.

Your activity should include the following: 1. A description of the 
algorithm(s) and, if helpful, pseudocode. 2. At least one worked example or 
diagram to show more precisely how the algorithm(s) works.
'''

from random import randint
import time
import heapq

class Heaps():
    
    def __init__(self, data=[], inc=[], dec=[], time=None):
        
        self.data = data
        self.inc = inc
        self.dec = dec
        self.time = time        
    
    # Initalize Data for Performance Calculations
    def initData(self):
        
        for i in range(500000):
            
            self.data.append(randint(0,1000))
        
    # Sort the Data to be Tested into Increasing Order
    def sortInc(self):
        
        self.inc = sorted(self.data)
    
    # Sort the Data to be Tested into Decreasing Order
    def sortDec(self):
        
        self.dec = sorted(self.data, reverse=True)
    
    # Perform heapsort() Functions to Test Running Times
    def heapSort(self, data):
        
        start_timer = time.time()
        
        h=[]
        for i in data:
            heapq.heappush(h, i)
        
        self.time = time.time() - start_timer
        
        return [heapq.heappop(h) for i in range(len(h))], self.time
    
if __name__ == '__main__':
    
    # Initialize Heaps Object
    my_heap = Heaps()
    
    # Initalize Data to Test Upon
    my_heap.initData()
    
    # Evaluate Heap Sort Time on Sorted (Increaseing Value) Array
    my_heap.sortInc()
    
    # Evaluate Heap Sort Time on Sorted (Decreaseing Value) Array
    my_heap.sortDec()
    
    my_heap.inc, my_heap.time = my_heap.heapSort(my_heap.inc)
    print()
    print('Heapsort for an Array of Increasing Order: ', my_heap.time, 'seconds.\n')
        
    my_heap.dec, my_heap.time = my_heap.heapSort(my_heap.dec)
    print('Heapsort for an Array of Decreasing Order: ', my_heap.time, 'seconds.\n')
    
    



