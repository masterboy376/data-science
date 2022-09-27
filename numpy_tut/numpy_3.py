import numpy as np

matrix = np.arange(1,13) #array of 1 to 12
print(matrix)
matrix = np.arange(1,13,2) #array of 1 to 12 of odd number
print(matrix)
matrix = np.linspace(1,5,4) #array of 1 to 12 of odd number
print(matrix)

array = np.arange(1,13)
matrix_2d = array.reshape(3,4) #2d
print(matrix_2d)

array = np.arange(1,13)
matrix_3d = array.reshape(2,3,2) #3d
print(matrix_3d)

new_arr= matrix_2d.ravel()
print(new_arr)
new_arr= matrix_3d.flatten() # modifyable
print(new_arr)

trans_matrix_2d = matrix_2d.transpose()
print(trans_matrix_2d)
