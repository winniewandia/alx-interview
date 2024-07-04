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
    for num in nums:
        prime = [True for j in range(num+1)]
        p = 2
        while p*p <= num:
            if prime[p]:
                for j in range(p*p, num+1, p):
                    prime[j] = False
            p += 1

        count = 0
        for j in range(2, num+1):
            if prime[j]:
                count += 1
        if count == 0:
            ben += 1
        elif count % 2 == 0:
            ben += 1
        else:
            mar += 1
    if ben < mar:
        return "Maria"
    else:
        return "Ben"


# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
# print("Winner: {}".format(isWinner(1, [2])))
