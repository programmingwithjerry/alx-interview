#!/usr/bin/python3
""" For Pascal's triangle."""
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    Parameters:
    n (int): The number of rows in Pascal's Triangle to generate.
    
    Return:
    list: A list of lists containing integers,
    representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        # Fill in the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
