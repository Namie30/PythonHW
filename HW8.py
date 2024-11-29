#1 With Function
"""
def anagram_checker(s1, s2):
        letters1 = {}
        letters2 = {}

        for i in range(len(s1)):
            letters1[s1[i]] = letters1.get(s1[i], 0) + 1
            letters2[s2[i]] = letters2.get(s2[i], 0) + 1

        return letters2 == letters1

print(anagram_checker("listen", "silent"))
print(anagram_checker("something", "some1hing"))
"""
"""
#funqciis gareshe gavaketebdit ase
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("something", "some1hing"))
"""
#N2
# def symbol_checker(text, s):
#     letters = {}
#     for char in text:
#         letters[char] = letters.get(char, 0) + 1
#
#     return letters.get(s, 0)
#
# print(symbol_checker("hello", "l"))
# print(symbol_checker("hello", "x"))

#3
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
print(fib(4))











