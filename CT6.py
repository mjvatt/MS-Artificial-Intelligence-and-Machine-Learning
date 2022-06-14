# -*- coding: utf-8 -*-
"""
Created on Thu May 9 11:13:37 2022

@author: mjvat
"""

import os
import time
import glob

my_path = os.getcwd()

class FileCreator:
    
    def __init__(self, linuxoutputfile=None, python_all_lines=None, \
                 file_part1=None, file_part2=None, linux_time=None, \
                 python_all=None, times=[], combine_files=None, \
                 python_time_all=None, python_time_split=None, \
                 python_time_1=None, python_time_2=None):

        self.linuxoutputfile = linuxoutputfile
        self.python_all_lines = python_all_lines
        self.combine_files = combine_files
        self.linux_time = linux_time
        self.python_all = python_all        
        self.python_time_all = python_time_all
        self.times = times
        
    def readFile(self):
        
        self.linuxoutputfile = open('file10x.txt','r')
        
    def pythonAllFile(self):
        
        start_timer = time.time()
        
        with  open('file10x.txt', 'r') as file:
            self.python_all_lines = file.readlines()
                
        self.python_all = time.time() - start_timer
        
    def filePartition(self, num_splits):
        
        print('\nThe number of splits called: {}'.format(num_splits))
        
        combine_timer = time.time()
        
        times = []
        
        partition = int(len(self.python_all_lines)/num_splits)
        
        for splits in range(num_splits):
            
            part_timer = time.time()
            
            if splits == 0:
                with open('file'+str(splits)+'.txt', 'w') as file:
                    for line in self.python_all_lines[:partition]:
                        self.file_part = file.write(line)
            elif splits == 1:
                with open('file'+str(splits)+'.txt', 'w') as file:
                    for line in self.python_all_lines[partition:partition*2]:
                        self.file_part = file.write(line)
            else:
                with open('file'+str(splits)+'.txt', 'w') as file:
                    for line in self.python_all_lines[partition*(splits):partition*(splits+1)]:
                        self.file_part = file.write(line)
                 
            self.timer = time.time() - part_timer
            times.append(self.timer)
            self.times = times
            
        # Python Split Times
        for i in range(len(self.times)):
            print('\nPython split time {} executed in {} seconds.'.format(i, self.times[i]))       

        # Python Split Times Combined
        total_split_time = 0
        for i in range(len(my_files.times)):
            total_split_time += my_files.times[i]    
        
        print('\nPython split total time results in {} seconds.'.format(total_split_time))
        
        # Recombined files
        my_files.combineFiles(num_splits)
        
        combined_time = time.time() - combine_timer
        
        print('\nPyton split + recombine time results in {} seconds.'.format(combined_time))
        
    def combineFiles(self, num_splits):
        
        if num_splits < 11:
            file_list = glob.glob('file[0-9].txt')
            print('\nFiles to recombine: ', file_list)
            
            with open('combined_files'+str(num_splits)+'.txt', 'w') as result:
                for file in file_list:
                    for line in open(file, 'r'):
                        result.write(line)
        else: 
            file_list = glob.glob('file*[0-9].txt')
            print(type(file_list))
            print('\nFiles to recombine: ', file_list)
            
            with open('combined_files'+str(num_splits)+'.txt', 'w') as result:
                for file in file_list:
                    for line in open(file, 'r'):
                        result.write(line)
                        
    def linuxTime(self, filename):

        file = open(str(filename))        
        all_lines = file.readlines()
        self.linux_time = all_lines[10000001]
        
if __name__ == '__main__':
    
    # Create python file object
    my_files = FileCreator()
    
    # Read file10x.txt created from Linux
    my_files.readFile()

    # Read file10x.txt contents into Python
    my_files.pythonAllFile()
    
    # Linux Time
    my_files.linuxTime(my_files.linuxoutputfile.name)
    print('\nLinux script executed in {} seconds.'.format(my_files.linux_time))
    
    # Python All Time
    print('\nPython file10x.txt read-in executed in {} seconds.'.format(my_files.python_all))
    
    # Split file10x.txt into two txt files
    list_lengths = []
    list_lengths = [2, 5, 10, 20]
    for num_splits in list_lengths: 
        my_files.filePartition(num_splits)