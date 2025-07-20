"""
Coin Change Dynamic Programming Algorithm

This module implements the classic coin change problem using dynamic programming.
Given coins of different denominations and a target amount, find the minimum number
of coins needed to make that amount.

Algorithm: Bottom-up dynamic programming
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)

Author: Leetcode Practice
"""

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
        return 0
    t = [0 for _ in range(amount + 1)]
    coins.sort()
    for currAmount in range(1, amount + 1):
        subTable = []
        for currCoin in coins:
            if currAmount - currCoin >= 0 and t[currAmount - currCoin] != -1:
                subTable.append(t[currAmount - currCoin] + 1)
            if len(subTable) == 0:
                t[currAmount] = -1
            else:
                t[currAmount] = min(subTable)
                
    return t[-1]
 
print(coinChange([1, 3, 4, 5], 7))
     
                
