#!/usr/bin/python3
"""
    This module provides utilities to determine if all
    boxes can be unlocked. Each box is represented by an
    index in a list, and may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    n = len(boxes)
    opened_boxes = [False] * n  # Track opened boxes
    opened_boxes[0] = True      # Start with the first box unlocked
    keys = boxes[0]             # Keys found in the first box

    for key in keys:
        if 0 <= key < n and not opened_boxes[key]:
            opened_boxes[key] = True
            keys.extend(boxes[key])  # Add keys from this box to the list

    return all(opened_boxes)
