import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from matplotlib import style

plt.figure(figsize=(23,27))
 
##----------------------------------------start 
#plt.subplot(3,2,1)
plt.subplot(321)
#********************************************Line Plot
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_tem = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_tem = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]
 
plt.plot(days, delhi_tem, "mo--", linewidth = 3,
        markersize = 10, label = "Delhi tem")
 
plt.plot(days, mumbai_tem, "yo:", linewidth = 3,
        markersize = 10, label = "Mumbai tem}")
 
plt.title("Delhi  & Mumbai Temperature Line Plot", fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc = 4)
plt.grid(color='w', linestyle='-', linewidth=2)
 
#---------------------------------------------------------------end
 
plt.subplot(3,2,2) ##-------------------------------------------------start
#****************************************************************histograms
ml_students_age = np.random.randint(18,45, (100))
py_students_age = np.random.randint(15,40, (100))
bins = [15,20,25,30,35,40,45]
 
plt.hist([ml_students_age, py_students_age], bins, rwidth=0.8, histtype = "bar",
         orientation='vertical', color = ["m", "y"], label = ["ML Student", "Py Student"])
 
plt.title("ML & Py Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.legend()
#----------------------------------------------------------------------end
 
plt.subplot(3,2,3) ##--------------------------------------------start
#************************************************************Bar Chart
classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10] # out of 100 student in each class
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15]
classes_index = np.arange(len(classes))
 
width = 0.2
 
plt.barh(classes_index, class1_students, width , color = "b",
        label =" Class 1 Students") #visible=False
 
plt.barh(classes_index + width, class2_students, width , color = "g",
        label =" Class 2 Students") 
 
plt.barh(classes_index + width + width, class3_students, width , color = "y",
        label =" Class 3 Students") 
 
plt.yticks(classes_index + width, classes, rotation = 20)
plt.title("Bar Chart of IAIP Class Bar Chart", fontsize = 18)
plt.ylabel("Classes",fontsize = 15)
plt.xlabel("No. of Students", fontsize = 15)
plt.legend()
#--------------------------------------------------------------------end
 
plt.subplot(3,2,4) ##------------------------------------------------start
#**************************************************************Scatter Plot
x = [34,5,4,2,4,32,5,6,5,4,6,35,25,346,6,5,34,2,434,3]
y = [34,5,4,2,4,32,5,6,5,4,6,35,25,346,6,5,34,2,434,3]

plt.scatter(x,y, c = "r", marker = "*", s = 100, alpha=0.5, linewidths=10,
           edgecolors="g" )#verts="<"
 
plt.scatter(x,[34,5,4,2,4,32,5,6,5,4,6,35,25,346,6,5,34,2,434,3], c = "y", marker = "o", s = 100, alpha=0.5, linewidths=10,
           edgecolors="c" )
plt.title("Google Play Store Apps Scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews & Installs")
#----------------------------------------------------------------------end
 
 
plt.subplot(3,2,5) ##-----------------------------------------start
#*************************************************************Pie plot
classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece']
class1_students = [45, 15, 35, 25, 30]
explode = [0.03,0,0.1,0,0]
colors = ["c", 'b','r','y','g']
textprops = {"fontsize":15}
 
plt.pie(class1_students, 
        labels = classes, 
        explode = explode, 
        colors =colors, 
        autopct = "%0.2f%%", 
        shadow = True, 
        radius = 1.4,
       startangle = 270, 
        textprops =textprops)
#------------------------------------------------------end
 
 
plt.subplot(3,2,6, projection='polar', facecolor='k' ,frameon=True)
 
plt.savefig("./subplot_figure.png") # save subplots at drive "D" of name subplot_figure
plt.show()