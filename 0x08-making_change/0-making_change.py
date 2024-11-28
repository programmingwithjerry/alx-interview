#!/usr/bin/env python3
"""
This script determines the fewest number of coins needed
to meet a given amount
total using a dynamic programming approach.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet
    a given amount total.

    Args:
        coins (list of int): The values of the coins in possession.
        total (int): The target amount to achieve.

    Return:
        int: Fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    # Populate the DP array
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If total cannot be met, return -1
    return dp[total] if dp[total] != float('inf') else -1
