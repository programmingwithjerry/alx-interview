#!/usr/bin/python3
'''Solving the N-Queens Problem'''

import sys

if __name__ == '__main__':
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Ensure the argument is a valid integer
    try:
        num_queens = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    # Verify that N is at least 4
    if num_queens < 4:
        print('N must be at least 4')
        exit(1)

    all_solutions = []
    current_placement = []  # format [row, col]
    finished = False
    row = 0
    col = 0

    # Traverse through rows
    while row < num_queens:
        backtrack = False
        # Traverse through columns
        while col < num_queens:
            # Check if the current column is valid for placement
            is_valid = True
            for queen in current_placement:
                queen_col = queen[1]
                if (queen_col == col or 
                    queen_col + (row - queen[0]) == col or 
                    queen_col - (row - queen[0]) == col):
                    is_valid = False
                    break

            if not is_valid:
                if col == num_queens - 1:
                    backtrack = True
                    break
                col += 1
                continue

            # Place the queen
            current_placement.append([row, col])
            # If last row is reached, record the solution and reset to the last row
            # and the last valid column in that row
            if row == num_queens - 1:
                all_solutions.append(current_placement[:])
                for queen in current_placement:
                    if queen[1] < num_queens - 1:
                        row = queen[0]
                        col = queen[1]
                for _ in range(num_queens - row):
                    current_placement.pop()
                if row == num_queens - 1 and col == num_queens - 1:
                    current_placement = []
                    finished = True
                row -= 1
                col += 1
            else:
                col = 0
            break
        if finished:
            break
        # If unable to place a queen, backtrack to the previous row
        # and move to the next column
        if backtrack:
            row -= 1
            while row >= 0:
                col = current_placement[row][1] + 1
                del current_placement[row]  # Remove the last queen's position
                if col < num_queens:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    # Print all solutions
    for index, solution in enumerate(all_solutions):
        if index == len(all_solutions) - 1:
            print(solution, end='')
        else:
            print(solution)
