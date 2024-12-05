#!/usr/bin/python3
"""This Defines island perimeter finding function."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a 2D grid.
    """

    # Get the number of columns and rows in the grid
    num_columns = len(grid[0])
    num_rows = len(grid)

    # Variables to track the total land cells and shared sides
    #between adjacent land cells
    shared_sides = 0
    land_cells = 0

    # Iterate through each cell in the grid
    for row in range(num_rows):
        for col in range(num_columns):
            # Check if the current cell is a land cell
            if grid[row][col] == 1:
                land_cells += 1  # Increment the count of land cells

                # Check for a land cell to the left and count shared sides
                if col > 0 and grid[row][col - 1] == 1:
                    shared_sides += 1

                # Check for a land cell above and count shared sides
                if row > 0 and grid[row - 1][col] == 1:
                    shared_sides += 1

    # Calculate the total perimeter: each land cell has 4 sides,
    # but shared sides reduce the perimeter by 2 for each shared side
    return land_cells * 4 - shared_sides * 2
