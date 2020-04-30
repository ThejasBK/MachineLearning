import pandas as pd
patientInfo = pd.read_csv('PatientInfo.csv')
weather = pd.read_csv('Weather.csv')
weather.head()
patientInfo.head()
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
plt.figure(figsize = (25,4))   
sns.countplot(patientInfo['province'])    #No. of cases in state of South Korea
sns.countplot(patientInfo['sex'])    #No. of male and female affected in south Korea
sns.countplot(patientInfo['sex'],hue = patientInfo['age'])     #Male and female based on ages
for i in range(3326):
    patientInfo['age'][i] = str(patientInfo['age'][i])[:2]
for i in range(3326):
    if patientInfo['age'][i][1] == 's':
        patientInfo['age'][i] = str(patientInfo['age'][i])[:1]
sns.heatmap(patientInfo.isna())
patientInfo.drop(['global_num','disease','infection_case','infection_order','infected_by',
              'contact_number','symptom_onset_date','confirmed_date','released_date','deceased_date'],axis = 1,inplace = True)
patientInfo.drop(['age'],inplace = True,axis = 1)
patientInfo['avg_temp'] = None
for i in range(3326):
    if patientInfo['sex'][i] == 'male':
        patientInfo['sex'][i] = 1
    else:
        patientInfo['sex'][i] = 0
for i in range(3326):
    for j in range(25135):
        if patientInfo['province'][i] == weather['province'][j]:
            patientInfo['avg_temp'][i] = weather['avg_temp'][j]
patientInfo.drop(['country','province','city','state'],axis = 1,inplace = True)
patientInfo.dropna(inplace = True)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
x = pd.DataFrame()
x['birth_year'] = patientInfo['birth_year']
x['avg_temp'] = patientInfo['avg_temp']
import numpy as np
y = patientInfo['sex']
x = np.array(x)
y = np.array(y)
data = []
data.append(x)
data.append(y)
data = tuple(data)
kmeans.fit(data[0])
plt.scatter(data[0][:,1],data[0][:,0],c = data[1],cmap = 'inferno',marker = '.')
g = sns.PairGrid(patientInfo)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
