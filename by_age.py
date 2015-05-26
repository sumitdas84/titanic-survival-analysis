from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

"""
this model find out name prefix like miss, master ... 
we use name for assingning missing values of age

"""
if __name__ == '__main__':
	
	age_grp = {}
	
	from_csv = pd.read_csv('data/train.csv')
	
	for i in range (0, len(from_csv)):
		dumb = from_csv['Name'][i]
		dumb = dumb.split(" ")
		for prefix in dumb:
			if "." in prefix and not math.isnan(float(from_csv['Age'][i])):
				if age_grp.has_key(prefix):
					age_grp[prefix].append(float(from_csv['Age'][i]))
					break
				else:
					age_grp[prefix] = []
					age_grp[prefix].append(float(from_csv['Age'][i]))
					break
	
	for key in age_grp:
		print key, age_grp[key]