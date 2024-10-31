#!/usr/bin/python3
"""
    Calculate the minimum number of operations to reach
    exactly n 'H' characters in a text file
    starting with a single 'H'. Allowed operations are
    Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to
    reach exactly n 'H' characters.
    """
    if n < 2:
        #If n is 1 or less,we need no operations beyond the initial 'H'
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
