import pandas as pd
import numpy as np
import random as rnd

# visualization
#import seaborn as sns
#import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


train_df = pd.read_csv('./AnimalMovement.csv')
test_df = pd.read_csv('./AnimalMovement.csv')
combine=[train_df, test_df]

X_train = train_df.drop(["DisasterPrediction", "Species", "SiteID", "DateTime", "CaptureEventID"], axis=1)
Y_train = train_df["DisasterPrediction"]
X_test  = test_df.drop(["DisasterPrediction","Species", "SiteID", "DateTime", "CaptureEventID"], axis=1).copy()
X_train.shape, Y_train.shape, X_test.shape



from sklearn.ensemble import RandomForestClassifier as RFC
rfc_b = LogisticRegression()
rfc_b.fit(X_train,Y_train)
Y_pred = rfc_b.predict(X_train)
rfc_knn = round(rfc_b.score(X_train, Y_train) * 100, 2)
rfc_knn

# Save your model
from sklearn.externals import joblib
joblib.dump(rfc_b, 'model.pkl')
print("Model dumped!")

# Load the model that you just saved
rfc_b = joblib.load('model.pkl')

# Saving the data columns from training
model_columns = list(X_train.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
