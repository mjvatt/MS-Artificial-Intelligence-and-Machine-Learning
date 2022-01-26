# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 04:03:20 2021

@author: mjvat
"""

# Get the Average Weight of the Soccer Team Player Weights
def getAvg(weights):
    total = sum(weights)
    avgweight = total / len(weights)
    return avgweight

# Get the Max Weight of the Soccer Team Player Weights
def getMax(weights):
    maxweight = max(weights)
    return maxweight

# Main Function to Handle Inputs, Choices, and Ancillary Functions
def main():
    weights = [float(input('Please enter the weight of a soccer player:\n')) for i in range(4)]
    avgweight = getAvg(weights)
    maxweight = getMax(weights)
    
    print()
    print('Weights:', weights,'\n')
    print('Average weight:', avgweight, '\n')
    print('Max weight:', maxweight, '\n')

if __name__ == '__main__':
    main()
    
    
    
