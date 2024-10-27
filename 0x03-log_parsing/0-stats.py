#!/usr/bin/python3
"""
This script reads lines from standard input (stdin) and calculates specific metrics:
1. The cumulative file size across all lines.
2. Counts for specific HTTP status codes.

The script prints these metrics every 10 lines processed or when interrupted by a keyboard signal (CTRL+C).
"""
import sys


def display_metrics(total_size, status_code_counts):
    """
    Displays the metrics calculated so far:
    - Total file size.
    - Count of each HTTP status code that has been encountered at least once.

    Parameters:
    - total_size (int): The cumulative total of all file sizes processed.
    - status_code_counts (dict): A dictionary mapping HTTP status codes to their respective counts.
    """
    print('File size: {}'.format(total_size))
    # Display counts for each status code, sorted in ascending order
    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))


if __name__ == '__main__':
    # Initialize total file size counter
    total_size = 0

    # Dictionary to track occurrences of specific HTTP status codes
    status_code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        line_count = 0  # Track the number of lines processed
        for line in sys.stdin:
            # Split the line into components and ensure it contains at least the expected number of parts
            args = line.split()
            if len(args) > 6:
                # Extract the status code and file size from the end of the line
                status = args[-2]
                file_size = args[-1]

                # Update the total file size
                total_size += int(file_size)

                # Increment the count for the extracted status code if it is in our defined list
                if status in status_code_counts:
                    line_count += 1
                    status_code_counts[status] += 1

                    # Display metrics after every 10 lines processed
                    if line_count % 10 == 0:
                        display_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Print the final metrics if a keyboard interrupt is detected
        display_metrics(total_size, status_code_counts)
        raise
    else:
        # Print metrics if we reach the end of input
        display_metrics(total_size, status_code_counts)

