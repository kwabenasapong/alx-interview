#!/usr/bin/python3

"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given
amount total.
Write a function `def makeChange(coins, total):
` that returns the fewest number of coins needed to meet the
total. If `total` is `0` or less, return `0`. If `total` cannot
be met by any number of coins you have, return `-1`. Coins are
stored in a list `coins` where the value of each coin will be
the number of cents it is worth. The avaiable coins are
`[1, 2, 5, 10, 25, 50]`.
"""


def makeChange(coins: list, total: int) -> int:
    """
    Write a function `def makeChange(coins, total):
    ` that returns the fewest number of coins needed to meet the
    total. If `total` is `0` or less, return `0`. If `total` cannot
    be met by any number of coins you have, return `-1`.
    """
    if total <= 0:
        return 0
    if coins is None or len(coins) == 0:
        return -1
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            count += total // coin
            total = total % coin
    if total > 0:
        return -1
    return count
