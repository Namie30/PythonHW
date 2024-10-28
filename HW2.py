#N1
"""
print('Even or Odd Guesser Program')

a = int(input('Please Input Chosen Number: '))

if a % 2 == 0:
    print("Your Chosen number is Even!")
else:
    print("Your Chosen number is odd!")

"""

#N2
"""
print("Make up a sentence and see if this 3 words(small, tall, middle) are in there")

word = str('small')
word1 = str('tall')
word2 = str('middle')

text = str(input("Please Input you text: ")).lower()

if word in text:
    print(word)
elif word1 in text:
    print(word1)
elif word2 in text: 
    print(word2)
else: 
    print("There is no trace of these 3 words in your text")

"""
#N3
print('Let me help you with you Math HomeWork')

number1 = float(input('Please input your first number: '))
number2 = float(input('Please also input you second number: '))
operator = str(input('Now choose operator(+,-,*,/,%,^): '))

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    print(number1 % number2)
else:
    print(number1 ** number2)