import sklearn.ensemble as ske
import numpy as np
import csv
import pandas as pd
import math

from_csv = pd.read_csv('data/train.csv')
# print x
with open('data/train.csv') as csvfile:
	csvreader = csv.reader(csvfile)
	header = csvreader.next()
	X = []
	Y = []
	test = []
	train = []
	for row in csvreader:
		if(row[4]=='male'):
			gender = 0
		else:
			gender = 1

		if(row[5]):
				li = [int(row[2]),gender,int(row[6]),int(row[7]),int(row[1]),float(row[5])]
				X.append(li[:-1])
				Y.append(li[5])
				train.append(li)
		else:
				test.append([int(row[2]),gender,int(row[6]),int(row[7]),int(row[1])])

	X = np.array(X)
	Y = np.array(Y)
	test_array = np.array(test)


rf = ske.RandomForestClassifier(n_estimators=100)

rf_fit = rf.fit(X, Y)
prediction = rf.predict(test_array)
prediction = np.array(prediction)
# c = np.hstack((test_array, np.atleast_2d(prediction).T))


# train = np.concatenate((train,c))
for j in prediction:
	for i in xrange(0,len(from_csv)):
		if math.isnan(float(from_csv['Age'][i])):
			from_csv['Age'][i] = int(j)
			break

from_csv.to_csv('data/train_random_age.csv',mode = 'w', index=False)