from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  new_word = ''
  for character in text:
    if character in alphabet:

      letter_index = alphabet.index(character)

      if direction == 'encode':
        shifted_index = letter_index + shift
      elif direction == 'decode':
        shifted_index = letter_index - shift

      new_word += alphabet[shifted_index]
    else:
      new_word += character

  if direction == 'encode':
    print(f'The encoded text is {new_word}')
  elif direction == 'decode':
    print(f'The decoded text is {new_word}')

print(logo)

# Something to start the while loop
repeat = 'yes'

while repeat == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Had to look at the challenge answer
  shift = shift % 26
  
  caesar(text, shift, direction)

  repeat = input('Do you want to repeat? Type yes if you do.\n')

print('Goodbye')

