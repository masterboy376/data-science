import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from matplotlib import style

plt.subplot(2,2,1)

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp = [33,34,32,32,38,39,39,34,33,32,31,37,33,37,39]
mumbai_temp = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
style.use("ggplot")
plt.plot(days, delhi_temp, "bo--", label="Delhi")
plt.plot(days, mumbai_temp, "ro--", label="Mumbai")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.legend(loc=2)
plt.grid(color='k', linestyle='-', linewidth=1)
 
plt.subplot(2,2,2)
 
ml_student_age = np.random.randint(18, 45, (100))
py_student_age = np.random.randint(15, 40, (100)) 
style.use("ggplot")
bins = [15,20,25,30,35,40,45]
plt.figure(figsize=(16,9))
plt.hist([ml_student_age, py_student_age], bins, rwidth=0.8, histtype="bar", orientation= "vertical", color=["b","r"], label=["ML students", "PY students"])
# plt.hist(py_student_age, bins, rwidth=0.8, histtype="bar", orientation= "vertical", color="b", label="PY students")
plt.title("ML students age")
plt.xlabel("student age category")
plt.ylabel("no. student age")
plt.legend()

plt.subplot(2,2,3)
 
classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10] # out of 100 student in each class
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15] 
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

plt.subplot(2,2,4)

classes = ['Python', 'Java', 'JavaScript', 'C++', 'Rust']
class1_students = [30,5,35,25,5]
explode = [0.05, 0 , 0, 0.03, 0]
colors = ["c", 'b','r','y','g']
textprops = {"fontsize":15}

plt.pie(class1_students,
        labels = classes,
       explode = explode,
       colors = colors,
       textprops = textprops,
       autopct = "%0.2f%%",
       shadow = True,
       radius = 1.4,
       startangle = 270)
 
plt.show()