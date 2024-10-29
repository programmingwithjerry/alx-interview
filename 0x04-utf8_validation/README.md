# UTF-8 Validation

## Overview
This project provides tools to validate UTF-8 encoded data. It includes methods to determine if a given data set represents a valid UTF-8 encoding sequence, helping to handle text data integrity in applications.

## Usage
The primary function reads an array of bytes and checks if it follows UTF-8 encoding rules. This is helpful for handling encoded text in various systems, ensuring compatibility with UTF-8 encoding.

## Requirements
- Python 3.7+
- Basic understanding of UTF-8 encoding standards.

## Example
```python
# Example input
data = [197, 130, 1]
print(validUTF8(data)) # Expected output: True
