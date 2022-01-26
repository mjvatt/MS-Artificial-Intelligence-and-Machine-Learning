# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:46:29 2021

@author: mjvat
"""

import ReportPothole
import city_districts
from uuid import uuid4

class Potholes():
    
    def __init__(self, report, ID, address, size, location, district, priority):
        
        self.report = report
        self.ID = ID
        self.address = address
        self.size = size
        self.location = location
        self.district = district
        self.priority = priority
    
    def report(self, report):
        
        new_pothole.report = report
        new_pothole.ID = new_pothole.uniqueID()

    def uniqueID(self):
        
        uniqueID = str(uuid4())
        return uniqueID

    def district(self, location):
        
        for district in city_districts:
            if location in district:
                new_pothole.district = district
            else:
                new_pothole.district = None
                
        return new_pothole.district
    
    def priority(self, size):
        
        if size < 4:
            new_pothole.priority = 'Low'
        elif size < 8:
            new_pothole.priority = 'Medium'
        else: 
            new_pothole.priority = 'High'
            
        return new_pothole.priority
        
if __name__ == '__main__':
    
    new_pothole = Potholes()
    new_pothole.report = new_pothole.report(ReportPothole)
    new_pothole.address = ReportPothole.address()
    new_pothole.size = ReportPothole.severity()
    new_pothole.location = ReportPothole.location()
    new_pothole.district = new_pothole.district(new_pothole.location)
    new_pothole.priority = new_pothole.priority(new_pothole.size)
    
    
    