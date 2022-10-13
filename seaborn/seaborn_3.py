import seaborn as sns # for data visualization
import numpy as np # for numeric computing
import matplotlib.pyplot as plt # for data visualization

# bar plot

tips_df = sns.load_dataset("tips")
print(tips_df)

sns.barplot()

sns.barplot(x = tips_df.day, y = tips_df.total_bill)

sns.barplot(x = tips_df.day, y = tips_df.total_bill, hue = tips_df.sex)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df)

order = ['Sun', 'Thur', 'Fri', 'Sat']
 
sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df, order = order)

hue_order = ['Female', 'Male']
 
sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df, hue_order = hue_order)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df,  n_boot=2)

sns.barplot(x ='total_bill', y = 'size', hue = 'sex', data = tips_df,orient='h')

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',data = tips_df, color="g")

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df, palette="magma")

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df, saturation=.3)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df, errcolor='0.5')

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',data = tips_df, errwidth= 12)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',data = tips_df, capsize=1)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',data = tips_df, dodge= False)

kwargs = {'alpha':0.9, 'linestyle':':', 'linewidth':5, 'edgecolor':'k'}
sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',data = tips_df,**kwargs)


sns.set() # for darkgrid background
sns.barplot(x = 'day', y = 'total_bill', data = tips_df, alpha =.9, linestyle = "-.", linewidth = 3,edgecolor = "g")

sns.set()
ax = sns.barplot(x = 'day', y = 'total_bill', data = tips_df, alpha =.9, linestyle = "-.", linewidth = 3,edgecolor = "g")
ax.set(title = "Barplot of Tips DataFrame",xlabel = "Days",ylabel = "Total Bill")

sns.set()
plt.figure(figsize = (16,9))
sns.barplot(x = 'day', y = 'total_bill', data = tips_df, alpha =1, linestyle = "-.", linewidth = 3,edgecolor = "k")
plt.title("Barplot of Days and Total Bill", fontsize = 20)
plt.xlabel("Days", fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.savefig("Barplot of Days and Total Bill")
plt.show()