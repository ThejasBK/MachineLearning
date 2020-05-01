import pandas as pd

def gender(sex):
    if sex == 'male':
        return 1
    else:
        return 0
        
def embark(x):
    if x == 'S':
        return 1
    elif x == 'C':
        return 2
    else:
        return 0
        
data = pd.read_csv('titanic_train.csv')
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
data.drop(['Name','Age','Ticket'],axis = 1,inplace = True)
data['sex'] = data['Sex'].apply(gender)
data.drop('Sex',axis = 1,inplace = True)
sns.heatmap(data.isna())
data.drop('Cabin',axis = 1,inplace = True)
data['Embarked'] = data['Embarked'].apply(embark)
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 2).fit(data)
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(data['sex'],km.labels_))
print(classification_report(data['sex'],km.labels_))
