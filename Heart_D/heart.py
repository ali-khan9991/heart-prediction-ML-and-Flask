import numpy as np
import pandas as pd
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv('heart.csv')
X = data[["thalachh","oldpeak","caa","cp","exng","chol","age","trtbps","slp","sex"]]
X = np.array(X)
Y = data['output']
Y = np.array(Y)
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)
clf = RandomForestClassifier(n_estimators=168,criterion='gini',max_depth=6,max_features=2,min_samples_leaf=8).fit(X_train,y_train)
pickle.dump(clf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

