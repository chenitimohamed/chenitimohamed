#Numpy Tutorial 4
import numpy as np

#Copy

array = np.array([1,2,3,4,5])# One Dimension array!
copy  = array.copy()# Create a copy of the original array!
array[0] = 10 # this changes 1 to 10(change of element)
print(array)# this will print the array with element change
print(copy)# this will print the original array

#View
array2 = np.array([1,2,3,4,5])# One dimension array
view  = array2.view()# this will create a view of the original array
array2[0] = 10 # change 1 to 10(change element)
print(array2)# print the array with the change element
print(view)# print the array with the change element

#Python to recall weather it's a copy or a view

