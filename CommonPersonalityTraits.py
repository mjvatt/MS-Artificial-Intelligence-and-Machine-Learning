# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:34:43 2021

@author: mjvat
"""

# Create the Personality class
class Personality():
    
    # Initizialize the personality traits
    def __init__(self, personality_traits=[]):
        self.personality_traits = []
    
    # Define the excellent software developers trait function
    def excellentSoftwareDevelopers(self, trait):
        
        for traits in trait:
            self.personality_traits.append(traits)
        
        return self
    
    # Define the function to check to see if the person is an excellent software developer
    def isExcellentSD(self, traits):
        
        # Check the traits to see if they are one of the common personality traits 
        # of an excellent software developer
        answers = []
        for trait in traits:
            if (trait == 'Logical' or trait == 'Perserverance' or trait == 'Inquisitive'):
                answers.append('yes')
            else:
                answers.append('no')
              
        # Check if any of the traits 
        if 'no' in answers:
            print('Person is not an excellent software developer\n')
        else:
            print('Person is an excellent sofware developer!\n')
        
        if all(x in traits for x in ['Logical', 'Perserverance', 'Inquisitive']):
            print('Excellent software developer found!')
            
if __name__ == '__main__':
    
    # Give a software developer some traits
    excellent_traits = ['Logical', 'Perserverance', 'Inquisitive']
    
    # Initailze  the software developer object and append their traits
    excellent_software_developers = Personality()
    excellent_software_developers.excellentSoftwareDevelopers(excellent_traits)
    
    # Let's see what traits they were given
    print()
    print(excellent_software_developers.personality_traits, '\n')
    
    # Let's see if the person is an excellent software developer
    excellent_software_developers.isExcellentSD(excellent_software_developers.personality_traits)