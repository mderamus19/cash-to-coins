# Convert the dollar amount into the coins that make up
# that dollar amount. The final result is an object
# with the correct number of quarters, dimes, nickels, and pennies.
# This should be the output.
#  print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

for coins in piggyBank.items():

    print(coins)
