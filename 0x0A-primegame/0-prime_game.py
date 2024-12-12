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

    # Initialize win counters for Maria and Ben
    maria_wins, ben_wins = 0, 0

    # Find the maximum value of n to precompute primes
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for num in range(2, int(max_num**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max_num + 1, num):
                is_prime[multiple] = False

    # Precompute the number of primes up to each number
    primes_up_to = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if is_prime[i] else 0)

    # Evaluate each game round
    for n in nums:
        # Count primes up to n
        prime_count = primes_up_to[n]

        # Determine the winner of the round based on the prime count parity
        if prime_count % 2 == 1:  # Maria wins if the count is odd
            maria_wins += 1
        else:  # Ben wins if the count is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Output should be "Ben"
