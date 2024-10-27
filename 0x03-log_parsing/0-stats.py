#!/usr/bin/python3
"""Reads from standard input and computes running metrics.

After every ten lines or upon receiving a keyboard interruption (CTRL + C),
outputs:
    - The cumulative file size.
    - The count of each encountered status code.
"""

def display_summary(file_size, code_counts):
    """Prints the computed metrics.

    Args:
        file_size (int): The cumulative file size.
        code_counts (dict): A dictionary with status code counts.
    """
    print("File size: {}".format(file_size))
    for code in sorted(code_counts):
        print("{}: {}".format(code, code_counts[code]))

if __name__ == "__main__":
    import sys

    file_size = 0
    code_counts = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_counter = 0

    try:
        for line in sys.stdin:
            if line_counter == 10:
                display_summary(file_size, code_counts)
                line_counter = 1
            else:
                line_counter += 1

            parts = line.split()

            # Accumulate file size if the last element is a valid integer
            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Count occurrences of valid status codes
            try:
                status_code = parts[-2]
                if status_code in valid_status_codes:
                    code_counts[status_code] = code_counts.get(status_code, 0) + 1
            except IndexError:
                pass

        # Final summary output after reading all lines
        display_summary(file_size, code_counts)

    except KeyboardInterrupt:
        # Output the current metrics if interrupted
        display_summary(file_size, code_counts)
        raise
