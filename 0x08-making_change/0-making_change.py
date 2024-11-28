#!/usr/bin/python3
"""Calculate the minimum number of coins needed
   to reach a specific amount.
"""


def makeChange(coins, total):
    """Determine the minimum coins required to reach the total amount.
    """
    if total <= 0:
        return 0

    accumulated = 0  # Tracks the running total of coin values used
    coin_counter = 0  # Tracks the number of coins used
    coins.sort(reverse=True)  # Sort coins in descending order

    for denomination in coins:
        while accumulated < total:
            accumulated += denomination
            coin_counter += 1
        if accumulated == total:
            return coin_counter
        # Backtrack if we exceed the total
        accumulated -= denomination
        coin_counter -= 1

    return -1
