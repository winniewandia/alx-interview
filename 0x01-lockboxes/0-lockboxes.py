#!/usr/bin/python3
"""Determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (list): list of lists of integers.
    """
    visited = set()
    visited.add(0)
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and key not in visited:
                stack.append(key)
                visited.add(key)
    return len(visited) == len(boxes)
