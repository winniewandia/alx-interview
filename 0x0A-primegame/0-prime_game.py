#!/usr/bin/python3

"""A function that determines the winner of a prime game"""


def isWinner(x, nums):
    """A function that determines the winner of a prime game

    Args:
        x (int): number of rounds
        nums (arr): array of integers

    Returns:
        str: name of the player who wins the most rounds
    """
    if not nums or x < 1:
        return None

    ben = 0
    mar = 0
    if len(nums) != x:
        return None
    for i in range(len(nums)):
        prime = [True for j in range(i+1)]
        p = 2
        while p*p <= i:
            if prime[p]:
                for j in range(p*p, i+1, p):
                    prime[j] = False
            p += 1

        count = 0
        for p in range(2, i+1):
            if prime[p]:
                count += 1
            b = 0
            m = 0
            if count == 0:
                b += 1
                ben += b
            elif count % 2 == 0:
                b += 1
                ben += b
            else:
                m += 1
                mar += m
    if ben < mar:
        return "Maria"
    else:
        return "Ben"
