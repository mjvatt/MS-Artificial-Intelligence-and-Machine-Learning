# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:46:01 2021

@author: mjvat
"""

# Import Module to Quit Program
import sys

# Read User Inputs for Jerseys and Player Ratings
def readInputs():
    
    roster = {}
    j_list = []
    r_list = []
    
    # User Inputs for Jerseys
    print('Please enter 5 jersey numbers (0-99)')
    for i in range(5):
        x = int(input())
        if (x >= 0) and (x <= 99):
            j_list.append(x)
        else:
            j_list.append(int(input('Invalid: please try again (0-99)\n')))
    
    print()
    
    # User Inputs for Player Ratings
    print('Please enter 5 player ratings (1-9)')
    for i in range(5):
        y = int(input())
        if (y >= 1) and (y <= 9):
            r_list.append(y)
        else:
            r_list.append(int(input('Invalid: please try again (1-9)\n')))

    # Build the Roster Dictionary of Jersey Numbers and Player Ratings
    roster = {j_list[i] : r_list[i] for i in range(len(j_list))}
    
    return roster

# Sort the Jersey Numbers in Ascending Order
def sortRoster(team_roster):
    
    sorted_tr = sorted(team_roster.keys())
    return sorted_tr

# Prints the Sorted Roster and its Respective Player Ratings
def printRoster(sorted_tr, team_roster):
    
    print('\nROSTER')
    for jersey in sorted_tr:      
        print('Jersey number: {}, Rating: {}'.format(jersey, team_roster[jersey]))
    
# Prints Menu for User Options After Building Roster
def printMenu():
    
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    
# Function to Respond to User Input to Menu Options
def __userChoice(userChoice, sorted_tr, team_roster):
    
    j_list = []
    r_list = []
    
    # User Input to Add a Player to the Roster
    if userChoice == 'a':
        x = int(input('Please enter a new jersey number (0-99):\n'))   
        if (x >= 0) and (x <= 99):
            j_list.append(x)
        else:
            j_list.append(int(input('Invalid: please try again (0-99)\n')))
            
        y = int(input('Please enter a new player rating (1-9)\n'))
        if (y >= 1) and (y <= 9):
            r_list.append(y)
        else: 
            r_list.append(int(input('Invalid: please try again (1-9)\n')))
        
        new_dict = {j_list[0] : r_list[0]}
        team_roster.update(new_dict)

        updated_sorted_tr = sortRoster(team_roster)
        
        printRoster(updated_sorted_tr, team_roster)
    
    # User Input to Remove a Player from the Roster
    elif userChoice == 'd':
        p = int(input('Which player would you like to remove? Options are: {}\n'.format(sorted_tr)))
        if p not in sorted_tr:
            p = int(input('Invalid: please try again. Options are: {}\n'.format(sorted_tr)))
        team_roster.pop(p)
        
        updated_sorted_tr = sortRoster(team_roster)
        
        printRoster(updated_sorted_tr, team_roster)        
        
    # User Input to Update a Player on the Roster
    elif userChoice == 'u':
        u = int(input('Which player would you like to update? Options are: {}\n'.format(sorted_tr)))
        if u not in sorted_tr:
            u = int(input('Invalid: please try again. Options are: {}\n'.format(sorted_tr)))
        team_roster.pop(u)
        
        new_jersey_number = int(input('Please enter a jersey number for update\n'))
        new_player_rating = int(input('Please enter a new player rating for update\n'))
        
        update_player = {new_jersey_number : new_player_rating}
        team_roster.update(update_player)
        
        updated_sorted_tr = sortRoster(team_roster)
        
        printRoster(updated_sorted_tr, team_roster)
    
    # User Input to Filter the Roster by a Minimum Player Rating
    elif userChoice == 'r':
        filtered_roster = {}
        r = int(input('What is the minimum player rating to filter at?\n'))
        if (r >= 1) and (r <= 9):    
            for jersey in sorted_tr:
                if team_roster[jersey] >= r:
                    filtered_roster[jersey] = team_roster[jersey]
        else:
            r = int(input('Invalid: please try again (1-9)\n'))
            for jersey in sorted_tr:
                if team_roster[jersey] >= r:
                    filtered_roster[jersey] = team_roster[jersey]
                    
        updated_sorted_tr = sortRoster(filtered_roster)
        
        printRoster(updated_sorted_tr, filtered_roster)
          
    # User Input to Simply Print the Entire Roster as it Currently Sits
    elif userChoice == 'o':
        printRoster(sorted_tr, team_roster)
        
    # User Input to Quit the Program
    elif userChoice == 'q':
        print('\nGoodbye!')
        sys.exit()
                
# Main Function to Handle Inputs, Choices, and Ancillary Functions
def main():
    
    team_roster = readInputs()
    sorted_tr = sortRoster(team_roster)

    printRoster(sorted_tr, team_roster)
    printMenu()

    userChoice = input('Choose an option:\n')    
    __userChoice(userChoice, sorted_tr, team_roster)
    
# Calls Main Function
if __name__ == "__main__":
    main()