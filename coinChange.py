import math

def coinChange(coins, amount):
    """
    This function calculates the fewest number of coins that you need to make
    up a given amount. If that amount of money cannot be made up by any
    combination of the coins, it returns -1.

    Args:
      coins: A list of integers representing the denominations of the coins.
      amount: An integer representing the total amount of money.

    Returns:
      The fewest number of coins needed to make up the amount, or -1 if it's
      not possible.
    """
    # dp[i] will be storing the minimum number of coins required for amount i.
    # We initialize all values to a value larger than any possible number of coins.
    dp = [math.inf] * (amount + 1)

    # The number of coins required for amount 0 is 0.
    dp[0] = 0

    # Sort the coins to potentially optimize the inner loop, though it's not
    # strictly necessary for correctness.
    coins.sort()

    # For each amount from 1 to the target amount...
    for i in range(1, amount + 1):
        # ... and for each coin denomination...
        for coin in coins:
            # If the current coin can be used to make up the current amount...
            if i - coin >= 0:
                # We update the minimum number of coins for the current amount.
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                # Since the coins are sorted, we can break early if the coin
                # is larger than the current amount.
                break

    # If dp[amount] is still math.inf, it means the amount cannot be made up.
    return dp[amount] if dp[amount] != math.inf else -1
 
print(coinChange([1, 3, 4, 5], 7))
