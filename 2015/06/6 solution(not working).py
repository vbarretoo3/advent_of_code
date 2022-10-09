import numpy as np
from pandas import array

def solve1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]

    grid = np.full([1000,1000], 0)
    for instructions in data:
        words = instructions.split()
        x1, x2 = map(int, words[-3].split(","))
        y1, y2 = map(int, words[-1].split(","))

        if instructions.startswith("turn on"):
            grid[x1:x2+1, y1:y2+1] = 1
        elif instructions.startswith("turn off"):
            grid[x1:x2+1, y1:y2+1] = 0
        elif instructions.startswith("toggle"):
            grid[x1:x2+1, y1:y2+1] = 1 - grid[x1:x2+1, y1:y2+1]
    
    print(grid.sum())

solve1('./2015/06/input.txt')
