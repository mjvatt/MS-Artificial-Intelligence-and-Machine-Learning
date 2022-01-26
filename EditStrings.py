# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:41:51 2021

@author: mjvat
"""

import numpy as np

class EditStrings():

    def __init__(self, x=None, y=None, n=None, m=None, matrix=None, distance=None):

        self.x = ''
        self.y = ''
        self.n = 0
        self.m = 0
        self.matrix = []
        self.distance = 0

    def wordsToCompare(self):
	
        x, y = input('Please enter two strings separated by a space: ').split()
        print('\nThank you, calculating...\n')
        return x, y

    def getLength(self, x, y):

        n, m = len(x), len(y)
        return n, m

    def createMatrix(self, n, m):

        matrix = [[0 for i in range(n+1)] for ii in range(m+1)]

        for i in range(n+1):
            matrix[i][0] = i
        for j in range(m+1):
            matrix[0][j] = j

        return matrix

    def cost(self, x, y, n, m, matrix):
        
        if m == 0:
            return n
        if n == 0:
            return m

        for i in range(1, n+1):
            for j in range(1, m+1):
                if x[i-1] == y[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    insertion = matrix[i][j-1] + 20
                    deletion = matrix[i-1][j] + 20
                    replacement = matrix[i-1][j-1] + 5
                    matrix[i][j] = min(insertion, deletion, replacement)

        print('Complete\n')
        print('String Edit Distance: ', matrix[m][n], '\n')

        return matrix[n][m]
    
    def invert_matrix(self, matrix):

        matrix.reverse()
        return matrix
            

if __name__ == '__main__':

    # Initializes EditStrings Object
    my_strings = EditStrings()
    
    # Ask user for two words and retrieve their lengths
    my_strings.x, my_strings.y = my_strings.wordsToCompare()
    my_strings.n, my_strings.m = my_strings.getLength(my_strings.x, my_strings.y)
    
    # Initialize matrix for calculations
    my_strings.matrix = my_strings.createMatrix(my_strings.n, my_strings.m)
    #print(my_strings.matrix, '\n')
    
    # Calculate edit strings cost
    my_strings.distance = my_strings.cost(my_strings.x, my_strings.y, my_strings.n, my_strings.m, my_strings.matrix)

    # Invert the matrix for visual output    
    my_strings.matrix = my_strings.invert_matrix(my_strings.matrix)
    
    print(np.array(my_strings.matrix), '\n')
