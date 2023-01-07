from hangman_art import stages, logo
from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
lives = 6

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
  display += '_'

guessed_letters = []

did_game_end = False
did_player_win = False

print(stages[lives])
print(display)

while not did_game_end:

  guess = input('Guess a letter: ').lower()

  if guess in guessed_letters:
    print(f'You already guessed {guess}')
    continue
  else:
    guessed_letters += guess

  for index in range(len(chosen_word)):
    if guess == chosen_word[index]:
      display[index] = guess

  if guess not in chosen_word:
    print(f'{guess} is not part of the word')
    lives -= 1

  if '_' not in display:
    did_game_end = True
    did_player_win = True

  if lives == 0:
    did_game_end = True

  print(stages[lives])

  print(display)

if did_player_win:
  print('You win')
else:
  print('You lose')