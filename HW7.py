# #1
# squared_numbers = {x**2 for x in range(1, 11)}
#
# print(squared_numbers)
#
# #2
# S = input("Please input a string: ")
#
# char_set = set()
#
# for char in S:
#     char_set.add(char)
#
# print(char_set)
from enum import unique

#3
# tuple1 = (1,2,3,4,5,6)
#
# tuple2 = (4,5,5,6,6,7)
#
# unique_values = tuple(set(tuple1 + tuple2))
#
# print(f"Unique values are:  {unique_values}")
#
# duplicated_values = []
#
# combined_tuple = tuple1 + tuple2
# for value in unique_values:
#
#     if combined_tuple.count(value) > 1:
#         duplicated_values.append(value)
#
# print("Duplicated values:", duplicated_values)

# #4
#
# input_tuple = (1, 2, 3, 4, 6, 8, 9)
#
#
# if len(input_tuple) > 1:
#     swapped_tuple = (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)
#
#
# print("Input tuple:", input_tuple)
# print("Swapped tuple:", swapped_tuple)

#6

set1 = {1, 2}
set2 = {'a', 'b'}

result = {(a, b) for a in set1 for b in set2}

print(result)
