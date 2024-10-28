# #1
# s = input('Please input your sentence: ')
#
# word_count = {}
#
# for word in s.lower().split():
#     word_count[word] = word_count.get(word, 0) + 1
#
# print(word_count)

# 2
# number1 = float(input('Please input your first number: '))
# number2 = float(input('Please input your second number: '))
# operator = input('Please input your operator(-, +, *, /): ')
#
# math_dict = {
#     '+': number1 + number2,
#     '-': number1 - number2,
#     '*': number1 * number2,
#     '/': number1 / number2 if number2 != 0 else "Cannot divide by zero"
# }
#
# print(math_dict.get(operator, 'Please Enter Operators (+, -, *, /)'))


#3
# something_dict = {num: num**2 for num in range(1,11)}
#
# print(something_dict)

#4

company = {
    'Department': {
        'HR': {
            'Employees': {
                '1001': {'Name': 'Giorgi', 'Lastname': 'Giorgadze', 'Age': 24, "Salary": 4500},
                '1002': {'Name': 'Khatia', 'Lastname': 'Kvaracxelia', 'Age': 34, "Salary": 5500}
            }
        },
        'Marketing': {
            'Employees': {
                '1001': {'Name': 'Giorgi', 'Lastname': 'Burduli', 'Age': 24, 'Salary': 4500},
                '1002': {'Name': 'Khatia', 'Lastname': 'Sivsivadze', 'Age': 34, 'Salary': 5500},
                '1003': {'Name': 'Tamar', 'Lastname': 'Javakhishvili', 'Age': 28, 'Salary': 5000},
                '1004': {'Name': 'Nika', 'Lastname': 'Zedginidze', 'Age': 30, 'Salary': 6000},
                '1005': {'Name': 'Maka', 'Lastname': 'Burchuladze', 'Age': 29, 'Salary': 4800},
            }
        }
    }
}

Average_salary = 0
Employee_count = 0

for department in company['Department'].values():
    for employee in department['Employees'].values():
        Average_salary += employee['Salary']
        Employee_count += 1

if Employee_count > 0:
    Average_salary = Average_salary / Employee_count
else:
    print('There are no employees')

print(Average_salary)






# product = {
#     'Technology': {
#       'Laptops': {
#           '1001': {'brand': 'Apple', 'price': 4000, 'quantity': 4},
#           '1002': {'brand': 'HP', 'price': 2000, 'quantity': 9},
#       },
#       'Phones': {
#           '2001': {'brand': 'Apple', 'price': 5000, 'quantity': 7},
#           '2002': {'brand': 'Samsung', 'price': 4500, 'quantity': 8},
#       },
#     },
#     'Cloth': {
#         'Pants': {
#             '3001': {'brand': 'Levis', 'price': 250, 'quantity': 4},
#             '3002': {'brand': 'Lee', 'price': 200, 'quantity': 9},
#         },
#         'Shirts': {
#             '4001': {'brand': 'Adidas', 'price': 150, 'quantity': 4},
#             '4002': {'brand': 'Nike', 'price': 175, 'quantity': 9},
#         },
#     }
#
# }