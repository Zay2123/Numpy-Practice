import numpy as np 

# Problem 1 — Random Data
# Create a 5x5 matrix of random integers between 1 and 100.Then print: the matrix the shape

arr1 =np.array([np.random.randint(1,100,25)]).reshape(5,5)
print(arr1)
print(arr1.shape)

# Problem 2 — Find Values Using Boolean Masking 
# Using your random matrix from Problem 1: Print all values greater than 50. Print all values less than 25. Count how many values are greater than 70
plus50 = np.array([])
less25 = np.array([])
count75plus = 0
for i in np.nditer(arr1):
    if i > 50 and i > 70:
        plus50 = np.append(plus50, i)
        count75plus += 1
    elif i > 50:
        plus50 = np.append(plus50, i)
    elif i < 25:
       less25 = np.append(less25, i)
print("Here are all numbers in the array greater than 50", plus50)
print("Here are all numbers in the array less than 25", less25)
print("The amount of numbers in the array above 75 is" , count75plus)

# Problem 3 — Row & Column Statistics (Axis)
# Using the same matrix: Calculate and print:Sum of each row Sum of each column Mean of each row 
rowcount = 1
for i in range(0,5):
    print("The Sum of Row", rowcount,":", np.sum(arr1[i,:]))
    rowcount = rowcount + 1 
columncount = 1  
for i in range(0,5):
    print("The Sum of Column", columncount,":", np.sum(arr1[:,i]))
    columncount = columncount + 1
rowcount = 1
for i in range(0,5):
    print("The Mean of Row", rowcount,":", np.mean(arr1[i,:]))
    rowcount = rowcount + 1
    
# Problem 4 — Broadcasting
# Create: arr = np.arange(1,6) Add this array to each row of the matrix from Problem 1.
# Example idea: [1 2 3 4 5] gets added to every row automatically Print the result.
arr = np.arange(1,6)
for i in range(0,5):
    arr1[i,:] = (arr1[i,:]) + arr
print(arr1)

# Problem 5 — Matrix Math
# Create two 3x3 matrices of random integers (1–10). Perform and print: Matrix multiplication Element-wise multiplication, Transpose of one matrix
arr2 =np.array([np.random.randint(1,10,9)]).reshape(3,3)
print("Array2", arr2)
arr3 =np.array([np.random.randint(1,10,9)]).reshape(3,3)
print("Array3", arr3)
print("The Matrix Multiplication of Array2 and Array3 is:", np.matmul(arr2, arr3))
print("The Elementwise Multiplication of Array2 and Array3 is:", np.multiply(arr2, arr3))
print("The Transposed Matrix over Array2 is " , np.transpose(arr2))