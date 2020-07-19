#!/usr/bin/python3
"""function to determine if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """determines if list of given boxes can all be unlocked"""
    keyRing = []
    for boxNum in range(len(boxes)):
        if boxNum == 0 or boxNum in keyRing:
            keyRing += boxes[boxNum]
    if len(set(keyRing)) == len(boxes) - 1:
        return True
    else:
        return False
