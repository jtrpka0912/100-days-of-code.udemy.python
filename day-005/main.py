import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

total_characters = total_letters + total_symbols + total_numbers

password = ''

while total_characters != 0:
  # 0 = Letter, 1 = Symbol, 2 = Number
  choose_character = random.randint(0, 2)

  if choose_character == 0:
    if total_letters != 0:
      random_letter = random.randint(0, len(letters) - 1)
      password += letters[random_letter]
      total_letters -= 1
      total_characters -= 1
    continue

  if choose_character == 1:
    if total_symbols != 0:
      random_symbol = random.randint(0, len(symbols) - 1)
      password += symbols[random_symbol]
      total_symbols -= 1
      total_characters -= 1
    continue

  if choose_character == 2:
    if total_numbers != 0:
      random_number = random.randint(0, len(numbers) - 1)
      password += numbers[random_number]
      total_numbers -= 1
      total_characters -= 1
    continue

print(f"Here is your password: {password}")