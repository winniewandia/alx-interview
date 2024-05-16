#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (IndexError, ValueError):
        return None, None, None


def process_logs():
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
