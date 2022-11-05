# import piplite
# await piplite.install('seaborn')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
dt=pd.read_csv("./budget.csv")

dt.shape

dt.head(10)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


dt


dt.info()


dt.isnull().sum()


dt.isnull()


plt.figure(figsize=(25,25))
sns.heatmap(dt.isnull())
plt.show()


null_var = dt.isnull().sum()/dt.shape[0] * 100
null_var


drop_columns=null_var[null_var>20].keys()
drop_columns


dt2 = dt.drop(columns = drop_columns)
dt2


sns.heatmap(dt2.isnull())
plt.show()


dt3= dt.dropna()
dt3


sns.heatmap(dt3.isnull())
plt.show()


dt3.isnull().sum()


dt3.select_dtypes(include=['int64', 'float64']).columns


sns.displot(dt['1960'])
plt.show()


sns.displot(dt3['1960'])
plt.show()


sns.distplot(dt['1960'])
sns.distplot(dt3['1960'])
plt.show()


feature_list = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018']
plt.figure(figsize=(25,25))
for i,var in enumerate(feature_list):
    plt.subplot(15,4,i+1)
    sns.distplot(dt[var], bins=20)
    sns.distplot(dt3[var],bins=20)
    
plt.show()


dt3.select_dtypes(include=['object']).columns


pd.concat([dt['Code'].value_counts()/dt.shape[0] * 100,
         dt3['Code'].value_counts()/dt3.shape[0] * 100], axis=1, keys=['dirty', 'clean'])


cate_feature_list=['Name', 'Code', 'Type', 'Indicator Name']


def cate_feature_dist(var):
    return pd.concat([dt[var].value_counts()/dt.shape[0] * 100,
         dt3[var].value_counts()/dt3.shape[0] * 100], axis=1, keys=['dirty', 'clean'])


for i,var in enumerate(cate_feature_list):
    print(cate_feature_dist(var))





