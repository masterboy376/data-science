import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns

# seaborn line plot 

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
 
#create dataframe using two list days and temperature
temp_df = pd.DataFrame({"days":days, "temperature":temperature})
 
# Draw line plot
sns.lineplot(x = "days", y = "temperature", data=temp_df,)
plt.show() # to show graph

#load tips dataset from GitHub
tips_df = sns.load_dataset("tips")
print(tips_df) # call tips DataFrame

print(tips_df.shape) # get shape of dataseat tips

#Draw line plot of total_bill and tip
sns.lineplot(x = "total_bill", y = "tip", data = tips_df)

#Draw line plot of tip and total_bill
sns.lineplot(x = "tip", y = "total_bill", data = tips_df)

#Draw line plot of tip and size
sns.lineplot(x = "tip", y = "size", data = tips_df)

#Draw line plot of size and total_bill
sns.lineplot(x = "size", y = "total_bill", data = tips_df)

# Draw line plot of size and total_bill with parameters
sns.lineplot(x = "size", y = "total_bill", data = tips_df, hue = "sex",
            style = "sex", palette = "hot", dashes = False, 
            markers = ["o", "<"],  legend="brief",)
 
plt.title("Line Plot", fontsize = 20) # for title
plt.xlabel("Size", fontsize = 15) # label for x-axis
plt.ylabel("Total Bill", fontsize = 15) # label for y-axis
plt.show()

plt.figure(figsize = (16,9)) # figure size with ratio 16:9
sns.set(style='darkgrid',) # background darkgrid style of graph 
 
# Draw line plot of size and total_bill with parameters
sns.lineplot(x = "size", y = "total_bill", data = tips_df, hue = "sex",
            style = "sex", palette = "hot", dashes = False, 
            markers = ["o", "<"],  legend="brief",)
 
plt.title("Line Plot", fontsize = 20)
plt.xlabel("Size", fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()

plt.figure(figsize = (16,9))
sns.set(style='darkgrid',)
 
# Draw line plot of size and total_bill with parameters and hue "day"
sns.lineplot(x = "size", y = "total_bill", data = tips_df, hue = "day",
            style = "day", palette = "hot", dashes = False, 
            markers = ["o", "<", ">", "^"],  legend="brief",)
 
plt.title("Line Plot", fontsize = 20)
plt.xlabel("Size", fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()
