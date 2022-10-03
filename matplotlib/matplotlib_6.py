import matplotlib.pyplot as plt

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

explode = [0.03,0,0.1,0,0] # To slice the perticuler section
colors = ["c", 'b','r','y','g'] # Color of each section
textprops = {"fontsize":15} # Font size of text in pie chart

plt.figure(figsize = (16,9))
wedgeprops = {"linewidth": 4, 'width':3, "edgecolor":"k"} # Width = 1
plt.pie(
        class1_students, 
        labels = classes, 
        explode = explode, 
        colors = colors, 
        autopct = "%0.2f%%", 
        pctdistance = 0.6, 
        shadow =True, 
        labeldistance = 1.6, 
        startangle = 270,
        radius = 1, 
        counterclock = True, 
        wedgeprops = wedgeprops,
        textprops = textprops,
        center=(2, 3),
        frame=True,
        rotatelabels=True
        ) 
plt.show()

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
plt.legend()
plt.show()

import numpy as np
plt.figure(figsize=(7,4))
#plt.figure(figsize=(16,9)
 
colors = ['r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w']
labels = np.ones(20)
#labels = [1.0,1.0,1.0,1.0,1.0,.........,1.0]
 
plt.pie([1], colors="k", radius = 2.05)
plt.pie(labels, colors=colors, radius = 2.0)
 
plt.pie([1], colors="g", radius = 1.8)
plt.pie([1], colors="y", radius = 1.6)
plt.pie([1], colors="c", radius = 1.3)
plt.pie([1], colors="b", radius = 1.1)
plt.pie([1], colors="m", radius = 0.9)
 
plt.pie([1], colors="b", radius = 0.31)
plt.pie(labels, colors=colors, radius = 0.3)
 
plt.pie([1], colors="w", radius = 0.2)
plt.pie([1], colors="k", radius = 0.1)
 
plt.show()