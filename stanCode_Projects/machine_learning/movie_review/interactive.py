"""
File: interactive.py
Name: Jessica
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""
import util
import submission

def main():
	trainExamples = util.readExamples('polarity.train')
	validationExamples = util.readExamples('polarity.dev')
	featureExtractor = submission.extractWordFeatures
	weights = submission.learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=40, alpha=0.01)
	util.interactivePrompt(featureExtractor, weights)

if __name__ == '__main__':
	main()
