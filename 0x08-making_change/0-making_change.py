#!/usr/bin/python3

"""A function that returns the minimum number of coins needed to make
change for a given total amount.
"""


def makeChange(coins, total):
    """A function that returns the minimum number of
    coins needed to make

    Args:
        coins (list): a list of integers representing the coin values
        total (int): the total amount of change needed

    Returns:
        int: the minimum number of coins needed to make change
    """
    if total <= 0:
        return 0
    n = len(coins)
    for i in range(n):
        for j in range(0, n-i-1):
            if coins[j] < coins[j+1]:
                coins[j], coins[j+1] = coins[j+1], coins[j]

    ans = 0
    for i in range(n):
        while coins[i] <= total:
            total -= coins[i]
            ans += 1
        if total == 0:
            return ans
    return -1
