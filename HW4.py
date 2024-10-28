#1
"""
txt = input('Lets determine if your given text is a palindrome. Please input the text: ')
if txt == txt[::-1]:
    print('Given text is palindrome')
else:
    print('Given text is not palindrome')
"""

#2

txt = input('Lets turn your given text into ASCII sequence: ')

ascii_values = [ord(char) for char in txt]
print(f"Ascii values are: {ascii_values}")