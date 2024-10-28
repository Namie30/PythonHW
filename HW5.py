#1
"""
mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

x = mylist[2] + mylist[8] + mylist[13]
print(x)
"""

#2
"""
import random

first_list = [random.randint(1, 100) for _ in range(20)]
second_list = []

for x in first_list:
    if x % 2 != 0:
        second_list.append(x)

min_value = second_list[0]
max_value = second_list[0]

for y in second_list:
    if y < min_value: 
        min_value = y
    if y > max_value:
        max_value = y 

print(first_list)
print(second_list)
print(f"MIN Value is: {min_value}, while MAX value is: {max_value}")
"""

#3
"""
my_list = [43, '22', 12, 66, 210, ["hi"]]

#a 
print(my_list.index(210))

#b
my_list.append('hello')

#c
my_list.pop(2)
print(my_list)

#d
my_list2 = my_list.copy()
my_list2.clear()

print(my_list)
print(my_list2) ##togotc vxedavt carielia
"""
#N4
"""
matrix1 = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 1]
]
matrix2 = [
   [11, 22, 33],
   [4, 5, 6],
   [77, 88, 11]
]

result = []

for i in range(len(matrix1)):
    row = []

    for j in range(len(matrix2[0])):
        row.append(matrix1[i][j] + matrix2[i][j])

    result.append(row)

for row in result:
    print(row)

"""
#N5
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transpose = [[0, 0, 0] for _ in range(3)]  

for i in range(3): 
    for j in range(3): 
        transpose[j][i] = matrix[i][j] 

print("Transposed Matrix:")
for row in transpose:
    print(row)
"""

#N6
import random

matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

for row in matrix:
    print(row)