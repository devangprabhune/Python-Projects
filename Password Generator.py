print("Password Generator")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '|', ';', ':', ',', '<', '.', '>', 
    '/', '?']

print("Welcome to Password Generator")
letters_cnt= int(input("How many letters would you like ?" ))
numbers_cnt = int(input("How many numbers would you like ?" ))
symbols_cnt = int(input("How many symbols would you like ?" ))

#initialize an empty password > level easy
# password = ""
# for char in range(0, letters_cnt):
#     password+= random.choice(letters)

# for num in range(0, numbers_cnt):
#     password+= random.choice(numbers)

# for sym in range(0,symbols_cnt):
#     password+= random.choice(symbols)

# print(password)

#level hard

password_list = []

for char in range(0, letters_cnt):
    password_list.append(random.choice(letters))

for num in range(0, numbers_cnt):
    password_list.append(random.choice(numbers))

for sym in range(0, symbols_cnt):
    password_list.append(random.choice(symbols))

password = ""
# for i in range(0, len(password_list)):
#     password += random.choice(password_list)

random.shuffle(password_list)
print(password_list)
for _ in password_list:
    password += _
print(f"your password is {password_list}")
