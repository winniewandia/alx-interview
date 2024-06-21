#!/usr/bin/python3

"""UTF-8 Validation
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    Args:
        data (list): a list of integers
    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise
    """

    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set
    mask2 = 1 << 6

    # For each integer in the data list
    for num in data:

        # Get the most significant bit
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:

            # If the current number is a continuation byte
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
