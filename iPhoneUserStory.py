# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:10:17 2021

@author: mjvat
"""

# iPhone User Story Pseudocode 

class Favorite(object): 
    
    def __init__(self, feature, favoritesList=[]):
        self.favoritesList = []
        self.feature = feature
        
    # Create a new favorite
    def newFavorite(self, x):
        return self.favoritesList.append(x)
 
    # Save feature to favorites list
    def saveFeature(self, x):
        return self.favoritesList.append(x)
        
    # Edit favorites
    def editFavorite(self, index, edited_item):
        self.favoritesList[index] = self.favoritesList[edited_item]
        
    # Delete favorites
    def deleteFavorite(self, x):
        return self.favoritesList.pop(x)
        
    # Encounter Error
    def isError(self, x):
        self.handleErrorException()
      
myFavorites = Favorite()
myFavorites.newFavorite('Like Button')
myFavorites.newFavorite('Play Song')
myFavorites.newFavorite('Save Date')

print(myFavorites)

