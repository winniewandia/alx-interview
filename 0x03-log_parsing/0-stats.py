#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


def display_metrics(file_size, status_counts):
    """Display the calculated metrics.

    Args:
        file_size (int): The total file size read so far.
        status_counts (dict): The count of each status code read so far.
    """
    if not isinstance(file_size, int):
        print("Error: file_size must be an integer.")
        return
    if not isinstance(status_counts, dict):
        print("Error: status_counts must be a dictionary.")
        return
    print("File size: {}".format(file_size))
    for key in sorted(
            [k for k in status_counts.keys() if k is not None and
             k in status_counts]):
        print("{}: {}".format(key, status_counts[key]))


if __name__ == "__main__":
    import sys
    total_size = 0
    status_counts = {}
    valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for log_line in sys.stdin:
            line_count += 1

            if line_count == 10:
                display_metrics(total_size, status_counts)
                line_count = 0

            log_parts = log_line.split()

            try:
                total_size += int(log_parts[-1])
            except (IndexError, ValueError):
                continue

            try:
                status = log_parts[-2]
                if status in valid_statuses:
                    status_counts[status] = status_counts.get(status, 0) + 1
            except IndexError:
                continue

        display_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        display_metrics(total_size, status_counts)
        raise
