#!/usr/bin/env python3
"""
Determine the winner of a game where players take turns picking primes
and removing them and their multiples.
"""

def isWinner(x, nums):
    """
    Determine who wins the most rounds.
    """
    if not nums or x < 1:
        return None

    # Find the maximum value of n to precompute primes
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    # Precompute the number of primes up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner of each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

