import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer

df = pd.read_csv('C:/Users/Anuska Sarkar/Downloads/archive/covid_19_data.csv')
print(df.head(50))
df.drop(['SNo','Last Update'],axis = 1, inplace = True)
df.rename(columns = {'ObservationDate': 'Date','Province/State': 'State','Country/Region': 'Country'},inplace = True)
df['Date'] = pd.to_datetime(df['Date'])

imputer = SimpleImputer(strategy = 'constant')
df2 = pd.DataFrame(imputer.fit_transform(df),columns = df.columns)

df3 = df2.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum().reset_index()

print(df3.head(20))

countries = df3['Country'].unique()
print(len(countries))

for index in range(0,len(countries)):
    C = df3[df3['Country']==countries[index]].reset_index()
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color = 'blue',label = 'Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color = 'green',label = 'Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color = 'red',label = 'Deaths')
    plt.title(countries[index])
    plt.xlabel('Days since the First Suspect')
    plt.ylabel('Numberof Cases')
    plt.legend()
    plt.show()

df4 = df3.groupby(['Date'])[['Date','Confirmed','Deaths','Recovered']].sum().reset_index()

C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color = 'blue',label = 'Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color = 'green',label = 'Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color = 'red',label = 'Deaths')
plt.title('World')
plt.xlabel('Days since the First Suspect')
plt.ylabel('Numberof Cases')
plt.legend()
plt.show()