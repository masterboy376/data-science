# Import libraries
import seaborn as sns  # For Data Visualization
from scipy.stats import norm  # for scientific Computing
import matplotlib.pyplot as plt  # For Data Visualization

# histogram

# Load "tips" DataFrame from GitHub seaborn repository
tips_df = sns.load_dataset("tips")
tips_df

# Plot Histogram of "size"
sns.distplot(tips_df["size"])

# Plot Histogram of "tip"
sns.distplot(tips_df["tip"])

# Plot Histogram of "total_bill"
sns.distplot(tips_df["total_bill"])

# Plot Histogram of "total_bill" with bins parameters
sns.distplot(tips_df["total_bill"], bins=55)

# Plot Histogram of "total_bill" with hist parameters
sns.distplot(tips_df["total_bill"], hist=False)

# Plot Histogram of "total_bill" with kde (kernal density estimator) parameters
sns.distplot(tips_df["total_bill"], kde=False,)

# Plot Histogram of "total_bill" with rugplot parameters
sns.distplot(tips_df["total_bill"], rug=True,)

# Plot Histogram of "total_bill" with fit and kde parameters
# for fit (prm) -  from scipi.stats import norm
sns.distplot(tips_df["total_bill"], fit=norm, kde=False)

# Plot Histogram of "total_bill" with color parameters
sns.distplot(tips_df["total_bill"], color="r",)  # pass red color

# Plot Histogram of "total_bill" with vertical parameters
sns.distplot(tips_df["total_bill"], vertical=True,)  # Horizontal hist

# Plot Histogram of "total_bill" with norm_hist parameters
sns.distplot(tips_df["total_bill"], norm_hist=True,)

# Plot Histogram of "total_bill" with axlabel parameters
sns.distplot(tips_df["total_bill"], axlabel="Total Bill",)

# Plot Histogram of "total_bill" with label parameters
sns.distplot(tips_df["total_bill"], label="Total Bill",)
plt.title("Histogram of Total Bill")  # for histogram title
plt.legend()  # for label

# Plot histogram in prper format
plt.figure(figsize=(16, 9))  # figure ration 16:9
sns.set()  # for style
sns.distplot(tips_df["total_bill"], label="Total Bill",)
plt.title("Histogram of Total Bill")  # for histogram title
plt.legend()  # for label

tips_df.total_bill.sort_values()

# Modify histogram with bins
bins = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  # list
plt.figure(figsize=(16, 9))
sns.set()
sns.distplot(tips_df["total_bill"], bins=bins)
plt.xticks(bins)  # set bins value
plt.title("Histogram of Total Bill")
plt.show()

plt.figure(figsize=(16, 9))
sns.set()
# hist keyword argument to change hist format
sns.distplot(tips_df["total_bill"],
             hist_kws={'color': '#DC143C', 'edgecolor': '#aaff00',
                       'linewidth': 5, 'linestyle': '--', 'alpha': 0.9})  # hist keyword parameter to change hist format

plt.figure(figsize=(16,9))
sns.set()
# hist, kde and rug keyword  argument to change hist format
sns.distplot(tips_df["total_bill"],
            hist_kws = {'color':'#DC143C', 'edgecolor':'#aaff00',
                       'linewidth':5, 'linestyle':'--', 'alpha':0.9},
             
            kde_kws = {'color':'#8e00ce', 
                       'linewidth':8, 'linestyle':'--', 'alpha':0.9},
)

plt.figure(figsize=(16,9))
sns.set()
# hist, kde and rug keyword  argument to change hist format
sns.distplot(tips_df["total_bill"],
            hist_kws = {'color':'#DC143C', 'edgecolor':'#aaff00',
                       'linewidth':5, 'linestyle':'--', 'alpha':0.9},
             
            kde_kws = {'color':'#8e00ce', 
                       'linewidth':8, 'linestyle':'--', 'alpha':0.9},
            rug = True,
            rug_kws = {'color':'#0426d0', 'edgecolor':'#00dbff',
                       'linewidth':3, 'linestyle':'--', 'alpha':0.9},)

plt.figure(figsize=(16,9))
sns.set()
 
# hist, fit and rug keyword  argument to change hist format
sns.distplot(tips_df["total_bill"],
            hist_kws = {'color':'#DC143C', 'edgecolor':'#aaff00',
                       'linewidth':5, 'linestyle':'--', 'alpha':0.9},
             
            kde=False,
            fit = norm,
            fit_kws = {'color':'#8e00ce', 
                       'linewidth':12, 'linestyle':'--', 'alpha':0.4},
            rug = True,
            rug_kws = {'color':'#0426d0', 'edgecolor':'#00dbff',
                       'linewidth':5, 'linestyle':'--', 'alpha':0.9},)

# Plot histogram in best format
plt.figure(figsize=(16,9))
sns.set() 
bins = [1,5,10,15,20,25,30,35,40,45,50,55]
sns.distplot(tips_df["total_bill"],bins=bins,
            hist_kws = {'color':'#DC143C', 'edgecolor':'#aaff00',
                       'linewidth':5, 'linestyle':'--', 'alpha':0.9},
             
            kde=False,
            fit = norm,
            fit_kws = {'color':'#8e00ce', 
                       'linewidth':12, 'linestyle':'--', 'alpha':0.4},
            rug = True,
            rug_kws = {'color':'#0426d0', 'edgecolor':'#00dbff',
                       'linewidth':3, 'linestyle':'--', 'alpha':0.9},
            label = "TB") 
plt.xticks(bins)
plt.title("Histogram of Restorant Total Bill", fontsize = 20)
plt.xlabel("Total Bill", fontsize = 15)
plt.legend()
plt.show()

# Plot multiple seaborn histogram in single graph
plt.figure(figsize=(16,9))
sns.distplot(tips_df["total_bill"], bins=9, label="total_bil")
sns.distplot(tips_df["tip"], bins=9, label="tip")
sns.distplot(tips_df["size"], bins=9, label = "size")
plt.legend()