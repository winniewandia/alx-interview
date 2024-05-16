#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import re


def print_stats(total_size, status_codes):
    """function is used to print out the current statistics

    Args:
        total_size (int): total size of the files
        status_codes (int): dictionary containing the status codes
    """
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """function is used to parse the line

    Args:
        line (std_in): line to be parsed

    Returns:
        dict: ip_address, status_code, file_size
    """
    try:
        pattern = (
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] '
            r'"GET /projects/260 HTTP/1.1" '
            r'(\d{3}) (\d+)'
        )
        match = re.match(pattern, line)
        if match:
            ip_address = match.group(1)
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            return ip_address, status_code, file_size
        else:
            return None, None, None
    except (IndexError, ValueError):
        return None, None, None


def process_logs():
    """function is used to process the logs from the stdin
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is None:
                continue

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


process_logs()
