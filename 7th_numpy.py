#Numpy Tutorial 6- Handy operation for data analytics

import numpy as np

#Operation that comes in handy for data analysis!
one_dim = np.array([0, 1, 2, 3, 4, 5]) # [ 1 2 3 4 5 ]
two_dim = np.array([[1,2,3],[4,5,6]])  # [[ 1 2 3][4 5 6]]

#Summation
print(sum(sum(two_dim)))

