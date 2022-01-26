# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:45:45 2021

@author: mjvat
"""

class ReportPothole():
    
    def __init__(self, address, location, severity):
        
        self.address = address
        self.location = location
        self.severity = severity

    def address(self):
        
        new_pothole.address = input('Please enter the street address for the pothole: ')
        
        return new_pothole.address
    
    def location(self):
        
        new_pothole.location = input('Please describe the location of the pothole in the street: ')
        return new_pothole.locaiton
    
    def severity(self):
        
        new_pothole.severity = input('On a scale of 1-10, how large is the pothole? ')
        return new_pothole.severity
    
if __name__ == '__main__':
    
    new_pothole = ReportPothole()
    new_pothole.address = new_pothole.address()
    new_pothole.location = new_pothole.location()
    new_pothole.severity = new_pothole.severity()

    