# -*- coding: utf-8 -*-
"""spammail.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19xgtIdHwMToEAB6mXHD92Va5qUw2x12G

IMPORTING DEPENDENCIES
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Datacollection and preprocessing"""

#loading the data from csvfile to a pandas Dataframe
raw_mail_data=pd.read_csv('mail_data.csv')

print(raw_mail_data)

#replace the num values with a null string
mail_data=raw_mail_data.where((pd.notnull(raw_mail_data)),'')

#printing the first 5 rows of the dataframe
mail_data.head()

#checking the number of rows and columns in the dataframe
mail_data.shape

"""Labelencoding"""

#label spam mail as 0 and ham mail as 1
mail_data.loc[mail_data['Category']=='spam','Category',]=0
mail_data.loc[mail_data['Category']=='ham','Category',]=1

"""spam=0
ham=1
"""

#seperating the data as text and label
X=mail_data['Message']
Y=mail_data['Category']

print(X)

print(Y)

"""Spilitting the data into training data &testdata"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

"""FEATURE EXTRACTION"""

#transform the text data to feature vectors that can be used as input to the logistuc regression model
feature_extraction=TfidfVectorizer(min_df=1,stop_words='english',lowercase=True)
X_train_features=feature_extraction.fit_transform(X_train)
X_test_features=feature_extraction.transform(X_test)

#conver Y_Train and Y_test values as integers
Y_train=Y_train.astype('int')
Y_test=Y_test.astype('int')

print(X_train)

print(X_train_features)

"""Training model

logistic regression
"""

model=LogisticRegression()

#training the logistic regression model with the training data

model.fit(X_train_features,Y_train)

"""Evaluating the trained model"""

#prediction on training data
prediction_on_training_data=model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)

print('Accuracy on training data:',accuracy_on_training_data)

#prediction on test data
prediction_on_test_data=model.predict(X_test_features)
accuracy_on_test_data=accuracy_score(Y_test,prediction_on_test_data)

print('Accuracy on test data',accuracy_on_test_data)

"""Building a predictive system"""

def predict_email():
  input_mail=[]
#convert text to feature vectors
input_data_features=features_extraction.transform(input_mail)
#making predictions
prediction=model.predict(input_data_features)
print(prediction)
 if prediction[0] == 1:
        print("This email is likely to be a ham mail.")

    else:
        print("This email is likely to be a spam mail.")
predict_email()