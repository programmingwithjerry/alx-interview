#!/usr/bin/python3

"""Prime game module.
   This module implements a function to determine the winner of
   a prime number game
   based on the given number of rounds and a list of integers.
"""


def isWinner(x, nums):
    """Determines the winner of a prime number game.
    """
    # Handle edge cases: no rounds to play or an empty list of numbers
    if x < 1 or not nums:
        return None

    # Initialize the win counters for Maria and Ben
    maria, ben = 0, 0

    # Identify the largest number across all rounds
    max_n = max(nums)

    """Create a boolean list to identify primes using
    the Sieve of Eratosthenes"""
    primes = [True for _ in range(1, max_n + 1, 1)]
    primes[0] = False  # Mark 1 as non-prime since it's not a prime number

    # Apply the Sieve of Eratosthenes to determine prime numbers
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue  # Skip non-prime numbers and the number 1
        # Mark multiples of the current prime number as non-prime
        for j in range(i + i, max_n + 1, i):
            primes[j - 1] = False

    # Determine the winner for each round
    for _, n in zip(range(x), nums):
        # Count how many numbers up to `n` are prime
        primes_count = len(list(filter(lambda x: x, primes[:n])))

        # Update win counters based on the parity of the prime count
        ben += primes_count % 2 == 0  # Ben wins if count is even
        maria += primes_count % 2 == 1  # Maria wins if count is odd

    # Decide the overall winner or declare a tie
    if maria == ben:
        return None  # Tie
    return 'Maria' if maria > ben else 'Ben'
