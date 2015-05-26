from __future__ import division
import sys
import csv

if __name__ == '__main__':
	with open('train.csv', 'rb') as f:
		reader = csv.reader(f)
		s_f = 0
		s_m = 0
		d_f = 0
		d_m = 0
		cnt = 0
		for row in reader:
			if row[1] == '1' and row[4] == 'female':
				s_f = s_f + 1
			if row[1] == '1' and row[4] == 'male':
				s_m = s_m + 1
			if row[1] == '0' and row[4] == 'female':
				d_f = d_f + 1
			if row[1] == '0' and row[4] == 'male':
				d_m = d_m + 1
			cnt = cnt + 1

		print  'female survived = ', s_f/(s_f + d_f) * 100 
		print  'male survived = ',s_m /(s_m + d_m) * 100
		print  'female dead = ',d_f /  (s_f + d_f)*100
		print  'male dead = ',d_m / (s_m + d_m)*100