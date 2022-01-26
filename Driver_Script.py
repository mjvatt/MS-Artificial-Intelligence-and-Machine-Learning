# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:11:44 2022

@author: mjvat
"""

'''
Write a driver script that does the following:

    Create a binary search tree from an array of random numbers 
        (`Array.new(15) { rand(1..100) }`)
    Confirm that the tree is balanced by calling `#balanced?`
    Print out all elements in level, pre, post, and in order
    try to unbalance the tree by adding several numbers 100
    Confirm that the tree is unbalanced by calling `#balanced?`
    Balance the tree by calling `#rebalance!`
    Confirm that the tree is balanced by calling `#balanced?`
    Print out all elements in level, pre, post, and in order

Compile and submit your source code and screenshots of the application 
executing the application and the results in a single document.
'''

from random import randint

class BST:
    
    # Initialze BST object
    def __init__(self, val=None):
        
        self.left = None
        self.right = None
        self.val = val
        
    # Initalize Data for the Tree
    def initData(self):
        
        data = []
        for i in range(15):
            data.append(randint(0,100))
            
        return data
        
    # Add More Data Points to Try and Unbalance the Tree
    def addData(self, data=[]): 
        
        for i in range(12):
            
            data.append(randint(101,200))
            
        return data
    
    # Sort the data array
    def sort(self, data):
        
        data = sorted(data)
        
        return data

    # Find the Root
    def root(self, data):
        
        middle = round(len(data)/2)
        root = data[middle]
        return root, middle
    
    # Insert values into the BST
    def insert(self, val):
        
        if not self.val:
            self.val = val
            return
    
        if self.val == val:
            return
    
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST(val)
            return
    
        if self.right:
            self.right.insert(val)
            return
        self.right = BST(val)
        
    # Get Heights 
    def getHeights(self, data, left_height, right_height):
        
        count = 0

        if count == 0:
            print("Left Height:",left_height)
            print("Right Height:",right_height,'\n')
        else:
            print("New Left Height:",left_height)
            print("New Right Height:",right_height,'\n')
            
        difference = 0        
        
        difference = abs(left_height-right_height)
        
        return difference 
    
    # Check to see if the Tree is balanced
    def isBalanced(self, data, middle):
        
        #middle = round(len(data)/2)
        
        balanced = False
        
        difference = 0
    
        left_height = len(data[:middle-1])
        right_height = len(data[middle:])
        
        if left_height == right_height:
            balanced = True
            print("Left Height:",left_height)
            print("Right Height:",right_height,'\n')
        else:
            difference = self.getHeights(data, left_height, right_height)
        
        return balanced, difference
    
    # Balance an unbalanced tree
    def rebalance(self, data, root):
        
        middle = round(len(data)/2)
        left_height = len(data[:middle-1])
        right_height = len(data[middle:])
        print("New Left Height:", left_height)
        print("New Right Height:", right_height,'\n')
        
        balanced = False
        
        if left_height == right_height:
            balanced = True
            return
        else:
            difference = self.getHeights(data, left_height, right_height)
    
        return balanced, difference
    
    # Print out tree with Preorder Traversal
    def preorder(self, vals):
        
        root, middle = myTree.root(data)
        
        array = []
        array.append(root)
        for i in range(len(data)):
           
            if data[i] != root:
                array.append(data[i])

        return array

    # Print out tree with Postorder traversal
    def postorder(self, vals):

        root, middle = myTree.root(data)
        
        array = []
        
        for i in range(len(data)):
            
            if data[i] != root:
                array.append(data[i])
        
        array.append(root)
        
        return array
    
    # Print out tree with Inorder Traversal
    def inorder(self, vals):
        
        root, middle = myTree.root(data)
        
        array = []
        
        for i in range(len(data)):
            
            array.append(data[i])

        return array
    
# Call main() program
if __name__ == '__main__':

        # Initialize BST Object
        myTree = BST()
        
        # Add the initial array of random numbers
        data = myTree.initData()
        for datum in data:
            myTree.insert(datum)
        
        print()
        print('Original Array:',data,'\n')   
        
        # Sort the initial array 
        data = myTree.sort(data)
        print("Original Array Sorted:",data,'\n')
        
        # Find the root
        root, middle = myTree.root(data)
        print("Original Root:",root,'\n')
        
        # Is the array balanced?
        is_balanced = False
        difference = 0
        is_balanced, difference = myTree.isBalanced(data, middle)
        print('Is the tree balanced?:',is_balanced)
        print('What is the difference in heights?:',difference,'\n')
        
        ## Print out all elements in level, pre, post, and inorder for initial array
        print('################################################\n')
        
        # Preorder Traversal
        print("Original Array Preorder Traversal:")
        print(myTree.preorder([]),'\n')
        
        # Postorder Traversal
        print("Original Array Postorder Traversal:")
        print(myTree.postorder([]),'\n')
        
        # Inorder Traversal
        print("Original Array Inorder Traversal:")
        print(myTree.inorder([]),'\n')
        print('################################################\n')

        # Add values to the array to unbalance the teree
        data = myTree.addData(data)
        for datum in data:
            myTree.insert(datum)
            
        print("New Array with added Data:",data,'\n')
        
        # Is the array still balanced?
        is_balanced = False
        difference = 0
        is_balanced, difference = myTree.isBalanced(data, middle)
        print('Is the tree still balanced?:', is_balanced)
        print('What is the difference in heights?:',difference,'\n')
        
        # Balance the new tree
        data = myTree.sort(data)
        root, middle = myTree.root(data)
        print("New Array Root:",root,'\n')
        myTree.rebalance(data, root)
        
        # Confirm tree has been rebalanced
        is_balanced = False
        difference = 0
        is_balanced, difference = myTree.isBalanced(data, middle)
        print('Did it get rebalanced?:',is_balanced)
        print('What is the difference in heights?:',difference,'\n')
            
        ## Print out all elements in level, pre, post, and inorder for rebalanced array
        print('################################################\n')

        # Preorder Traversal
        print("Original Array Preorder Traversal:")
        print(myTree.preorder([]),'\n')
        
        # Postorder Traversal
        print("Original Array Postorder Traversal:")
        print(myTree.postorder([]),'\n')
        
        # Inorder Traversal
        print("New Array Inorder Traversal:")
        print(myTree.inorder([]),'\n')
        print('################################################\n')
