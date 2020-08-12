#!/usr/bin/python3
"""function to determine minimum operations for output"""


def minOperations(n):
    """determines min operations to generate n copied output"""
    if not isinstance(n, int) or n <= 1:
        return 0
    opCount = 2
    textLen = len("HH")
    clipB = len("H")
    while textLen < n:
        if n % textLen == 0:
            clipB = textLen
            textLen += clipB
            opCount += 2
        else:
            textLen += clipB
            opCount += 1
    return opCount
