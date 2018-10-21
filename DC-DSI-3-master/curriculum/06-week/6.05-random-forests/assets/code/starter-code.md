# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 08:05:50 2016

@author: JosephNelson
"""

import pandas as pd
df = pd.read_csv('./assets/datasets/car.csv')
df.head()

df.acceptability.unique() # shows our y

# encode acceptability
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(df['acceptability'])
X = pd.get_dummies(df.drop('acceptability', axis=1))

X.head() # did it work?


# get the classifiers
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier

cv = StratifiedKFold(y, n_folds=3, shuffle=True, random_state=41)

dt = DecisionTreeClassifier()
s = cross_val_score(dt, X, y, cv=cv, n_jobs=-1)
print "{} Score:\t{:0.3} ± {:0.3}".format("Decision Tree", s.mean().round(3), s.std().round(3))

# instantiate
bdt = BaggingClassifier(DecisionTreeClassifier())
rf = RandomForestClassifier(n_jobs=-1)
et = ExtraTreesClassifier(n_jobs=-1)

def score(model, name):
    s = cross_val_score(model, X, y, cv=cv, n_jobs=-1)
    print "{} Score:\t{:0.3} ± {:0.3}".format(name, s.mean().round(3), s.std().round(3))

# how did they do?!
score(dt, "Decision Tree")
score(bdt, "Bagging DT")
score(rf, "Random Forest")
score(et, "Extra Trees")