#!/usr/bin/python3
"""
Log Parsing: Reads from standard input, tracking file size and status code counts.
"""

import sys

if __name__ == '__main__':

    total_file_size, line_counter = 0, 0
    tracked_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code_counts = {code: 0 for code in tracked_codes}

    def display_metrics(code_counts: dict, total_file_size: int) -> None:
        """Outputs cumulative file size and counts for each tracked status code."""
        print("File size: {:d}".format(total_file_size))
        for code, count in sorted(code_counts.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            line_counter += 1
            data_parts = line.split()
            
            # Increment count for recognized status codes
            try:
                status_code = data_parts[-2]
                if status_code in code_counts:
                    code_counts[status_code] += 1
            except IndexError:
                pass
            
            # Add to total file size if last element is a valid integer
            try:
                total_file_size += int(data_parts[-1])
            except (IndexError, ValueError):
                pass
            
            # Display metrics after every 10 lines
            if line_counter % 10 == 0:
                display_metrics(code_counts, total_file_size)
        
        # Final output after processing all lines
        display_metrics(code_counts, total_file_size)

    except KeyboardInterrupt:
        # Output metrics on keyboard interruption
        display_metrics(code_counts, total_file_size)
        raise
