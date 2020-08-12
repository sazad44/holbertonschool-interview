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
        if n % len(start) == 0:
            clipB = start
            start += clipB
            opCount += 2
        else:
            start += clipB
            opCount += 1
    return opCount
