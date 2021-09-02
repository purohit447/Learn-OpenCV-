# Numpy Fundamentals
# By Karan Purohit

# Whats Inside?

# 1. row vector (arr1)
# 2. column vector (arr2)
# 3. 2D vector (arr3)
# 4. 3D vector (arr4)
# 5. zero vector (arr5)
# 6. ones vector (arr6)
# 7. full vector (arr7)
# 8. identity vector (arr8)
# 9. arange vector (arr9)
# 10. linspace vector (arr10)
# 11. random vector (arr11)
# 12. random integer vector (arr12)
# 13. find shape of vector (arr13)
# 14. find size of vector (arr14)
# 15. find data-type of vector (arr15)
# 16. change data-type of vector (arr16)
# 17. elementary oprations on vector (arr17)
# 18. scaler oprations on vector (arr18)
# 18.1 find the minimum element of vector
# 18.2 find the maximum element of vector
# 19. access all elements of vector (arr19)
# 20. access all elements of a row/column  (arr20)
# 21. access elements between ranges (arr21)
# 22. reversing row wise the vector matrix (ar22)
# 23. reshape the vector matrix (arr23)
# 24. append the element in a vector matrix (arr24)
# 25. delete the element at particular index in a vector (arr25)
# 26. flaten any vector matrix (arr26)
# 27. concatenate any vector matries (arr27)
# 28. transpose any vector matrix (arr28) 
# 29. copy any vector matrix (arr29)



import numpy as np

arr1 = np.array([1,2,3,4])  # declaration of a row vector
print(arr1,"\n")   # output: [1 2 3 4] 


arr2 = np.array([[1],[2],[3]]) # declaration of column vector
print(arr2,"\n")   
# output: [[1]
#          [2]
#          [3]]


arr3 = np.array([(1,2,3),(4,5,6)]) # declaration of 2D vector
print(arr3,"\n") 
# output:  [[1 2 3]
#           [4 5 6]]


arr4 = np.array([[(1,2,3),(4,5,6)],[(1,2,3),(4,5,6)]]) # declaration of 3D vector
print(arr4,"\n") 
# output:  [[[1 2 3]
#            [4 5 6]]
#
#            [[1 2 3]
#            [4 5 6]]] 


arr5 = np.zeros((3,3), dtype="uint8") # declaration of zero vector of specific data-types //uint8 = usigned integer of 8 bits size
print(arr5,"\n")   
# output: [[0 0 0]
#          [0 0 0]
#          [0 0 0]]
  

arr6 = np.ones((3,5), dtype="int") # declaration of ones vector
print(arr6,"\n")  
# output: [[1 1 1 1 1]
#          [1 1 1 1 1]
#          [1 1 1 1 1]]
 

arr7 = np.full((3,5),5) # declaration of parameter's vector // i.e 5 here
print(arr7,"\n")  # output: [[5 5 5 5 5]
#                            [5 5 5 5 5]
#                            [5 5 5 5 5]] 
 

arr8 = np.eye(3, dtype="int") # declaration of Identity matrix 
print(arr8,"\n")  # output: [[1 0 0]
#                           [0 1 0]
#                           [0 0 1]] 


arr9 = np.arange(0,10,2) # declaration of vector with 2 in gaps between 0-9
print(arr9,"\n")  # output: [0 2 4 6 8] 


arr10 = np.linspace(0,2,9) # declaration of vector with 9 values between 0-2 inclusively
print(arr10,"\n")  # output:  [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ] 


arr11 = np.random.rand(2,3)*255 # declaration of random vactor between 0-1 without scaler multiplication //255 multipliend here
print(arr11,"\n")  
# output: [[ 17.68858346 115.54634764 216.55541234]
#          [212.37821281 202.55367052 226.99675923]]


arr12 = np.random.randint(5, size=(3,3)) # declaration of random integer vector of size(x,y) between 0-4 
print(arr12,"\n")
# output: [[2 3 0]
#          [4 1 0]
#          [4 0 1]]


arr13 = np.array([(1,2,3),(4,5,6)])
print(arr13.shape,"\n") # finds the dimentions of the vector
# output: (2, 3)


arr14 = np.array([(1,2,3),(4,5,6)])
print(arr14.size,"\n") # finds the size of vector
# output: (6)


arr15 = np.array([(1,2,3),(4,5,6)])
print(arr15.dtype,"\n") # finds out the data type of the vector
# output: int32


arr16 = arr15.astype(float) # changes the data type of a vector
print(arr16.dtype,"\n")  # output:  float64


arr17 = arr15+arr16 # elementry opprations can be done directly like add,subtract,multiply,division
print(arr17,"\n")  
# output:  [[ 2.  4.  6.]
#           [ 8. 10. 12.]]  


arr18 = arr17+20 # scaler oppration can also be performed
print(arr18,"\n") 
# output:  [[22. 24. 26.]
#           [28. 30. 32.]] 


print(arr18.min(),"\n") # finds the minimum element
# output: 22.0


print(arr18.max(),"\n") # finds the maximum element 
# output: 32.0


arr19 = np.array([(1,2,3),(4,5,6)]) 
print(arr19[:,:],"\n")  # ":" gives the all elements in the the matrix
# output: [[1 2 3]
#          [4 5 6]] 


arr20 = np.array([(1,2,3),(4,5,6)])
print(arr20[1,:],"\n") # ":" if used in row or column gives all the elments of particular row or column  
# output:   [4 5 6]  


arr21 = np.array([(1,2,3),(4,5,6)])
print(arr21[0,1:3],"\n") # it gives elemnts between the given range(x,y-1) in particular row or column 
# output: [2,3]


arr22 = np.array([(10,9,8,7),(6,5,4,3),(2,1,0,-1)])
print(arr22[::-1],"\n") # reversing the array row wise
# output:  [[ 2  1  0 -1]
#           [ 6  5  4  3]
#           [10  9  8  7]]


arr23 = np.array([(10,9,8,7),(6,5,4,3),(2,1,0,-1)])
arr23 = arr23.reshape(1,12)  # it reshapes the array but remember the no. of elements must be supporting the new given shape to avoid errors 
print(arr23,"\n")   # output: [[10  9  8  7  6  5  4  3  2  1  0 -1]] 


arr24 = np.array([(1,2,3,4,5,6)])
arr24 = np.append(arr24,7)  # it appends the particular element in the array
print(arr24,"\n")  # output: [1 2 3 4 5 6 7] 


arr25 = np.array([(1,2,3,4,5,6)])
arr25 = np.delete(arr25,0)  # it deletes the particular element at given index in the array
print(arr25,"\n")  # output: [2 3 4 5 6] 


arr26 = np.array([(1,2,3),(4,5,6)])
arr26 = arr26.ravel()  # it only flatens any array given to it making it an row vector
print(arr26,"\n")  # output:  [1 2 3 4 5 6] 

arrx = np.array([1,2,3,4]) 
arry = np.array([5,6,7])
arr27 = np.concatenate((arrx,arry)) # it concatenates both the arrays 
print(arr27,"\n")  # output: [1 2 3 4 5 6 7] 

arr28 = np.array([(1,2,3,4,5),(6,7,8,9,0)])
arr28 = np.transpose(arr28) # it transpose the arrays 
print(arr28,"\n") 
# output:  [[1 6]
#           [2 7]
#           [3 8]
#           [4 9]
#           [5 0]] 


arr29 = np.copy(arr28)  # it copies the array 
print(arr29)
# output:  [[1 6]
#           [2 7]
#           [3 8]
#           [4 9]
#           [5 0]] 
