# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:40:47 2021

@author: mjvat
"""

# A customer in a store is purchasing five retail items. 
# Write a program that asks for the price of each item and then displays the 
  # subtotal of the sale, the amount of sales tax, and the total. 
  # Assume the sales tax is 7 percent.

# Compile and submit your source code and screenshots of the application 
# executing the code and the results in a single document.

# Calculations
def calculations(price1, price2, price3, price4, price5):
    sub_total = price1 + price2 + price3 + price4 + price5
    sales_tax = 0.07
    total_cost = sub_total + (sub_total * sales_tax)
    print()
    print('The subtotal of your shopping is: ${:.2f}'.format(sub_total))
    print('The sales tax is: {:.2f}%'.format(sales_tax))
    print('The total is: ${:.2f}'.format(total_cost))

# Main function
def main():
    price1, price2, price3, price4, price5 = (
        input('Please enter the prices of the five purchased items separated by a comma (no dollar signs needed):\n').split(',')
    )
    price1 = float(price1)
    price2 = float(price2)
    price3 = float(price3)
    price4 = float(price4)
    price5 = float(price5)

    calculations(price1, price2, price3, price4, price5)
if __name__ == '__main__':
    main()