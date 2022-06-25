# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 19:16:07 2022

@author: mjvat
"""

from random import choice
from experta import *


class HealthcareInfo(Fact):
    
    '''
    This is the Expert System for a local hospital emergency room to help
    staff determine what immediate response should be given to an
    incoming patient of varying degree of injury.
    '''
    pass

class HealthcareRobot(KnowledgeEngine):
    
    # Healthcare Rule 1
    @Rule(HealthcareInfo(injury='bad'))
    def emergency(self):
        print('Give CPR and call for a surgeon.\n')
    # Healthcare Rule 2    
    @Rule(HealthcareInfo(injury='ok'))
    def emergency_room(self):
        print('Give the patient morphine and wait for the doctor.\n')
    # Healthcare Rule 3
    @Rule(HealthcareInfo(injury='good'))
    def open_wound(self):
        print('Clean the wound and place a bandage over it to protect from \
              infection and to keep it clean.\n')
    # Healthcare Rule 4
    @Rule(HealthcareInfo(injury='broken arm'))
    def broken_bone(self):
        print('Call for x-rays and place a cast upon the broken arm.\n')
    # Healthcare Rule 5
    @Rule(HealthcareInfo(injury='cancer'))
    def cancer(self):
        print('Call the oncologist and schedule chemo-therapy.\n')
    # Healthcare Rule 6
    @Rule(HealthcareInfo(injury='surgery'))
    def surgery(self):
        print('Prep the patient for surgery and go over the surgical details \
              to verify accuracy, correctness, and order of operations.\n')
              
    def read_in_facts(self):
        
        facts_list = open('Facts.txt', 'r')
        injuries = []
        for line in facts_list:
            injuries.append(line.strip())
        
        return injuries

def main():
    
    # injuries = ['bad','ok','good','broken arm','cancer', 'surgery']
    engine = HealthcareRobot()
    injuries = engine.read_in_facts()
    print('\nThe type of injuries to examine: \n{}'.format(injuries))
    print()
    
    for i in range(1,7):
        engine.reset()
        engine.declare(HealthcareInfo(injury=choice(injuries)))
        print('Hospital Response for Patient #{}:'.format(i))
        engine.run()


if __name__ == '__main__':
    
    main()
    
