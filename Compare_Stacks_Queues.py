# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:11:44 2022

@author: mjvat
"""

'''
Option #1: List Based Stack
Design and implement an experiment that will compare the performance of the 
Python list based stack and queue with the linked list implementation. Provide 
a brief discussion of both stacks and queues for this activity.

Your Python Programming submission materials must include your source code and 
screenshots of the Python interface executing the application and the results.

'''

from random import randint
import time

# Helper for buiding a Queue
class Node(object):
    
    def __init__(self, value=None, next=None):
        
        self.value = value
        self.next = next

# Build a Queue Object
class Queue(object):
    
    def __init__(self, head=None, tail=None, count=0):
        
        self.head = head
        self.tail = tail
        self.count = count
    
    def isEmpty(self):
        
        return self.head == None and self.tail == None
    
    def enqueue(self, value):
        
        node = Node(value)
        
        if self.head == None:
            
            self.head = node
            self.tail = self.head
            return
        
        self.tail.next = node
        self.tail = node
        self.count+=1
    
    def dequeue(self):
        
        if self.head == None:
            
            raise Exception('Cannot dequeue, queue is currently empty.')
            
        value = self.head.value
        self.head = self.head.next
        self.count-=1
        
        if self.head == None:
            
            self.tail = None
            
        return value
    
    def buildQueue(self, data):
        
        for i in range(len(data)):
            
            self.enqueue(data[i])
            
        if self.isEmpty():
            
            print('The queue is empty')
            
        return self
    
    # Perform Queue Calculation
    def queuePerformance(self, data):
        
        start_timer = time.time()
        
        test_queue = []
        
        for i in range(self.count):
            
            test_queue.append(self.dequeue())
            
        self.time2 = time.time() - start_timer
        
        print('Queue Test Time: ', self.time2, '\n')
        
        return self.time2
    
# Build a Stack Object
class Stack(object):
    
    def __init__(self, stack=[]):
        
        self.stack = stack
        
    # List Based Stack
    def buildStack(self, data):
        
        for i in range(len(data)):
            
            self.stack.append(data[i])
        
        return self.stack

    # Perform Stack Calculation
    def stackPerformance(self, data):
        
        start_timer = time.time()

        test_stack = []
        
        for i in range(len(data)):
            
            test_stack.append(self.stack.pop())
            
        self.time1 = time.time() - start_timer
        
        print('Stack Test Time: ', self.time1, '\n')
        
        return self.time1
    
# Perform Comparison Calculations
class ComparePerformance():
    
    #def __init__(self, data=[3,4,7,8,11], stack=[], queue, compare):
    def __init__(self, data=[], stack=[], q=None, compare=None, time1=None, \
                 time2=None):
        
        self.data = data
        self.stack = stack
        self.q = q
        self.compare = compare
        
    # Initalize Data for Performance Calculations
    def initData(self):
        
        for i in range(50000000):
            
            self.data.append(randint(0,1000))
        
    def compareCalc(self, stack_time, q_time):
        
        time = 0
        
        if stack_time > q_time:
            
            time = stack_time - q_time
            print('It took ', time, 'seconds longer for the Stack performance than the Queue performance.')
        
        else:
            
            time = q_time - stack_time
            print('It took ', time, 'seconds longer for the Queue performance than the Stack performance.')
        
        
if __name__ == '__main__':
    
    my_compare = ComparePerformance()
    
    my_compare.initData()
    print()
    print('my_compare.data first 10 values: ', my_compare.data[0:10], ' of', len(my_compare.data), 'values \n')
    stack_run = Stack()
    my_compare.stack = stack_run.buildStack(my_compare.data)
    stack_time = stack_run.stackPerformance(my_compare.stack)

    q_run = Queue()
    my_compare.q = q_run.buildQueue(my_compare.data)
    q_time = q_run.queuePerformance(my_compare.q)
    
    my_compare.compareCalc(stack_time, q_time)
    
    
    
    