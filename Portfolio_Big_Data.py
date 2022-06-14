# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:13:37 2022

@author: mjvat
"""

import os
import time
import threading
import multiprocessing

my_path = os.getcwd()

class PortfolioProject:
    
    def __init__(self, readFile1=None, readFile2=None, outputFile=None, \
                 file_part=None, read_timer=None, brute_timer=None, \
                 conc_timer=None, split_timer=None, mp_timer=None, \
                 sumFiles=[], conc_sumFiles=[], mp_sumFiles=[]):
        
        self.readFile1 = readFile1 
        self.readFile2 = readFile2
        self.outputFile = 'totalfile.txt'
        self.file_part = file_part
        
        self.read_timer = read_timer
        self.brute_timer = brute_timer
        self.conc_timer = conc_timer
        self.mp_timer = mp_timer
        self.split_timer = split_timer
        
        self.sumFiles = sumFiles
        self.conc_sumFiles = conc_sumFiles
        self.mp_sumFiles = mp_sumFiles

    def readFile(self, firstFile, secondFile):
        
        start_timer = time.time()
        print()
        print('readFile()')
        print()
        print(time.strftime("%H:%M:%S"))
        print()
        print('Start reading in data...\n')
        
        with open(str(firstFile), 'r') as file:
            self.readFile1 = file.readlines()
        print('First file complete...\n')
        
        with open(str(secondFile), 'r') as file:
            self.readFile2 = file.readlines()
        print('Second file complete...\n')
        
        self.readFile1 = list(map(int, self.readFile1))
        print('First file mapping complete...\n')
        self.readFile2 = list(map(int, self.readFile2))
        print('Second file mapping complete...\n')
        self.read_timer = time.time() - start_timer
        
    def bruteForce_sumFileLines(self):
        
        print('BruteForce()')
        print()
        print(time.strftime("%H:%M:%S"))
        print()
        
        start_timer = time.time()
        
        for i in range(len(self.readFile1)):
            self.sumFiles.append(self.readFile1[i] + self.readFile2[i])
       
        self.writeNewFile()
        
        self.brute_timer = time.time() - start_timer
        
    def writeNewFile(self):
    
        with open(self.outputFile, 'w') as file:
            for i in range(len(self.sumFiles)):
                file.writelines(str(self.sumFiles[i]) + '\n')

        file.close()
        
    def sumLines(self, x, y):
        
        for i in range(len(x)):
            self.conc_sumFiles.append(x[i] + y[i])
    
    def concurrency(self, n_threads):

        print('Concurrency()')
        print()
        print(time.strftime("%H:%M:%S"))
        print()
        
        start_timer = time.time()
        
        threads = []
        
        for i in range(n_threads):
            t = threading.Thread(target=self.sumLines(self.readFile1, self.readFile2), args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
                                        
        self.conc_timer = time.time() - start_timer
        
        # self.writeNewFile()

    def multiProc(self, files, n_proc): 

        print('Multiprocessing()')
        print()
        print(time.strftime("%H:%M:%S"))
        print()
        
        start_timer = time.time()
        
        processes = []
        
        if len(files) == 2:
            self.readFile1 = files[0]
            self.readFile2 = files[1]
        
            for i in range(n_proc):
                p = multiprocessing.Process(target=self.sumLines(self.readFile1, self.readFile2), args=(i,))
                processes.append(p)
                p.start()

            for p in processes:
                p.join()
                        
        else:         
            for i in range(len(files)):
                
                self.readFile1 = files[i]
                self.readFile2 = files[i]
                
                for i in range(n_proc):
                    p = multiprocessing.Process(target=self.sumLines(self.readFile1, self.readFile2), args=(i,))
                    processes.append(p)
                    p.start()
           
                for p in processes:
                    p.join()

        self.mp_timer = time.time() - start_timer

        # self.writeNewFile()

    def splitFiles(self, firstFile, secondFile, n_splits):

        print('SplitFiles()')
        print()
        print(time.strftime("%H:%M:%S"))
        
        print('\nThe number of splits called: {}'.format(n_splits), '\n')

        start_timer = time.time()
        
        partition = int(len(self.readFile1)/n_splits)
        
        files = []
        
        for splits in range(n_splits):
            
            if splits == 0:
                with open(firstFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile1[:partition]:
                        self.file_part = file.write(str(line)+'\n')
                        if (firstFile+'_'+str(splits)+'.txt') not in files:
                            files.append(firstFile+'_'+str(splits)+'.txt')
                        
            elif splits == 1:
                with open(firstFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile1[partition:partition*2]:
                        self.file_part = file.write(str(line)+'\n')
                        if (firstFile+'_'+str(splits)+'.txt') not in files:
                            files.append(firstFile+'_'+str(splits)+'.txt')

            else:
                with open(firstFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile1[partition*(splits):partition*(splits+1)]:
                        self.file_part = file.write(str(line)+'\n')
                        if (firstFile+'_'+str(splits)+'.txt') not in files:
                            files.append(firstFile+'_'+str(splits)+'.txt')
                
        partition = int(len(self.readFile2)/n_splits)
        
        for splits in range(n_splits):
            
            if splits == 0:
                with open(secondFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile2[:partition]:
                        self.file_part = file.write(str(line)+'\n')
                        if (secondFile+'_'+str(splits)+'.txt') not in files:
                            files.append(secondFile+'_'+str(splits)+'.txt')

            elif splits == 1:
                with open(secondFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile2[partition:partition*2]:
                        self.file_part = file.write(str(line)+'\n')
                        if (secondFile+'_'+str(splits)+'.txt') not in files:
                            files.append(secondFile+'_'+str(splits)+'.txt')

            else:
                with open(secondFile+'_'+str(splits)+'.txt', 'w') as file:
                    for line in self.readFile2[partition*(splits):partition*(splits+1)]:
                        self.file_part = file.write(str(line)+'\n')
                        if (secondFile+'_'+str(splits)+'.txt') not in files:
                            files.append(secondFile+'_'+str(splits)+'.txt')
 
        my_files.multiProc(files, 2)
                
        self.split_timer = time.time() - start_timer  
        
if __name__ == '__main__':

    # Create python file object
    my_files = PortfolioProject()
    
    # Read in txt file
    my_files.readFile('hugefile1.txt', 'hugefile2.txt')

    print('Only the first 5 values will appear below...\n')
    print('First File: ', my_files.readFile1[:5], '\n')
    print('Second File: ', my_files.readFile2[:5], '\n')
    print('Total time to read in data in seconds: ', my_files.read_timer, '\n')

    # Sum file lines employing brute force into new output file
    my_files.bruteForce_sumFileLines()
    print('First 5 bruteforce sum values are: ', my_files.sumFiles[:5], '\n')
    print('Total time for brute force execution in seconds: ', my_files.brute_timer, '\n')
    
    # Sum file lines employing concurrency into new output
    my_files.concurrency(2)
    print('First 5 concurrency sum values are: ', my_files.conc_sumFiles[:5], '\n')
    print('Total time for concurrency execution in seconds: ', my_files.conc_timer, '\n')
    
    # Sum file lines employing multithreading into new output
    files = [my_files.readFile1, my_files.readFile2]
    my_files.multiProc(files, 2)
    print('First 5 multiprocessing sum values are: ', my_files.conc_sumFiles[:5], '\n')
    print('Total time for multiprocessing execution in seconds: ', my_files.mp_timer, '\n')
    
    # Split hugefiles into 10 
    my_files.splitFiles('hugefile1.txt', 'hugefile2.txt', 10)
    print('Total time for splitting and multiprocessing of files (10 each) execution in seconds: ', my_files.split_timer)
    