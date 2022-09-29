import matplotlib.pyplot as plt
import numpy as np
import random

# histogram
ml_student_age = np.random.randint(18, 45, (100))
py_student_age = np.random.randint(15, 40, (100))
print(ml_student_age)
print(py_student_age)

from matplotlib import style
style.use("ggplot")
bins = [15,20,25,30,35,40,45]
plt.figure(figsize=(16,9))
plt.hist([ml_student_age, py_student_age], bins, rwidth=0.8, histtype="bar", orientation= "vertical", color=["b","r"], label=["ML students", "PY students"])
# plt.hist(py_student_age, bins, rwidth=0.8, histtype="bar", orientation= "vertical", color="b", label="PY students")
plt.title("ML students age")
plt.xlabel("student age category")
plt.ylabel("no. student age")
plt.legend()
plt.show()