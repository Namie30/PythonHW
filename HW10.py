 #Test
# def lamb(x,y):
#     return x+y
# print(lamb(4,5))
#
# lamb_lambs = lambda x, y: x + y
# print(lamb_lambs(10, 19))

#1
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

print(list(zip(my_list1, my_list2)))

#2
my_list = [1, 2, 3, 4, 5, 6, 7]

even_numbers = list(filter(lambda x: x % 2 == 0, my_list))

print(even_numbers)

#3
my_list = [1, -2, -3, 4, -5, 6, 7]

positive_numbers = list(filter(lambda x: x > 0, my_list))

print(positive_numbers)

#4
my_strings = ["madam", "hello", "racecar", "world", "level"]

palindromes = list(filter(lambda x: x == x[::-1], my_strings))

print(palindromes)

#5
from functools import reduce
def multiply_elements(numbers):
    return reduce(lambda x, y: x * y, numbers)

my_numbers = [1, 2, 3, 4, 5]
result = multiply_elements(my_numbers)
print(result)

