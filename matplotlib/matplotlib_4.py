import matplotlib.pyplot as plt # For visualization
import pandas as pd # for data cleaing & analysis


# Dataset taken from kaggel.com
df_google_play_store_apps = pd.read_csv("D:\\Private\Indina AI Production\Kaggel Dataset\google-play-store-apps\googleplaystore.csv")
print(df_google_play_store_apps.shape) # Get shape of dataset in rows and colms

df_google_play_store_apps = pd.read_csv("D:\\Private\Indina AI Production\Kaggel Dataset\google-play-store-apps\googleplaystore.csv", nrows = 1000)
print(df_google_play_store_apps.shape) ## Get shape of dataset in rows and colms


x = df_google_play_store_apps["Rating"]
y = df_google_play_store_apps["Reviews"]


plt.scatter(x,y) # Draw scatter plot with parameter x and y
plt.show()


plt.scatter(x,y)
plt.title("Google Play Store Apps Scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


plt.figure(figsize = (16,9)) # figure size ratio 16:9
plt.scatter(x,y, c = "r", marker = "*", s = 100, alpha=0.5, linewidths=10, edgecolors="g" )#verts="<"
plt.title("Google Play Store Apps Scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = "r", marker = "*", s = 100, alpha=0.5, linewidths=10,edgecolors="g" )#verts="<"
plt.scatter(x,df_google_play_store_apps["Installs"], c = "y", marker = "o", s = 100, alpha=0.5, linewidths=10, edgecolors="c" )
plt.title("Google Play Store Apps Scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews & Installs")
plt.show()