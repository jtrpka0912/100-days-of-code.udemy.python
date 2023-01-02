import random

choices = ['Rock', 'Paper', 'Scissors']
player_choice = choices[int(input('Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))]
opponent_choice = choices[random.randint(0, 2)]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if player_choice == 'Rock':
  print(rock)
  print('Computer Chose:')
  if opponent_choice == 'Rock':
    print(rock)
    print('A draw')
  elif opponent_choice == 'Paper':
    print(paper)
    print('You lose')
  elif opponent_choice == 'Scissors':
    print(scissors)
    print('You win')

elif player_choice == 'Paper':
  print(paper)
  print('Computer Chose:')
  if opponent_choice == 'Rock':
    print(rock)
    print('You win')
  elif opponent_choice == 'Paper':
    print(paper)
    print('A draw')
  elif opponent_choice == 'Scissors':
    print(scissors)
    print('You lose')

if player_choice == 'Scissors':
  print(scissors)
  print('Computer Chose:')
  if opponent_choice == 'Rock':
    print(rock)
    print('You lose')
  elif opponent_choice == 'Paper':
    print(paper)
    print('You win')
  elif opponent_choice == 'Scissors':
    print(scissors)
    print('A draw')