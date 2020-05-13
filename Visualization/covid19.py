data = requests.get('https://api.covid19api.com/summary').text
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import demjson
data = demjson.decode(data)
for i in data:
    print(i)
total_countries = 0
for i in data['Countries']:
    total_countries += 1
print(total_countries)
print(data['Countries'][0])
dictionary_countries = {}
for i in data['Countries']:
    try:
        dictionary_countries[i['Country']] = [i['TotalConfirmed'],i['TotalDeaths'],i['TotalRecovered']]
    except:
        continue
dictionary_countries
df = pd.DataFrame()
countries = []
total_cases = []
total_deaths = []
total_confired = []
for i in dictionary_countries:
    countries.append(i)
    total_cases.append(dictionary_countries[i][0])
    total_deaths.append(dictionary_countries[i][1])
    total_confired.append(dictionary_countries[i][2])
df['Country'] = countries
df['Total Confirmed'] = total_cases
df['Total Deaths'] = total_deaths
df['Total Recovered'] = total_confired
df
import plotly.express as py
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x = df['Country'],y = df['Total Deaths']))
fig.add_trace(go.Scatter(x = df['Country'],y = df['Total Confirmed']))
fig.add_trace(go.Scatter(x = df['Country'],y = df['Total Recovered']))
py.line(df,x = 'Country',y = 'Total Deaths')
py.line(df,x = 'Country',y = 'Total Confirmed')
py.line(df,x = 'Country',y = 'Total Recovered')
sns.jointplot(df['Total Recovered'],df['Total Deaths'],kind = 'kde')
df1 = df[df['Total Deaths'] > 1000]
df1
sns.jointplot(df1['Total Confirmed'],df1['Total Deaths'],kind = 'kde')
df2 = df[df['Total Confirmed'] > 50000]
df2
sns.jointplot(df2['Total Confirmed'],df2['Total Deaths'],kind = 'kde')
