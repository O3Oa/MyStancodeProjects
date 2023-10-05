"""
File: titanic_level2.py
Name: 
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
						  (You will only use this when mode == 'Test')
	:return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	labels = None
	################################
	#                              #
	#             TODO:            #
	if mode == 'Train':
		data.pop('PassengerId')
		data.pop('Name')
		data.pop('Ticket')
		data.pop('Cabin')
		data = data.dropna()
		# Changing 'male' to 1, 'female' to 0
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data.loc[data.Embarked == 'S', 'Embarked'] = 0
		data.loc[data.Embarked == 'C', 'Embarked'] = 1
		data.loc[data.Embarked == 'Q', 'Embarked'] = 2
		# labels = data.Survived
		# data.pop('Survived')
		labels = data.pop('Survived')
	elif mode == 'Test':
		training_data = training_data.mean()
		data.pop('PassengerId')
		data.pop('Name')
		data.pop('Ticket')
		data.pop('Cabin')
		# Changing 'male' to 1, 'female' to 0
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data.loc[data.Embarked == 'S', 'Embarked'] = 0
		data.loc[data.Embarked == 'C', 'Embarked'] = 1
		data.loc[data.Embarked == 'Q', 'Embarked'] = 2
		data['Age'].fillna(round(training_data.Age, 3), inplace=True)
		data['Fare'].fillna(round(training_data.Fare, 3), inplace=True)


	################################
	if mode == 'Train':
		return data, labels
	elif mode == 'Test':
		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	############################
	#                          #
	#          TODO:           #
	if feature == 'Sex':
		# One hot encoding for a new category Male
		data['Sex_1'] = 0
		data.loc[data.Sex == 1, 'Sex_1'] = 1
		# One hot encoding for a new category Female
		data['Sex_0'] = 0
		data.loc[data.Sex == 0, 'Sex_0'] = 1
		# No need Sex anymore!
		data.pop('Sex')
	elif feature == 'Pclass':
		# One hot encoding for a new category FirstClass
		data['Pclass_0'] = 0
		data.loc[data.Pclass == 1, 'Pclass_0'] = 1
		# One hot encoding for a new category SecondClass
		data['Pclass_1'] = 0
		data.loc[data.Pclass == 2, 'Pclass_1'] = 1
		# One hot encoding for a new category ThirdClass
		data['Pclass_2'] = 0
		data.loc[data.Pclass == 3, 'Pclass_2'] = 1
		data.pop('Pclass')
	elif feature == 'Embarked':
		data['Embarked_0'] = 0
		data.loc[data.Embarked == 0, 'Embarked_0'] = 1
		data['Embarked_1'] = 0
		data.loc[data.Embarked == 1, 'Embarked_1'] = 1
		data['Embarked_2'] = 0
		data.loc[data.Embarked == 2, 'Embarked_2'] = 1
		data.pop('Embarked')
	############################
	return data


def standardization(data, mode='Train'):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param mode: str, indicating the mode we are using (either Train or Test)
	:return data: DataFrame, standardized featurespoly_fea_extractor = preprocessing.PolynomialFeatures(degree=2)
	x_train = poly_fea_extractor.fit_transform(x_train)
	"""
	############################
	#                          #
	#          TODO:           #
	standardizer = preprocessing.StandardScaler()
	data = standardizer.fit_transform(data)
	return data


def main():
	"""
	You should call data_preprocess(), one_hot_encoding(), and
	standardization() on your training data. You should see ~80% accuracy on degree1;
	~83% on degree2; ~87% on degree3.
	Please write down the accuracy for degree1, 2, and 3 respectively below
	(rounding accuracies to 8 decimal places)
	TODO: real accuracy on degree1 -> 0.80196629
	TODO: real accuracy on degree2 -> 0.83707865
	TODO: real accuracy on degree3 -> 0.87640449
	"""
	data, y = data_preprocess(TRAIN_FILE)
	one_hot_encoding(data, 'Sex')
	one_hot_encoding(data, 'Pclass')
	one_hot_encoding(data, 'Embarked')
	# standardize
	standardizer = preprocessing.StandardScaler()
	data = standardizer.fit_transform(data)

	poly_fea_extractor = preprocessing.PolynomialFeatures(degree=3)
	x_train = poly_fea_extractor.fit_transform(data)

	h = linear_model.LogisticRegression(max_iter=10000)
	classifier = h.fit(x_train, y)
	acc = classifier.score(x_train, y)
	print('Degree 3 Training Acc:', acc)



if __name__ == '__main__':
	main()
