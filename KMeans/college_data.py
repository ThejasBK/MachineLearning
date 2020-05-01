import pandas as pd

def convert(cluster):
    if cluster == 'Yes':
        return 1
    else:
        return 0
        
data = pd.read_csv('College_Data',index_col=0)
data.head()
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.heatmap(data.isna())
data.describe()
data['Cluster'] = data['Private'].apply(convert)
data.drop('Private',axis = 1,inplace = True)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2).fit(data)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(data['Cluster'],kmeans.labels_))
print(confusion_matrix(data['Cluster'],kmeans.labels_))
