import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
data = pd.read_csv('testing_data_with_weather_info_week_2.csv')
data.head()
data.info()
x = data[['min','max','stp','wdsp','prcp','fog']]
y = data['temp']

#Start of prediction
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.3)
lr.fit(xtrain,ytrain)
pred = lr.predict(xtest)
plt.scatter(ytest,pred)
sns.distplot((ytest - pred))

#Checking the metrics scores for the model
from sklearn import metrics
metrics.mean_squared_error(ytest,pred)
metrics.mean_absolute_error(ytest,pred)
