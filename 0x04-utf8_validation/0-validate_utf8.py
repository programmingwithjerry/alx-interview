#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Parameters:
    data (list of int): List of integers where each integer represents one byte of data.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes left in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for byte in data:
        # Mask to get only the least significant 8 bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            if (byte & mask1) == 0:
                continue  # 1-byte character (ASCII)
            
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1  # 2-byte character
                
            elif (byte & (mask1 >> 2)) == (mask1 | mask2):
                num_bytes = 2  # 3-byte character
                
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask1 >> 2)):
                num_bytes = 3  # 4-byte character
                
            else:
                return False  # Invalid leading byte

        else:
            # Check that this byte is a continuation byte (10xxxxxx)
            if (byte & mask1) != mask1 or (byte & mask2) == mask2:
                return False

        # Reduce the number of bytes left to read in the current character
        num_bytes -= 1

    # If we finish and there are no bytes left in a character, it's valid UTF-8
    return (num_bytes == 0)
