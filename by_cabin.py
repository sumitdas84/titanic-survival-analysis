from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

"""
this script analyze cabin and print some result in %
"""
"""
iter on dataframe :
	for index,row in new_csv.iterrows():

write in csv :
	new_csv.to_csv('data/train_extract.csv',mode = 'w', index=False)
"""

if __name__ == '__main__':
	from_csv = pd.read_csv('data/train.csv')
	new_csv = from_csv
	new_csv = new_csv.dropna(subset= ['Cabin'])
	for index,row in new_csv.iterrows():
		new_csv.ix[index,'Cabin'] =  row['Cabin'][0:1]


	all_per_cabin = new_csv.Cabin.value_counts()
	
	new_csv = new_csv[new_csv.Survived == 1]

	s_per_cabin = new_csv.Cabin.value_counts()

	print s_per_cabin/all_per_cabin



	
