# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:02:42 2022

@author: mjvat
"""

class ATM():
    
    def __init__(self, pin=None, receipt=None, card=False, counter=0, balance=1000, amount=0, authenticate=False):
        
        self.pin = pin
        self.receipt = receipt
        self.card = card
        self.counter = counter
        self.balance = balance
        self.amount = amount
        self.authenticate = authenticate
                
    def verify(self, card):
        
        if card == True:
            self.userPin()        
            
    def userPin(self):
        
        pin = int(input('Please enter your pin, press enter when complete: \n\n'))
        
        if pin == 7399:
            self.authenticate = True
            self.warn()
        else: 
            self.failCount()

    def failCount(self):            
    
        if self.counter < 1:
            self.counter+=1
            print('\nSorry, that was incorrect. Please try again')
            self.userPin()
        else:
            print('\nAuthorization Denied. Thank you for using the ATM.')
            
    def warn(self):
        
        print('\nUser authorized...')
        print('\nWarning: Fees may apply to some user actions.')
        print('Warning: Fees will apply if your account is external to our institution.\n')
        self.userActions()
    
    def userActions(self):
        
        print('Current balance is: ', self.balance, '\n')
        print('Please select from the following actions (1-3): ')
        userAction = int(input('1) Withdrawal \n2) Deposit \n3) Transfer Funds \n\n'))
        if userAction == 2:
            print('\nSorry, that option is not currently available. Please try again.\n')
            self.userActions()
        elif userAction == 3:
            print('\nSorry, that option is not currently available. Please try again.\n')
            self.userActions()
        else:
            self.userBalance()
            self.withdraw()
            
    def userBalance(self):
    
        if self.balance > 0:
            pass
        else:
            print('Sorry, there are no funds for withdrawal. Goodbye.')

    def withdraw(self):
        
        amount = int(input('Please enter the amount to withdraw in denominations of 20: \n\n'))
        
        if amount % 20 != 0:
            print('\nInvalid amount, please try again: \n')
            self.withdraw()
        else:
            self.amount = amount
            self.correctAmount()
    
    def correctAmount(self):
        
        print('\nIs this amount correct to withdraw? (yes/no) $', self.amount)
        action = input()
        
        if action == 'yes' or action == 'Yes':
            if self.amount > self.balance:
                print('Sorry. Insufficient funds to process withdrawl. Please try again\n')
                self.withdraw()
            else:
                self.balance = self.balance - self.amount
                self.dispense(self.amount)
        else:
            self.withdraw()
    
    def dispense(self, amount):
        
        print('\n***Plays visual and audio cues to ensure user takes money...***\n')
        print('Current balance is now: ', self.balance, '\n')
        print('Please take your money: ', amount, '\n')
        print('***Turns off visual and audio cues***')
        self.sessionReceipt()
    
    def sessionReceipt(self):
        
        receipt = input('Would you like a receipt for this transaction? (yes/no) \n\n')
        
        if receipt == 'no' or receipt == 'No':
            self.newTransaction()
        else:
            print('\nPrinting reciept...')
            self.newTransaction()
    
    def newTransaction(self):
        
        newTrans = input('Would you like another transaction? (yes/no) \n\n')
        
        if newTrans == 'no':
            print('\nThank you for conducting business with us, we look forward to serving you again.\n')
            print('Goodbye!')
        else:
            self.userActions()

if __name__ == '__main__':
    
    session = ATM()
    session.verify(card=True)
    