import csv
import re
import sys
import pandas as pd 
import numpy as np
import collections

"""
family id
"""

if __name__ == '__main__':

	data = pd.read_csv('data/test_5.csv')
	data1 = pd.read_csv('data/train_5.csv')

	for index,row in data.iterrows():
		if type(row['Cabin']) is str:
			data.ix[index,'Cabin'] = str(row['Cabin'][0])
		else :
			data.ix[index,'Cabin'] = str('N/A')
	for index1,row1 in data1.iterrows():
		if type(row1['Cabin']) is str:
			data1.ix[index1,'Cabin'] = str(row1['Cabin'][0])
		else :
			data1.ix[index1,'Cabin'] = str('N/A')

	data.to_csv('data/test_6.csv',mode = 'w',index = False)
	data1.to_csv('data/train_6.csv',mode = 'w',index = False)