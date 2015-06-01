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
	data = pd.read_csv('data/all_data_1.csv')

	data['Family'] = pd.Series(str(np.nan), index=data.index)

	for index,row in data.iterrows():
		
		sirname = row['Name'].split(",")
		family_id = sirname[0]+"_"+str(1 + row['Parch'] + row['SibSp']) 

		data.ix[index,'Family'] = str(family_id)

	data.to_csv('data/all_data_2.csv',mode = 'w',index = False)