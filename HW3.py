# N1
"""
number = int(input('Reverse count, insert the Number: '))

while number > 0:
    print(number)
    number -= 1
"""

# N2
"""
total_sum = 0

while True:
    user_input = input('Please input a number or write sum to sum it all: ')

    if user_input == 'sum':
        print(total_sum)
        break
    if user_input:
        number = int(user_input)
        if number > 0:
            total_sum += number
    else:
         print("Please enter a valid positive number or type 'sum'.")
"""
# N3

import random

print('Welcome to the Number Guessing Simulator! Try to guess the number. You have 5 chances.')
number = random.randint(1, 100)
guess = None
counter = 5

while counter > 0:
    guess = int(input('Guess the number: '))
    if guess > number:
        counter -= 1
        print(f'Try something lower. You have {counter} attempts left.')
    elif guess < number:
        counter -= 1
        print(f'Try something higher. You have {counter} attempts left.')
    elif guess == number:
        print('Good Job you have guessed the number')
        break
if counter == 0 and guess != number:
    print(f'Sorry, you have run out of attempts. The correct number was {number}.')