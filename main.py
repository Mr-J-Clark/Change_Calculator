# 1.8 Computational thinking exercise
# Your turn.
# Create a money change calculator. Given a set of possible coins available to the shop attendant, and an
# amount of change they must provide the customer, calculate how many of each coin they should give the
# customer.
# Your finalised program should use an array of coin values, and accept user input of the amount of change
# needed to supply. An example run through might look like...
# How much change do you have to give? 67
# To return 67c, give the customer...
# 1 x 50c coins
# 0 x 20c coins
# 1 x 10c coins
# 1 x 5c coins
## 2 x 1c coins

def calculate_change(amount, coins):
    change = []

    for coin in coins:
        # Determine how many coins of this denomination to give
        num_coins = amount // coin
        change.append(num_coins)
        # Reduce the amount by the total value of those coins
        amount -= num_coins * coin

    return change


def main():
    # Define available coin values in cents
    coins = [50, 20, 10, 5, 1]

    # Accept user input
    amount = int(input("How much change do you have to give? "))

    # Calculate the change
    change = calculate_change(amount, coins)

    # Output the result
    print(f"To return {amount}c, give the customer...")
    for i in range(len(coins)):
        print(f"{change[i]} x {coins[i]}c coins")


main()