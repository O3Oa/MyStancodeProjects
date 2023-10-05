"""
File: boston_housing_competition.py
Name: Jessica
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""

import pandas as pd
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing
from sklearn import svm, tree
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor

TRAIN = 'boston_housing/train.csv'
TEST = 'boston_housing/test.csv'

def main():
	data_train = pd.read_csv(TRAIN)
	data_test = pd.read_csv(TEST)
	# print(data_train.count())
	# print(data_test.count())

	# Y = data_train.pop('medv')
	data_train.pop('ID')

	total_error = 0
	for i in range(100):
		train, val = model_selection.train_test_split(data_train, test_size=0.4)
		train_Y, val_Y = train.pop('medv'), val.pop('medv')
		standardizer = preprocessing.StandardScaler()
		train = standardizer.fit_transform(train)
		# print(train_Y)
		# print('-'*80)
		# print(val_Y)

		h = linear_model.LinearRegression()
		classifier = h.fit(train, train_Y)
		predictions = classifier.predict(train)
		# # print('----Training Error-----')
		# train_error = metrics.mean_squared_error(predictions, train_Y)**0.5

		# print('----Val Error-----')
		val = standardizer.transform(val)
		predictions_val = classifier.predict(val)
		val_error = metrics.mean_squared_error(predictions_val, val_Y) ** 0.5
		total_error += val_error
		# print(i,val_error)
	print('(Linear Regression) 100 times val error avg:', total_error/100)
	total_error = 0
	for i in range(100):
		train, val = model_selection.train_test_split(data_train, test_size=0.4)
		train_Y, val_Y = train.pop('medv'), val.pop('medv')
		standardizer = preprocessing.StandardScaler()
		train = standardizer.fit_transform(train)
		val = standardizer.transform(val)
		poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)
		train_poly = poly_phi_extractor.fit_transform(train)
		val_poly = poly_phi_extractor.transform(val)
		h = linear_model.LinearRegression()
		classifier = h.fit(train_poly, train_Y)
		predictions = classifier.predict(train_poly)

		# print('----Val Error-----')
		predictions_val = classifier.predict(val_poly)
		val_error = metrics.mean_squared_error(predictions_val, val_Y) ** 0.5
		total_error += val_error
	print('(Linear Regression degree2) 100 times val error avg:', total_error/100)

	total_error = 0
	for i in range(100):
		train, val = model_selection.train_test_split(data_train, test_size=0.4)
		train_Y, val_Y = train.pop('medv'), val.pop('medv')
		regr = svm.SVR()
		classifier = regr.fit(train, train_Y)
		predictions = classifier.predict(train)

		# print('----Val Error-----')
		predictions_val = classifier.predict(val)
		val_error = metrics.mean_squared_error(predictions_val, val_Y) ** 0.5
		total_error += val_error
	print('(SVM) 100 times val error avg:', total_error/100)

	total_error = 0
	for i in range(100):
		train, val = model_selection.train_test_split(data_train, test_size=0.4)
		train_Y, val_Y = train.pop('medv'), val.pop('medv')
		standardizer = preprocessing.StandardScaler()
		train = standardizer.fit_transform(train)
		val = standardizer.transform(val)
		#
		# poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)
		# train = poly_phi_extractor.fit_transform(train)
		# val = poly_phi_extractor.transform(val)
		#
		dtr = tree.DecisionTreeRegressor(max_depth=3)
		classifier = dtr.fit(train, train_Y)
		predictions = classifier.predict(train)

		# print('----Val Error-----')
		predictions_val = classifier.predict(val)
		val_error = metrics.mean_squared_error(predictions_val, val_Y) ** 0.5
		total_error += val_error
	print('(decision tree) 100 times val error avg:', total_error / 100)
	# print(val, data_test)
	# test_id = data_test.ID.tolist()
	# print(test_id)
	# data_test.pop('ID')
	# data_test = standardizer.transform(data_test)
	# predictions_test = classifier.predict(data_test)
	# print(predictions_test)
	# print(type(test_id))
	# out_file(test_id, predictions_test, 'boston_housing_decision_tree.csv')

	total_error = 0
	for i in range(100):
		train, val = model_selection.train_test_split(data_train, test_size=0.4)
		train_Y, val_Y = train.pop('medv'), val.pop('medv')
		standardizer = preprocessing.StandardScaler()
		train = standardizer.fit_transform(train)
		val = standardizer.transform(val)
		#
		# poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)
		# train = poly_phi_extractor.fit_transform(train)
		# val = poly_phi_extractor.transform(val)
		# #
		regr = GradientBoostingRegressor()
		classifier = regr.fit(train, train_Y)
		predictions = classifier.predict(train)

		# print('----Val Error-----')
		predictions_val = classifier.predict(val)
		val_error = metrics.mean_squared_error(predictions_val, val_Y) ** 0.5
		total_error += val_error
	print('(GradientBoost) 100 times val error avg:', total_error / 100)
	print(val, data_test)
	test_id = data_test.ID.tolist()
	# print(test_id)
	data_test.pop('ID')
	data_test = standardizer.transform(data_test)
	predictions_test = classifier.predict(data_test)
	# print(predictions_test)
	# print(type(test_id))
	out_file(test_id, predictions_test, 'boston_housing_decision_tree.csv')

def out_file(test_ID,predictions, filename):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	with open(filename, 'w') as out:
		out.write('Id,medv\n')
		for i in range(len(test_ID)):
			out.write(str(test_ID[i])+','+str(predictions[i])+'\n')
	print('===============================================')

if __name__ == '__main__':
	main()
