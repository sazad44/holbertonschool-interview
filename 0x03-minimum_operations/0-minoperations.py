#!/usr/bin/python3
"""function to determine minimum operations for output"""


def minOperations(n):
    """determines min operations to generate n copied output"""
    if n == 1:
        return n
    elif n <= 0:
        return 0
    opCount = 2
    start = "HH"
    clipB = "H"
    while len(start) < n:
        if n >= len(start) * 2 and n % 2 == 0:
            start *= 2
            opCount += 2
            clipB = start
        else:
            start += clipB
            opCount += 1
    return opCount
