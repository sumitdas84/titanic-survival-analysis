from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

if __name__ == '__main__':
	
	s_f = 0
	s_m = 0
	d_f = 0
	d_m = 0

	from_csv = pd.read_csv('data/train.csv')

	for i in range(0,len(from_csv)):
		if from_csv['Sex'][i] == 'female' and from_csv['Survived'][i] == 1:
			s_f = s_f + 1
		if from_csv['Sex'][i] == 'male' and from_csv['Survived'][i] == 1:
			s_m = s_m + 1
		if from_csv['Sex'][i] == 'female' and from_csv['Survived'][i] == 0:
			d_f = d_f + 1
		if from_csv['Sex'][i] == 'male' and from_csv['Survived'][i] == 0:
			d_m = d_m + 1

	print  'female survived = ', s_f/(s_f + d_f) * 100 
	print  'male survived = ',s_m /(s_m + d_m) * 100
	print  'female dead = ',d_f /  (s_f + d_f)*100
	print  'male dead = ',d_m / (s_m + d_m)*100