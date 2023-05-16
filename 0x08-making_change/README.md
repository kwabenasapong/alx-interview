# 0x08-making_change

## Description

### Project intended to learn:

- Python

## Task Project

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total. Write a function `def makeChange(coins, total):` that returns the fewest number of coins needed to meet the total. If `total` is `0` or less, return `0`. If `total` cannot be met by any number of coins you have, return `-1`. Coins are stored in a list `coins` where the value of each coin will be the number of cents it is worth. The avaiable coins are `[1, 2, 5, 10, 25, 50]`.

```sh
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([2], 3))

guillaume@ubuntu:~/0x08$ ./0-main.py
7
-1
guillaume@ubuntu:~/0x08$ 
```
