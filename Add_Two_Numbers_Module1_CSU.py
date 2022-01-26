# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:31:48 2021

@author: mjvat
"""

# Function to add two numbers together
def addNumbers(a,b):
     sum = a + b
     print('\nThe sum of the two numbers is: ',sum)
     
def subNumbers(a,b):
    difference = a - b
    print('The difference between the two numbers is: ',difference)

# Main function
def main():
    # First method: Ask for two numbers
    first_num = int(input('Please enter a number:\n'))
    second_num = int(input('Please enter a second number:\n'))
    
    # Second method: Ask for two numbers
    num1, num2 = input('Please enter two numbers separated by a comma:\n').split(',')
    num1 = int(num1)
    num2 = int(num2)
    
    # Calculations on first method
    addNumbers(first_num, second_num)
    subNumbers(first_num, second_num)
    
    # Calculations on second method
    addNumbers(num1, num2)
    subNumbers(num1, num2)
    
if __name__ == '__main__':
    main()