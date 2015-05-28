from __future__ import division
import numpy as np
import csv
import pandas as pd
import math
import re
import sklearn.ensemble as ske

with open('data/train_random_age.csv') as csvfile:
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

		
		li = [int(row[2]),gender,int(row[6]),int(row[7]),float(row[5])]
		X.append(li[:-1])
		Y.append(li[4])
	
with open('data/test.csv') as csvfile:
	csvreader = csv.reader(csvfile)
	header = csvreader.next()
	X = []
	Y = []
	test = []
	train = []
	for row in csvreader:
		if(row[3]=='male'):
			gender = 0
		else:
			gender = 1

		if(row[4]):
				li = [int(row[1]),gender,int(row[5]),int(row[6]),float(row[4])]
				X.append(li[:-1])
				Y.append(li[4])
		else:
				test.append([int(row[1]),gender,int(row[5]),int(row[6])])

X = np.array(X)
Y = np.array(Y)
test_array = np.array(test)
rf = ske.RandomForestClassifier(n_estimators=100)

rf_fit = rf.fit(X, Y)
prediction = rf.predict(test_array)
prediction = np.array(prediction)

data_test = pd.read_csv('data/test.csv')

for j in prediction:
	for i in xrange(0,len(data_test)):
		if math.isnan(float(data_test['Age'][i])):
			data_test['Age'][i] = int(j)
			break

data_train = pd.read_csv('data/train_random_age.csv')
data_train.loc[data_train['Sex']=='male','Sex'] = 0
data_train.loc[data_train['Sex']!='male','Sex'] = 1

train_data_array = np.array(data_train[['Pclass','Age','Sex','SibSp','Parch','Survived']])

data_test.loc[data_test['Sex']=='male','Sex'] = 0
data_test.loc[data_test['Sex']!='male','Sex'] = 1

test_data_array = np.array(data_test[['Pclass','Age','Sex','SibSp','Parch']])
new_X = train_data_array[0::,:-1:]
new_Y = train_data_array[0::,5:6:1]
new_Y = np.asarray(new_Y).ravel()

rf1 = ske.RandomForestClassifier(n_estimators=100)
rf1_fit = rf1.fit(new_X, new_Y)
prediction = rf1.predict(test_data_array)
prediction = np.array(prediction)

# print data_test
data_test['Survived'] = 1
j = 0
for i in prediction:
	data_test['Survived'][j] = int(i)
	j+=1
	# print i

my_result =  data_test[['PassengerId','Survived']]
print my_result.dtypes
# my_result.dtypes = np.int64
my_result.to_csv('data/train_random_survival.csv',mode = 'w', index=False)