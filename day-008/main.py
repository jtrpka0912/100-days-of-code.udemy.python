alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
  new_word = ''
  for letter in text:
    letter_index = alphabet.index(letter)

    if direction == 'encode':
      shifted_index = letter_index + shift
    elif direction == 'decode':
      shifted_index = letter_index - shift

    if shifted_index >= (len(alphabet)):
      shifted_index -= len(alphabet)

    new_word += alphabet[shifted_index]

  if direction == 'encode':
    print(f'The encoded text is {new_word}')
  elif direction == 'decode':
    print(f'The decoded text is {new_word}')


caesar(text, shift, direction)