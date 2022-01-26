# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:37:22 2021

@author: mjvat
"""

'''
This program reverses a Linked List in Python.
'''

# Time complexity - perform in O(2n), otherwise known as Linear time. 
# Space complexity - perform in O(n).

class Node(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        result = str(self.val)
        if self.next:
            result += str(self.next)
        return result
    
class Solution(object):
    
    def reverse(self, node):
        curr = node
        prev = None
        
        while curr != None:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(7))))))

print(Solution().reverse(node))
