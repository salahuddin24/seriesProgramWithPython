# matrix is two dymantional list
from pickletools import markobject

matrix = [
    [1, 3, 5],
    [2, 4, 6]
]
print(matrix[0][2]) # 0 number index col ar 2 number index ar row => 5
matrix[0][2] = 12 # change the value
for row in matrix :
    for col in row :
        print(col)