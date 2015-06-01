from __future__ import division
import csv
import re
import sys
import pandas as pd 
import numpy as np
import collections

"""
divided fare
"""

if __name__ == '__main__':
	data = pd.read_csv('data/all_data_2.csv')

	data['Fare_d'] = pd.Series(str(np.nan), index=data.index)


	all_ticket = data.Ticket.value_counts()
	print all_ticket

	for index,row in data.iterrows():

		data.ix[index,'Fare_d'] = row['Fare']/all_ticket[row['Ticket']]

	data.to_csv('data/all_data_3.csv',mode = 'w',index = False)