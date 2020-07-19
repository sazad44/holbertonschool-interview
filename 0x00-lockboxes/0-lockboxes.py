#!/usr/bin/python3
"""function to determine if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """determines if list of given boxes can all be unlocked"""
    boxNum = 0
    keyRing = []
    for box in boxes:
        if boxNum in keyRing or boxNum == 0:
            boxNum += 1
            keyRing += box
            continue
        else:
            print(box)
            print(boxNum)
            return False
    return True
