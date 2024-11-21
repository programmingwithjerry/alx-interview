#!/usr/bin/python3
"""
Module for rotating a 2D matrix in place.
"""

def rotate_2d_matrix(matrix):
    """
    Performs an in-place rotation of a 2D matrix (m x n dimensions).
    Args:
        matrix (list): A list of lists representing the 2D matrix.
    Return:
        None: Modifies the input matrix directly.
    """
    # Ensure the input is a list
    if type(matrix) != list:
        return

    # Check that the matrix is non-empty
    if len(matrix) <= 0:
        return

    # Validate that all elements in the matrix are lists
    if not all(map(lambda row: type(row) == list, matrix)):
        return

    # Get the dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Confirm that all rows have the same number of columns
    if not all(map(lambda row: len(row) == num_cols, matrix)):
        return

    col_index, row_index = 0, num_rows - 1
    # Iterate through each element in the matrix
    for i in range(num_cols * num_rows):
        """Start a new row for the rotated matrix after
           every original row's elements"""
        if i % num_rows == 0:
            matrix.append([])

        # Move to the last row and iterate backwards
        if row_index == -1:
            row_index = num_rows - 1
            col_index += 1

        # Append the transposed and reversed element to the new row
        matrix[-1].append(matrix[row_index][col_index])

        # Remove the processed row when finished
        if col_index == num_cols - 1 and row_index >= -1:
            matrix.pop(row_index)

        row_index -= 1
