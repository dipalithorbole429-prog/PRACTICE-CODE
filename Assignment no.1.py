import numpy as np
print("---1,ARRAY CREATION")
# l1=[10,20,30,40,50,60]
# Creating 1D and 2D array
arr_1d=np.array([10,20,30,40,50,60])
arr_2d=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
])
print("1D ARRAY:",arr_1d)
print("2D ARRAY:",arr_2d)
print()
#print("__2.INDEXING__")
#Accessing individual elements
first_element=arr_1d[0]
last_element=arr_1d[-1]
element_2d=arr_1d[1,2] #Row index 1,column index 2(value:7)
print(f"First Element of 1D:{first_element}")
print(f"last Element of 1D:{last_element}")
print(f"Element at row 1,column 2 n 2D:{element_2d}")
print()
print("---3.SLICING---")
#Extracting sub-array [start:stop:step]
slice_1d=arr_1d[1:4:1]
sub_2d=arr_2d[0:2,1:3]
print("1D slice_[1:4]:",slice_1D)
print("2D sub-grid(rows 0-1,cols 1-2):\n


























