import numpy as np
# create array

arr = [[1,2,3], [4,5,6], [7,8,9]]

is_5 = arr[1][1]

print(is_5)

arr_3d = np.array([[[[[1,2,3,4,5,6,7,8,9,0]
   ]]
]])

is_5_in_np = arr_3d[0][0][0][0][9]
print(is_5_in_np)