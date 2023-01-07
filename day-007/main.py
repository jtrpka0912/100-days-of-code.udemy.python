import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
  display += '_'

guess = input('Guess a letter: ').lower()

for index in range(len(chosen_word)):
  if guess == chosen_word[index]:
    display[index] = guess

print(display)