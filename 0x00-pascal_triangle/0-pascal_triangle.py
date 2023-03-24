#!/usr/bin/python3
""" Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer """
import math


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal’s triangle of n """
    if n <= 0:
        return []
    else:
        pascal = []
        for i in range(n):
            pascal.append([])
            for j in range(i + 1):
                pascal[i].append(math.factorial(
                    i) // (math.factorial(j) * math.factorial(i - j)))
        return pascal


if __name__ == "__main__":
    pascal_triangle(n)
