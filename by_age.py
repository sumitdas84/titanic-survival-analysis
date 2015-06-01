from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

"""
fill missing age data
"""

if __name__ == '__main__':
	
	# finding out average of age according to "Mr.","Mrs.", etc. and store it in "age_grp_avg"
	known = ['Miss.','Mrs.','Mr.','Master.']
	age_grp = {'Miss.':[],'Mrs.':[],'Mr.':[],'Master.':[],'female':[],'male':[]}
	
	from_csv = pd.read_csv('data/all_data.csv')
	
	for index,row in from_csv.iterrows():
		dumb = row['Name']
		dumb = dumb.split(" ")
		for prefix in dumb:
			if "." in prefix and  not math.isnan(float(row['Age'])):
				if prefix in known:
					age_grp[prefix].append(float(row['Age']))
					break
				else:
					age_grp[row['Sex']].append(float(row['Age']))
					break


	# calculate average

	age_grp_avg = {}
	for key in age_grp:
		age_grp_avg[key] = reduce(lambda x, y: x + y, age_grp[key]) / len(age_grp[key])

	# fill missing data
	for i in range (0, len(from_csv)):
		dumb = from_csv['Name'][i]
		dumb = dumb.split(" ")
		for prefix in dumb:
			if "." in prefix and  math.isnan(float(from_csv['Age'][i])):
				if prefix in known:
					from_csv['Age'][i] = str(age_grp_avg[prefix])
					break
				else:
					from_csv['Age'][i] = str(age_grp_avg[row['Sex']])
					break

	# store output in all_data_1.csv
	from_csv.to_csv('data/all_data_1.csv',mode = 'w', index=False)