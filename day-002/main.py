print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
tip_percentage = 0.01 * int(input('What percentage tip would you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))

split_bill = total_bill / split
tip_amount = split_bill * tip_percentage
total = round(split_bill + tip_amount, 2)

print(f'Each person should pay: {total}')