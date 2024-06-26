#!/usr/bin/python3
"""a function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """a function that returns the perimeter of the island described in grid
    """
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 4
                if row > 0 and grid[row - 1][col] == 1:
                    count -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    count -= 2
    return count
