#!/usr/bin/python3
"""function to determine if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """determines if list of given boxes can all be unlocked"""
    keyRing = [0]
    for boxNum in range(len(boxes)):
        if boxNum == 0 or boxNum in keyRing:
            keyRing += boxes[boxNum]
    for boxNum in range(len(boxes)):
        if boxNum in keyRing:
            keyRing += boxes[boxNum]
            continue
        else:
            return False
    return True
