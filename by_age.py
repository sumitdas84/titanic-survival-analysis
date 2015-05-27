from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

"""
this model find out name prefix like miss master
we use name for assingning missing values of age 
"""

if __name__ == '__main__':
	
	# finding out average of age according to "Mr.","Mrs.", etc. and store it in "age_grp_avg"
	age_grp = {}
	
	from_csv = pd.read_csv('data/train.csv')
	
	for i in range (0, len(from_csv)):
		dumb = from_csv['Name'][i]
		dumb = dumb.split(" ")
		for prefix in dumb:
			if "." in prefix and  not math.isnan(float(from_csv['Age'][i])):
				if age_grp.has_key(prefix):
					age_grp[prefix].append(float(from_csv['Age'][i]))
					break
				else:
					age_grp[prefix] = []
					age_grp[prefix].append(float(from_csv['Age'][i]))
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
				from_csv['Age'][i] = str(age_grp_avg[prefix])
				break

	# store output in train_1.csv
	from_csv.to_csv('data/train_1.csv')