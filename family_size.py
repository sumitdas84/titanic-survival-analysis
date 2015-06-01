from __future__ import division
import csv
import re
import sys
import pandas as pd 
import numpy as np
import collections

"""
family_size
"""

if __name__ == '__main__':
	data = pd.read_csv('data/all_data_3.csv')

	data['Family_size'] = pd.Series(str(np.nan), index=data.index)


	for index,row in data.iterrows():

		data.ix[index,'Family_size'] = 1 + row['Parch'] + row['SibSp']

	data.to_csv('data/all_data_4.csv',mode = 'w',index = False)