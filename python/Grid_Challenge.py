#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for index in range(len(grid)):
        row = grid[index]
        grid[index] = sorted(row)
    print(grid)
    for col in range(len(grid[0])):
        for row in range((len(grid))-1):
            if grid[row][col] > grid[row+1][col]:
                return "NO"
    return "YES"
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)



