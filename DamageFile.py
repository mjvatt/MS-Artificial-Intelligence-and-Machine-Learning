# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:46:51 2021

@author: mjvat
"""

import ReportPothole
import system_catalog_users

class DamageFile():
    
    def __init__(self, report, citizenInfo):
        
        self.report = report
        self.citizenInfo = citizenInfo
        
    def damage(self):
        
        new_damage_report.report = ReportPothole
        return new_damage_report.report
    
    def citizenInfo(self):
        
        new_damage_report.citizenInfo = system_catalog_users.UserLogin
        return new_damage_report.citizenInfo
        
if __name__ == '__main__':
    
    new_damage_report = DamageFile()
    new_damage_report.report = new_damage_report.damage()
    new_damage_report.citizenInfo = new_damage_report.citizentInfo()
    
    
    
    