# #1
# def positive_check(func):
#     def checker(number):
#         if number < 0:
#             raise ValueError("The number must be positive.")
#         result = func(number)
#         print(result)
#         return result
#     return checker
#
# @positive_check
# def return_number(number):
#     return number
#
# #return_number(5)
# return_number(-3) #works just as it should

#2
# class PositiveCheck:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, number):
#         if number < 0:
#             raise ValueError("The number must be positive.")
#         result = self.func(number)
#         print(result)
#         return result
#
# @PositiveCheck
# def return_number(number):
#     return number
#
# return_number(5)
# return_number(-3)

#3
import time
def calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@calculator
def function():
    time.sleep(1)
    return "Function complete"

function()
#4

