import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
  display += '_'

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

game_over = False
did_player_win = False

while not game_over:

  guess = input('Guess a letter: ').lower()

  for index in range(len(chosen_word)):
    if guess == chosen_word[index]:
      display[index] = guess

  if '_' not in display:
    game_over = True
    did_player_win = True

  print(display)

if game_over:
  if did_player_win:
    print('You win')
  else:
    print('You lose')