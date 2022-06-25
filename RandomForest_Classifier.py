# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 14:38:48 2022

@author: mjvat
"""


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

class Classifier:
    
    __slots__ = ('X', 'y', 'data', 'train_X', 'train_y', 'test_X', 'test_y', \
                 'prior', 'posterior', 'likelihood')
    

    def __init__(self, csv_filepath=None, target_column=None):
        
        self.X = None
        self.y = None
        self.data = None
        self.train_X, self.test_X = None, None
        self.train_y, self.test_y = None, None
        self.prior, self.posterior = None, None
        self._load_data(csv_file=csv_filepath, target_column=target_column, \
                        col_headers=['Id', 'SepalLengthCm', 'SepalWidthCm', \
                                     'PetalLengthCm', 'PetalWidthCm', 'Species'])
        

    def _load_data(self, csv_file=None, target_column=None, col_headers=None):
            
        self.data = pd.read_csv(csv_file, header=col_headers if not col_headers else 0)
        
        # Set the target_column as the last column in the csv_file
        if target_column is None:
            target_column = self.data.columns[len(self.data.columns)-1]
            
        self.y = self.data[target_column]
        self.data.drop(columns=[target_column], inplace=True)
        self.X = self.data
        
        self.train_X, self.test_X, self.train_y, self.test_y = \
            train_test_split(self.X, self.y, test_size=0.3, \
                              random_state=42, stratify=self.y)

                
    def _random_forest(self,  **kwargs):
        
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(self.train_X, self.train_y)
        y_pred = rf.predict(self.test_X)
        print('Accuracy: ', metrics.accuracy_score(self.test_y, y_pred))


    def _posterior_prob_freq_table(self):
        
        freq_table = pd.crosstab(self.y, 'Number of Species')
        print()
        print('The frequency table is: ')
        print(freq_table)
        
        
    def _likelihood_table(self):
        
        likelihood_table = pd.crosstab(self.y, 'Number of Species')
        likelihood_table = likelihood_table/len(self.y)
        print()
        print('The likelihood table is:') 
        print(likelihood_table)
        self.likelihood = likelihood_table

        
    def _prior(self):
        
        probabilities = 1/3, 1/3, 1/3
        hypotheses = 'setosa', 'versicolor', 'virginica'
        self.prior = pd.Series(probabilities, hypotheses)
        print()
        print('The priors are: ')
        print(self.prior)
    
    def _posterior_prob_class(self):
        
        print(self.prior[1])
        post_prob = self.prior[1] * self.likelihood['Number of Species']
        print()
        print('Posterior Probability by Class: ')
        print(post_prob)


    def train_classifier(self):
        
        classifier_scores = []
        
        classifier_scores.append((self._random_forest(scoring='accuracy',
                                                                 max_depth=[val for val in range(1, 51)],
                                                                 min_samples_split=[val for val in range(2, 11)])))
        

def main():
    
    input_csv = 'https://raw.githubusercontent.com/mjvatt/MS-Artificial-Intelligence-and-Machine-Learning/main/Iris.csv'
    classifier = Classifier(csv_filepath=input_csv)
    classifier._posterior_prob_freq_table()
    classifier._likelihood_table()
    classifier._prior()
    classifier._posterior_prob_class()
    print()
    print('Training the Random Forest Classifier: ')
    classifier.train_classifier()


if __name__ == '__main__':
    
    main()