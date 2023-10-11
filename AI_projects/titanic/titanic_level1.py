"""
File: titanic_level1.py
Name: 
----------------------------------
This file builds a machine learning algorithm from scratch 
by Python. We'll be using 'with open' to read in dataset,
store data into a Python dict, and finally train the model and 
test it on kaggle website. This model is the most flexible among all
levels. You should do hyper-parameter tuning to find the best model.
"""

import math
import util
TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename: str, data: dict, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be processed
	:param data: an empty Python dictionary
	:param mode: str, indicating if it is training mode or testing mode
	:param training_data: dict[str: list], key is the column name, value is its data
						  (You will only use this when mode == 'Test')
	:return data: dict[str: list], key is the column name, value is its data
	"""
	############################
	# TODO:

	if mode =='Train':
		data = {'Survived': [], 'Pclass': [], 'Sex': [], 'Age': [], 'SibSp': [], 'Parch': [], 'Fare': [],
				'Embarked': []}
		# sum_age = 0
		# sum_fare = 0
		with open(filename, 'r') as f:
			first = True
			for line in f:
				if first:
					first = False
				else:
					line = line.strip().split(',')
					line.pop(11)
					line.pop(9)
					line.pop(4)
					line.pop(3)
					line.pop(0)
					if line[2] == 'female':
						line[2] = 0
					elif line[2] == 'male':
						line[2] = 1
					if line[7] == 'S':
						line[7] = 0
					elif line[7] == 'C':
						line[7] = 1
					elif line[7] == 'Q':
						line[7] = 2
					if '' not in line:
						data['Survived'].append(float(line[0]))
						data['Pclass'].append(int(line[1]))
						data['Sex'].append(line[2])
						data['Age'].append(float(line[3]))
						# sum_age += float(line[3])
						data['SibSp'].append(int(line[4]))
						data['Parch'].append(int(line[5]))
						data['Fare'].append(float(line[6]))
						# sum_fare += float(line[6])
						data['Embarked'].append(line[7])
			# avg_age = sum_age//len(data['Age'])
			# avg_fare = sum_fare//len(data['Fare'])
	elif mode == 'Test':
		data = {'Pclass': [], 'Sex': [], 'Age': [], 'SibSp': [], 'Parch': [], 'Fare': [],
				'Embarked': []}
		avg_age = round(sum(training_data['Age'])/len(training_data['Age']), 3)
		avg_fare = round(sum(training_data['Fare'])/len(training_data['Fare']), 3)
		with open(filename, 'r') as f:
			first = True
			for line in f:
				if first:
					first = False
				else:
					line = line.strip().split(',')
					line.pop(10)
					line.pop(8)
					line.pop(3)
					line.pop(2)
					line.pop(0)
					if line[1] == 'female':
						line[1] = 0
					elif line[1] == 'male':
						line[1] = 1
					if line[6] == 'S':
						line[6] = 0
					elif line[6] == 'C':
						line[6] = 1
					elif line[6] == 'Q':
						line[6] = 2
					data['Pclass'].append(int((line[0])))
					data['Sex'].append(line[1])
					if line[2] == '':
						data['Age'].append(avg_age)
					else:
						data['Age'].append(float(line[2]))
					data['SibSp'].append(int(line[3]))
					data['Parch'].append(int(line[4]))
					if line[5] == '':
						data['Fare'].append(avg_fare)
					else:
						data['Fare'].append(float(line[5]))
					data['Embarked'].append(line[6])


				# if mode == 'Test':


				# else:
				# 	feature_vector = feature_extractor(line, mode)
				# 	data.append(feature_vector)


	############################
	return data


def one_hot_encoding(data: dict, feature: str):
	"""
	:param data: dict[str, list], key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: dict[str, list], remove the feature column and add its one-hot encoding features
	"""
	############################
	#          TODO:
	if feature == 'Sex':
		data['Sex_0'] = []
		data['Sex_1'] = []
		for i in range(len(data['Sex'])):
			if data['Sex'][i] == 0:
				data['Sex_0'].append(1)
				data['Sex_1'].append(0)
			else:
				data['Sex_0'].append(0)
				data['Sex_1'].append(1)
		data.pop('Sex')
	elif feature == 'Pclass':
		data['Pclass_0'] = []
		data['Pclass_1'] = []
		data['Pclass_2'] = []
		for i in range(len(data['Pclass'])):
			if data['Pclass'][i] == 1:
				data['Pclass_0'].append(1)
				data['Pclass_1'].append(0)
				data['Pclass_2'].append(0)
			elif data['Pclass'][i] == 2:
				data['Pclass_0'].append(0)
				data['Pclass_1'].append(1)
				data['Pclass_2'].append(0)
			else:
				data['Pclass_0'].append(0)
				data['Pclass_1'].append(0)
				data['Pclass_2'].append(1)
		data.pop('Pclass')
	elif feature == 'Embarked':
		data['Embarked_0'] = []
		data['Embarked_1'] = []
		data['Embarked_2'] = []
		for i in range(len(data['Embarked'])):
			if data['Embarked'][i] == 0:
				data['Embarked_0'].append(1)
				data['Embarked_1'].append(0)
				data['Embarked_2'].append(0)
			elif data['Embarked'] == 1:
				data['Embarked_0'].append(0)
				data['Embarked_1'].append(1)
				data['Embarked_2'].append(0)
			else:
				data['Embarked_0'].append(0)
				data['Embarked_1'].append(0)
				data['Embarked_2'].append(1)
		data.pop('Embarked')

	############################
	return data


def normalize(data: dict):
	"""
	:param data: dict[str, list], key is the column name, value is its data
	:return data: dict[str, list], key is the column name, value is its normalized data
	"""
	############################
	#          TODO:
	min_age = min(data['Age'])
	max_age = max(data['Age'])
	min_sibsp = min(data['SibSp'])
	max_sibsp = max(data['SibSp'])
	min_parch = min(data['Parch'])
	max_parch = max(data['Parch'])
	min_fare = min(data['Fare'])
	max_fare = max(data['Fare'])
	for i in range(len(data['Age'])):
		data['Age'][i] = (data['Age'][i]-min_age)/(max_age-min_age)
		data['SibSp'][i] = (data['SibSp'][i]-min_sibsp)/(max_sibsp-min_sibsp)
		data['Parch'][i] = (data['Parch'][i]-min_parch)/(max_parch-min_parch)
		data['Fare'][i] = (data['Fare'][i] - min_fare) / (max_fare - min_fare)

	############################
	return data


def learnPredictor(inputs: dict, labels: list, degree: int, num_epochs: int, alpha: float):
	"""
	:param inputs: dict[str, list], key is the column name, value is its data
	:param labels: list[int], indicating the true label for each data
	:param degree: int, degree of polynomial features
	:param num_epochs: int, the number of epochs for training
	:param alpha: float, known as step size or learning rate
	:return weights: dict[str, float], feature name and its weight
	"""
	# Step 1 : Initialize weights
	weights = {}  # feature => weight
	keys = list(inputs.keys())
	if degree == 1:
		for i in range(len(keys)):
			weights[keys[i]] = 0
	elif degree == 2:
		for i in range(len(keys)):
			weights[keys[i]] = 0
		for i in range(len(keys)):
			for j in range(i, len(keys)):
				weights[keys[i] + keys[j]] = 0
	# Step 2 : Start training
	# TODO:
	phi_x = {}
	for i in range(num_epochs):
		for j in range(len(inputs['Age'])):
			# phi_x = {column_name:value}
			# Step 3 : Feature Extract
			# TODO:
			for column_name, value in inputs.items():
				phi_x[column_name] = value[j]
			if degree == 1:
				phi_x = phi_x
			elif degree == 2:
				for x_1 in range(len(keys)):
					for x_2 in range(x_1, len(keys)):
						phi_x[keys[x_1] + keys[x_2]] = inputs[keys[x_1]][j] * inputs[keys[x_2]][j]
			k = util.dotProduct(phi_x, weights)
			s_k = 1 / (1 + math.exp((-k)))
			y = labels[j]
			# Step 4 : Update weights
			# TODO:
			util.increment(weights, -alpha * (s_k - y), phi_x)

	return weights
