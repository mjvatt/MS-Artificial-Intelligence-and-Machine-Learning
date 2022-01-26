# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:40:30 2021

@author: mjvat
"""

# Step 1: Build the ItemToPurchase class with the following specifications:

# Step 2: In the main section of your code, prompt the user for two items 
  # and create two objects of the ItemToPurchase class.
  
# Step 3: Add the costs of the two items together and output the total cost.    

# This is the main class ItemToPurchase - here we initalize values and 
  # parameterize the constructor
class ItemToPurchase:
    def __init__(self, item_name = 'None', item_price = 0, item_quantity = 0, total_cost = 0):
        self.item_name = item_name 
        self.item_price = item_price 
        self.item_quantity = item_quantity 
        self.total_cost = total_cost
        print_item_cost(self.item_name, self.item_price, self.item_quantity)
        
# This calculates the item(s) cost and total cost - returning the 
  # shopping cart total of both items combined
def print_item_cost(item_name, item_price, item_quantity):
    total_cost = item_price * item_quantity
    print('\n{} with a quantity of {} will cost: ${:.2f}'.format(item_name, item_quantity, total_cost)) 

# Main Function to read I/O and run the appropriate algorithm
def main():
    item_name1, item_name2 = (input('Please enter two items to purchase separated by a comma:\n').split(','))
    item_price1, item_price2 = (input('Enter the cost of each item separated by a comma:\n').split(','))
    item_quantity1, item_quantity2 = (input('How many of each item would you like (separated by a comma:\n').split(','))
    
    # Removes white space if necessary for clean formatting
    item_name1 = item_name1.strip()
    item_name2 = item_name2.strip()
    
    # Converts prices to integers from strings
    item_price1 = int(item_price1)
    item_price2 = int(item_price2)
    
    # This is to ensure proper data types and performance of calculations
    item_quantity1 = int(item_quantity1)
    item_quantity2 = int(item_quantity2)
    
    # Calls the class to perform necessary functions
    ItemToPurchase(item_name1, item_price1, item_quantity1)
    ItemToPurchase(item_name2, item_price2, item_quantity2)

    shopping_cart_total = (item_price1 * item_quantity1) + (item_price2 * item_quantity2)    
    print('\nThe entire shopping cart will cost: ${:.2f}'.format(shopping_cart_total))

# Calls main function
if __name__ == '__main__':
    main()
    
    
    