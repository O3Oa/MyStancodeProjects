#!/usr/bin/python

import math
import random
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Milestone 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # d_words = {}
    # for word in x.split():
    #     if word not in d_words:
    #         d_words[word] = 1
    #     else:
    #         d_words[word] += 1
    # return d_words
    d_words = defaultdict(int)
    for word in x.split():
        d_words[word] += 1
    return d_words
    # END_YOUR_CODE


############################################################
# Milestone 4: Sentiment Classification

def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    """
    weights = defaultdict(int)  # the weight vector

    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    # print(trainExamples)
    # for example in trainExamples:
    #     data = example[0]
    #     label = example[1]
    # example_list = []
    # example_dict = {}
    # h = predict(x)
    # def predictor(x):
    #     phi_x = featureExtractor(x)
    #     k = dotProduct(phi_x, weights)
    #     s_k = 1/(1+math.exp((-k)))
    #     return 1 if s_k >= 0.5 else 0

    #training data
    for i in range(numEpochs):
        for data, label in trainExamples:
            phi_x = featureExtractor(data)
            k = dotProduct(phi_x, weights)
            s_k = 1 / (1 + math.exp((-k)))
            y = 1 if label == 1 else 0
            weights = increment(weights, -alpha*(s_k-y), phi_x)

        def predictor(x):
            phi = featureExtractor(x)
            pk = dotProduct(phi, weights)
            s_pk = 1 / (1 + math.exp((-pk)))
            return 1 if s_pk >= 0.5 else -1

        training_error = evaluatePredictor(trainExamples, predictor)
        validation_error = evaluatePredictor(validationExamples, predictor)
        print(f'Training Error:({i} epoch):{training_error}')
        print(f'Validation Error:({i} epoch):{validation_error}')

    return weights

    # END_YOUR_CODE


############################################################
# Milestone 5a: generate test case

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and values are their word occurrence.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """
        phi_key = []
        # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
        for i in range(random.randrange(1, len(weights))):
            phi_key.append(random.choice(list(weights)))
        phi_str = ' '.join(phi_key)
        phi = extractWordFeatures(phi_str)
        k = dotProduct(phi, weights)
        y = +1 if k >= 0.5 else -1
        # END_YOUR_CODE
        return phi, y

    return [generateExample() for _ in range(numExamples)]


############################################################
# Milestone 5b: character features

def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """

    def extract(x: str) -> Dict[str, int]:
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        d_words = defaultdict(int)
        word = x.split()
        word_c = ''.join(word)
        for i in range(len(word_c)-n+1):
            if word_c[i:i+n] not in d_words:
                d_words[word_c[i:i+n]] = 1
            else:
                d_words[word_c[i:i+n]] += 1
        return d_words

        # END_YOUR_CODE

    return extract


############################################################
# Problem 3f: 
def testValuesOfN(n: int):
    """
    Use this code to test different values of n for extractCharacterFeatures
    This code is exclusively for testing.
    Your full written solution for this problem must be in sentiment.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, alpha=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(trainExamples,
                                   lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples,
                                        lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))

