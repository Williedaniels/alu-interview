#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    # copy all means copy = character
    # paste means character += copy
    character = 1
    copy = character
    min_ops = 0
    while character < n:
        # if n is divisible by character, then double it
        if n % character == 0:
            # copy all and paste is 2 ops
            copy = character
            character = 2 * copy
            min_ops += 2
        else:
            # otherwise add it +1
            # paste
            character += copy
            min_ops += 1
    return min_ops