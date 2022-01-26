# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:47:23 2021

@author: mjvat
"""

import Potholes
import nearest
import hours_per_type_size

class WorkOrder():
    
    def __init__(self, location, size, crewID, crewSize, equipment, allocatedHours, potholeStatus, filler, repairCost):
        
        self.location = location
        self.size = size
        self.crewID = crewID
        self.crewSize = crewSize
        self. equipment = equipment
        self.allocatedHours = allocatedHours
        self.potholeStatus = potholeStatus
        self.filler = filler
        self.repairCost = repairCost
    
    def crewID(self):
        
        return nearest.crewID

    def crewSize(self, crewID):
        
        new_work_order.crewSize = crewID.size
        return new_work_order.crewSize

    def equipment(self, crewID):

        new_work_order.equipment = crewID.equipmentList
        return new_work_order.equipment        
    
    def allocatedHours(self, report):
        
        new_work_order.allocatedHours = hours_per_type_size
        return new_work_order.allocatedHours
    
    def potholeStatus(self):
        
        new_work_order.potholeStatus = new_work_order.crewInput()
        return new_work_order.potholeStatus
    
    def crewInput(self):
        
        print('What status is the pothole: ')
        crewInput = input('1) WIP, 2) Repaired, 3) Temp Repair, 4) Unrepaired')
        return crewInput
    
    def filler(self, size):
        
        new_work_order.filler = size * .25 # truck loads
        
    def repairCost(self, hours, crewSize, material, equipment):
        
        new_work_order.repairCost = (hours + crewSize + material + equipment) * 275 # dollars
        
if __name__ == '__main__':
    
    new_work_order = WorkOrder()
    new_work_order.location = Potholes.location
    new_work_order.size = Potholes.size
    new_work_order.crewID = new_work_order.crewID()
    new_work_order.crewSize = new_work_order.crewSize(new_work_order.crewID)    
    new_work_order.equipment = new_work_order.equipment(new_work_order.crewID)  
    new_work_order.allocatedHours = new_work_order.allocatedHours()
    new_work_order.potholeStatus = new_work_order.potholeStatus()
    new_work_order.filler = new_work_order.filler(new_work_order.size)
    new_work_order.repairCost = new_work_order.repairCost(new_work_order.allocatedHours, new_work_order.crewSize, \
                                                          new_work_order.filler, new_work_order.equipment)

