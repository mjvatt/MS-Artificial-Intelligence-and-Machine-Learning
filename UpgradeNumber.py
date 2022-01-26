# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:44:43 2021

@author: mjvat
"""

import random

class rand_numberUpgrade(): 

	def __init__(self, rand_numbers=[]):

		self.rand_numbers = []

	def rng(self, rand):

		return ''.join(random.sample(rand, 10))

	def upgrade(self, check_num):
        
		for i in range(len(check_num)-1, 0, -1):

			if(check_num[i] > check_num[i-1]):

				first = check_num[i-1]
				second = check_num[i]

				upgraded_1 = check_num[0:check_num.find(first)]
				upgraded_2 = check_num[check_num.find(second)]
				upgraded_3 = check_num[check_num.find(first)]
				upgraded_4 = check_num[check_num.find(second)+1:]

				upgraded = upgraded_1 + upgraded_2 + upgraded_3 + upgraded_4
                
				return upgraded
	
		return 'There was nothing to change, no item swap will enlarge value.'

if __name__ == '__main__':

	rand_num = rand_numberUpgrade()
	rand_num.rand_numbers = ['0','1','2','3','4','5','6','7','8','9']
	rand_num.rng = rand_num.rng(rand_num.rand_numbers)
	rand_num.upgraded = rand_num.upgrade(rand_num.rng)

	print('Random rand_number generated: ', rand_num.rng, '\n')
	print('Upgraded rand_number to larger value: ', rand_num.upgraded, '\n')
    
    
