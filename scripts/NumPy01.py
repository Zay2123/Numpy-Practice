import numpy as np
# Problem 1- Create a NumPy array containing Numbers 1-10. Print the shape, data type, and Number of dimentions
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1.shape)
print(array1.dtype)
print(array1.ndim)
# Problem 2- Create an array of number 1-12, reshape it into a 3x4 matrix, print matrix
array2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array2re = np.reshape(array2, (3,4))
print(array2re)
# Problem 3- Create an array of number 1-16, reshape it into a 4x4 matrix Extract and Print: The First Row, The last Column and 2x2 center square
array3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
array3re = np.reshape(array3, (4,4))
print(array3re[0,:])
print(array3re[:,-1])
print(array3re[1:3,1:3])
# Problem 4- Using arr= np.array([2,4,6,8,10]) without  loops: Multiply all values by 3 and 5 to all values, and square every value Print results
array4= np.array([2,4,6,8,10])
print(array4 * 3)
print(array4 + 5)
print(array4 ** 2)
# Problem 5- data= np.array([23,45,12,67,34,89,21,55]) Calculate and Print the Mean, Median, SD, Min, and Max
data= np.array([23,45,12,67,34,89,21,55])
Mean = np.mean(data)
Median = np.median(data)
SD = np.std(data)
Minimum = np.min(data)
Maximum = np.max(data)
print(Mean)
print(Median)
print(SD)
print(Minimum)
print(Maximum)