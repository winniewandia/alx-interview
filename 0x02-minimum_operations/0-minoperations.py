#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """find the minimum number of operations required to
    generate a number n from 1

    Args:
        n (int): target number
    """
    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for current in range(2, n + 1):
        for factor in range(1, current):
            if current % factor == 0:
                dp[current] = min(dp[current],
                                  dp[factor] + (current //
                                                factor))
    return dp[n] if dp[n] != float('inf') else 0
