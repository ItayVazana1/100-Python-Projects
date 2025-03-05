# Day 5 project - Strong Password Generator
# random characters and also random order (so no pattern like letter-number-symbol) --> (Hard level)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '@', '#', '$', '^', '&', '*', '+', '-', '/']

print("Welcome to the Password Generator!")
number_of_letters = int(input("How many letters you want in your password?"))
number_of_numbers = int(input("How many numbers you want in your password?"))
number_of_symbols = int(input("How many symbols you want in your password?"))

list_characters = []

pass_length = number_of_symbols + number_of_letters + number_of_numbers

for i in range(0,number_of_letters):
    list_characters.append(random.choice(letters))

for i in range(0,number_of_numbers):
    list_characters.append(str(random.choice(numbers)))

for i in range(0,number_of_symbols):
    list_characters.append(random.choice(symbols))

print(list_characters)
password = ""

for i in range(0,len(list_characters)-1):
    c = random.choice(list_characters)
    password += c
    list_characters.remove(c)


print(f"Your generated password: {password}")