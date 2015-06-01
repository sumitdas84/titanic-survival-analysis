from __future__ import division
import csv
import re
import sys
import pandas as pd 
import numpy as np
import collections

"""
title
"""

if __name__ == '__main__':
	data = pd.read_csv('data/all_data_4.csv')

	data['Title'] = pd.Series(str(np.nan), index=data.index)
	known = ['Miss.','Mrs.','Mr.','Master.']

	for index,row in data.iterrows():
		dumb = row['Name']
		dumb = dumb.split(" ")
		for prefix in dumb:
			if "." in prefix:
				if prefix in known:
					data.ix[index,'Title'] = prefix
					break
				else:
					data.ix[index,'Title'] = 'u_'+row['Sex']
					break

		 

	data.to_csv('data/all_data_5.csv',mode = 'w',index = False)