import pandas as pd
data = pd.read_csv('winequality.csv')
data.head()
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.heatmap(data.isna())
sns.pairplot(data)

x = data[['fixed acidity','density','pH','alcohol']]
y = data['quality']

#Developing a model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.3)
lr = LinearRegression().fit(xtrain,ytrain)
pred = lr.predict(xtest)
from sklearn.metrics import mean_squared_error,mean_absolute_error
metrics.mean_absolute_error(ytest,pred)     #Score = 0.5457492989618039
metrics.mean_squared_error(ytest,pred)      #Score = 0.4863729739612816
plt.scatter(ytest,pred)
sns.lmplot(y = 'alcohol',x = 'quality',data = data)
plt.scatter('alcohol','quality',data = data)
