#!/usr/bin/python3
import sys
import signal

# Initialize counters and storage
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# This Function prints the statistics
def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

# Function to handle keyboard interruption (CTRL+C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Attach the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        
        # Parse the line with basic validation
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract relevant parts from the line
        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue  # Skip lines that do not match the expected format
        
        # Accumulate the total file size
        total_file_size += file_size
        
        # Update the status code count if it’s one of the specified codes
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment the line count and print statistics every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # On keyboard interruption, print statistics and exit
    print_statistics()
    sys.exit(0)
