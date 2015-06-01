from __future__ import division
import sys
import csv
import pandas as pd
import numpy as np
import re
import math

"""
this script analyze pclass and print some result in %
"""


if __name__ == '__main__':
	from_csv = pd.read_csv('data/train.csv')

	all_per_Pclass = from_csv.Pclass.value_counts()
	
	from_csv = from_csv[from_csv.Survived == 1]

	s_per_Pclass = from_csv.Pclass.value_counts()

	print s_per_Pclass/all_per_Pclass




	
