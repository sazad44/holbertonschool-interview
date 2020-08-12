#!/usr/bin/env python3
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
        if n >= len(start) * 2:
            clipB = start
            opCount += 1
            start += clipB
            opCount += 1
        elif len(start) + len(clipB) == n:
            start += "H"
            opCount += 1
        else:
            start += clipB
            opCount += 1
    if len(start) > n:
        return opCount - 1
    return opCount
