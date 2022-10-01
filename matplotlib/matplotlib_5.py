import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# bar chart 
classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10] # out of 100 student in each class
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15]

plt.bar(classes, class1_students)
plt.show()

plt.barh(classes, class1_students)
plt.show()

plt.figure(figsize=(16,9))
style.use("ggplot") 
plt.bar(classes, class1_students, width = 0.2, align = "edge", color = "y", edgecolor = "k", linewidth = 1, alpha = 0.9, linestyle = "-", label =" Class 1 Students", visible=True)
plt.show()
plt.figure(figsize=(16,9))
plt.bar(classes, class1_students, width = 0.2, color = "k",label =" Class 1 Students") #visible=False
plt.bar(classes, class2_students, width = 0.2, color = "b",label =" Class 2 Students") 
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.xlabel("Classes",fontsize = 15)
plt.ylabel("No. of Students", fontsize = 15)
plt.show()

plt.figure(figsize=(16,9))
classes_index = np.arange(len(classes))
width = 0.2
plt.bar(classes_index, class1_students, width , color = "b", label =" Class 1 Students") #visible=False
plt.bar(classes_index + width, class2_students, width , color = "g", label =" Class 2 Students") 
plt.bar(classes_index + width + width, class3_students, width , color = "y",label =" Class 2 Students") 
plt.xticks(classes_index + width, classes, rotation = 20)
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.xlabel("Classes",fontsize = 15)
plt.ylabel("No. of Students", fontsize = 15)
plt.show()

plt.figure(figsize=(16,9))
classes_index = np.arange(len(classes))
width = 0.2
plt.barh(classes_index, class1_students, width , color = "b", label =" Class 1 Students") #visible=False
plt.barh(classes_index + width, class2_students, width , color = "g", label =" Class 2 Students") 
plt.barh(classes_index + width + width, class3_students, width , color = "y", label =" Class 3 Students") 
plt.yticks(classes_index + width, classes, rotation = 20)
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.ylabel("Classes",fontsize = 15)
plt.xlabel("No. of Students", fontsize = 15)
plt.legend()
plt.show()