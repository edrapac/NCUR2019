import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy.stats import spearmanr

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing

data = 'training-passwords_similarities.csv'
accounts = pd.read_csv(data)

data = "training_passwords_similarities(firstname only).csv"
accounts = pd.read_csv(data)
accounts.head()

accounts.columns = ['Fname', 'Password','score']

accounts_data = accounts.ix[:,(0,1)].values #using fname and password
y = accounts.ix[:,2] #taget variable
x = scale(accounts_data)