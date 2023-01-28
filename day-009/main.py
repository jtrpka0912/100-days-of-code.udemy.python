from art import logo
import os

print(logo)

print('Welcome to the secret auction program.')

auctioneers = {}

to_continue = True;
while to_continue == True:
  name = input('What is your name?: ')
  bid = float(input('What\'s your bid?: $'))
  auctioneers[name] = bid

  is_more = input('Are there any other bidders? Type \'yes\' or \'no\'. ').lower()

  if is_more != 'yes':
    to_continue = False

  os.system('clear')

highest_bid = 0
highest_auctioneer = ''
for auctioneer in auctioneers:
  bid = auctioneers[auctioneer]
  
  if bid > highest_bid:
    highest_bid = bid
    highest_auctioneer = auctioneer

print(f'The winner is {highest_auctioneer} with a bid of ${highest_bid}')