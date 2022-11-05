
# import piplite
# await piplite.install('seaborn')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset
dt=pd.read_csv("./budget.csv")
dt.shape


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


dt.head(10)


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


dt.select_dtypes(include=['int64', 'float64']).columns


drop_columns==dt.select_dtypes(include=['int64', 'float64']).columns


int_col = dt.select_dtypes(include=['int64', 'float64']).columns
int_col


int_data = dt.select_dtypes(include=['int64', 'float64'])
int_data


sns.heatmap(int_data.isnull())
plt.show()


missing_int_var= [var for var in int_data.columns if int_data[var].isnull().sum()>0]
missing_int_var


for i,var in enumerate(missing_int_var):
    plt.subplot(15,4,i+1)
    sns.distplot(dt[var], bins=20)
    
plt.show()


# symmetric curve: any of mean, median, mode
# asymmetric curve: median


filled_dt_mean=dt.fillna(dt.mean()) #mean
filled_dt_mean.isnull().sum()


for i,var in enumerate(missing_int_var):
    plt.subplot(15,4,i+1)
    sns.distplot(dt[var], bins=20)
    sns.distplot(filled_dt_mean[var], bins=20)
    
plt.show()


filled_dt_median=dt.fillna(dt.median()) #mean
filled_dt_median.isnull().sum()


for i,var in enumerate(missing_int_var):
    plt.subplot(15,4,i+1)
    sns.distplot(dt[var], bins=20)
    sns.distplot(filled_dt_median[var], bins=20)
    
plt.show()


plt.figure(figsize=(25,25))
for i,var in enumerate(missing_int_var):
    plt.subplot(60,1,i+1)
    sns.boxplot(dt[var])
    sns.boxplot(filled_dt_median[var])
    
plt.show()


dt_concat = pd.concat([
    dt[missing_int_var],
    filled_dt_median[missing_int_var],
    filled_dt_mean[missing_int_var]
], axis=1, keys=['dirty', 'clean_median', 'clean_mean'])


dt_concat[dt_concat.isnull().any(axis=1)]





