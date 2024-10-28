#1
"""
int_list = [10, 20, 30, 40]

def add_to_list(number):
    global int_list
    int_list.append(number)

add_to_list(50)
print(int_list)
"""

#2
"""
def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

ans = sum_of_digits(12345)
print(ans)  
"""
#3
"""
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

ans = reverse_string("Hello")
print(ans)  
"""
#4
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(15):
    print(fib(i), end=" ")