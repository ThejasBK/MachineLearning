import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv('heart.csv')
data.head()
data.describe()
sns.heatmap(data.isna())
from sklearn.model_selection import train_test_split
x = data.drop(['target'],axis = 1)
y = data['target']
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.3)
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
error_rate = []
for i in range(1,20):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(xtrain,ytrain)
    pred = knn.predict(xtest)
    error_rate.append(np.mean(pred != ytest))
plt.figure(figsize=(10,6))
plt.plot(range(1,20),error_rate,color='blue',ls='--',marker='o')
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(xtrain,ytrain)
pred = knn.predict(xtest)
pred
from sklearn.metrics import classification_report, confusion_matrix 
print(classification_report(ytest,pred))
